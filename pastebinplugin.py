import sublime, sublime_plugin  
import sys
import os
import webbrowser
egg_path=os.path.join(sublime.packages_path(),'pastebinplugin/pastebin-1.1.1-py2.7.egg')
sys.path.append(egg_path)
from Pastebin import PastebinAPI as api
class pastepluginCommand(sublime_plugin.TextCommand):  
    def run(self,args):
        if self.view.sel()[0].size():
            paste_code= '\n'.join([self.view.substr(selection) for selection in self.view.sel()])
            x=api()
            dev_key='your developer key'
            url=x.paste(dev_key, paste_code, 
                   paste_format = 'Python'
                   )
            webbrowser.open(url)