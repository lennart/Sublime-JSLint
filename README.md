Cross-Platform JSLint Support for Sublime Text Editor 2 (using NodeJS)
========================

JSLint is an indispensable tool if you're serious about your JavaScript code quality. This project provides a cross-platform script which helps Sublime Text 2 to check JSLint when you’re working within a JavaScript file.

Features
-------------

- JSLint Validation using NodeJS

- Notification support using Growl (http://growl.info/) on OSX and notify-send on Linux. Those settings are configurable on "sublime-jslint (Linux).sublime-settings", "sublime-jslint (OSX).sublime-settings", and "sublime-jslint (Windows).sublime-settings".

How to use?
-------------

- If you are using Ubuntu install "notify-send" command line:

	apt-get install libnotify-bin

- If you are using OSX install "growlnotify" command line:

	Download the latest Growl version from http://growl.info/downloads, inside the .dmg file, go to "Extras" folder and install "growlnotify.pkg".

- If you are not using the deafult paths from the recommended installation for growlnotify or notify-send, make sure you update the "node_path" and "notification_command" on your system to the right paths.

	{
		"node_path": "/usr/local/bin/node",
		"notification_command": "/usr/bin/notify-send \"%(title)s\" \"%(msg)s\" --icon=\"%(image)s\""
	}

- Access via Command Palette (Ctrl+Shift+P) then search for:

	- JSLint: Quick Check (Ctrl+Shift+L)
	- JSLint: View Full Report (Ctrl+Shift+Alt+L)

Open up a .js file and hit Ctrl+Shift+L for Quick Report and Ctrl+Shift+Alt+L. An inline prompt will appear giving you the JSLint results:

Screenshots
-------------

![](https://github.com/eduardolundgren/sublime-jslint/raw/master/images/screenshot.png)
![](https://github.com/eduardolundgren/sublime-jslint/raw/master/images/preview.png)

Changeset
-------------

Rhino is no longer being used as default engine due to performance issues, NodeJS (http://nodejs.org/) is now being used instead.