import sublime, sublime_plugin  
import sys
import os
import webbrowser
egg_path=os.path.join(sublime.packages_path(),'pastebinplugin/pastebin-1.1.1-py2.7.egg')
sys.path.append(egg_path)
from Pastebin import PastebinAPI as api
class pastepluginCommand(sublime_plugin.TextCommand):  
    def run(self,args):
        syntaxes = {
      'ActionScript.tmLanguage': 'actionscript',
      'AppleScript.tmLanguage': 'applescript',
      'ASP.tmLanguage': 'asp',
      'Bibtex.tmLanguage': 'bibtex',
      'C.tmLanguage': 'c',
      'C#.tmLanguage': 'csharp',
      'C++.tmLanguage': 'cpp',
      'Clojure.tmLanguage': 'clojure',
      'CoffeeScript.tmLanguage': 'coffeescript',
      'CSS.tmLanguage': 'css',
      'D.tmLanguage': 'd',
      'Diff.tmLanguage': 'diff',
      'DOT.tmLanguage': 'dot',
      'Erlang.tmLanguage': 'erlang',
      'Go.tmLanguage': 'go',
      'Groovy.tmLanguage': 'groovy',
      'Haskell.tmLanguage': 'haskell',
      'HTML.tmLanguage': 'html5',
      'Java.tmLanguage': 'java',
      'JavaScript.tmLanguage': 'javascript',
      'JSON.tmLanguage': 'javascript',
      'JSON Generic Array Elements.tmLanguage': 'javascript',
      'LaTeX.tmLanguage': 'latex',
      'LaTeX Beamer.tmLanguage': 'latex',
      'LaTeX Memoir.tmLanguage': 'latex',
      'Lisp.tmLanguage': 'lisp',
      'Literate Haskell.tmLanguage': 'haskell',
      'Lua.tmLanguage': 'lua',
      'Makefile.tmLanguage': 'make',
      'Matlab.tmLanguage': 'matlab',
      'Objective-C.tmLanguage': 'objc',
      'Objective-C++.tmLanguage': 'objc',
      'OCaml.tmLanguage': 'ocaml',
      'OCamllex.tmLanguage': 'ocaml',
      'OCamlyacc.tmLanguage': 'ocaml',
      'Perl.tmLanguage': 'perl',
      'PHP.tmLanguage': 'php',
      'Plain text.tmLanguage': 'text',
      'Python.tmLanguage': 'python',
      'R.tmLanguage': 'rsplus',
      'R Console.tmLanguage': 'rsplus',
      'Regular Expressions (Python).tmLanguage': 'python',
      'Ruby.tmLanguage': 'ruby',
      'Ruby Haml.tmLanguage': 'ruby',
      'Ruby on Rails.tmLanguage': 'rails',
      'Scala.tmLanguage': 'scala',
      'SCSS.tmLanguage': 'css',
      'Shell-Unix-Generic.tmLanguage': 'bash',
      'SQL.tmLanguage': 'sql',
      'SQL (Rails).tmLanguage': 'sql',
      'Tcl.tmLanguage': 'tcl',
      'TeX.tmLanguage': 'latex',
      'TeX Math.tmLanguage': 'latex',
      'Textile.tmLanguage': 'latex',
      'XML.tmLanguage': 'xml',
      'YAML.tmLanguage': 'yaml'
    }
        if self.view.sel()[0].size():
            paste_code= '\n'.join([self.view.substr(selection) for selection in self.view.sel()])
            syntax = syntaxes.get(self.view.settings().get('syntax').split('/')[-1], 'text')
            x=api()
            dev_key='you dev key here'
            url=x.paste(dev_key, paste_code, 
                   paste_format = syntax
                   )
            webbrowser.open(url)
