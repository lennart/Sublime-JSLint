import sublime
import sublime_plugin
import os
import json

package = 'Sublime-JSLint'


def get_settings_value(key):
    settings1 = sublime.load_settings(package + '.sublime-settings')

    return settings1.get(key)

class JslintCommand(sublime_plugin.TextCommand):
    edit = {}

    def show_errors(self, jslint):
        return get_settings_value('show_errors_on_save') and jslint['totalErrors'] > 0

    def notify(self, jslint):
        images_dir = os.path.join(sublime.packages_path(), package) + '/images/'

        if jslint['totalErrors'] > 0:
            image = 'error.png'
        else:
            image = 'success.png'

        os.popen(get_settings_value("notification_command") % {"msg": jslint['file'], "title": jslint['shortlog'], "image": images_dir + image})

    def run(self, edit, fn='', log_level='shortlog'):
        syntax, extension = os.path.splitext(os.path.basename(self.view.settings().get('syntax')))

        if syntax == 'JavaScript':
            self.edit = edit

            package_dir = os.path.join(sublime.packages_path(), package)

            if fn == '':
                fn = self.view.file_name()

            jslint = json.loads(os.popen(get_settings_value("node_path") + ' "%(linter)s" --%(log_level)s "%(file)s"' % {'linter': package_dir + '/linter.js', 'log_level': log_level, 'file': fn}).read())

            if get_settings_value('show_notification_on_save') and (log_level == 'all' or log_level == 'shortlog'):
                self.notify(jslint)

            if log_level == 'all' or log_level == 'log' or self.show_errors(jslint):
                self.show_panel(jslint)

    def show_panel(self, jslint):
        output_view = self.view.window().get_output_panel('jslint')

        output_view.settings().set("result_file_regex", get_settings_value('result_file_regex'))
        output_view.settings().set("result_line_regex", get_settings_value('result_line_regex'))
        output_view.settings().set("result_base_dir", os.path.dirname(self.view.file_name()))

        output_view.insert(self.edit, 0, jslint['log'])

        # Set the selection to the beginning of the output_view to make result search work as soon as the panel appears (see exec.py in the Default package)
        edit = output_view.begin_edit()
        output_view.sel().clear()
        output_view.sel().add(sublime.Region(0))
        output_view.end_edit(edit)

        self.view.window().run_command('show_panel', {'panel': 'output.jslint'})


class ApplyJslintOnJavaScriptSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if get_settings_value('show_notification_on_save') or get_settings_value('show_errors_on_save'):
            view.run_command('jslint')
