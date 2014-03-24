#What is it?
This is a sublime text 2 plugin that pastes your selected text to <http://pastebin.com/> and opens it in webbrowser.




#How to install?
1. Create directory 'pastebinplugin' in Packages directory. (find Packages directory with sublime.packages_path() in sublime console)

2. get the pastebin egg from either [pypi](https://pypi.python.org/pypi/Pastebin) or install it with pip and look for the egg in site-packages directory in main python directory. copy this file to the 'pastebinplugin' directory

3. copy pastebinplugin.py inside directory 'pastebinplugin'. 

4. assign dev_key variable to your developer key(get it from pastebin, you need to make an account for it, free ofcourse)

5. set up a key binding by putting this in the user keybinding list(Preferences>Key Bindings-User)
```{ "keys": ["f1"], "command": "pasteplugin" }``` (within the ```[...]``` ofcourse)
this will bind ```F1``` key to the command.

6. To use, **select the text** you want to post to pastebin and press ```F1``` key.