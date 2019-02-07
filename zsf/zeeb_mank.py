#-*- coding: utf-8 -*-
from readline import set_pre_input_hook
from .core.temp import logo
from .core.helper import Helper as help
from .core.temp import loading
set_pre_input_hook()
from . import aex
import sys

def bingung():
    campret = '[!] Type "Exit" For Exit from This Tool\n[!] Type "help" for show modules\n '
    print('\n')
    print(campret)
    print('\n')
    while True:
          try:
             nm = input('[zsf]: ').lower()
             if 'infoga' in nm:
                 aex.infoga()
             elif 'scanners' in nm:
                 aex.web_scan()
             elif 'exploit' in nm:
                 aex.exploiter()
             elif 'help' in nm:
                 print('\n')
                 print('[!] type one of the module names to use')
                 help.utama()
                 print('\n')
             elif 'exit' in nm:
                 exit('Exit !')
             else:
                 print('')
                 print('No Command '+nm)
                 print('')
          except EOFError:
             break
             exit()
          except KeyboardInterrupt:
             break
             exit()


def main():
    loading('[*] starting zeebsploit framework')
    print(logo)
    bingung()
