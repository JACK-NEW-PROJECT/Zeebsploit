#-*- coding: utf-8 -*-
# codename: jaxBCD
# github: https://github.com/jaxBCD

from lib.main import gwe_serius
from lib.main import log_
import os,readline,sys
log = log_()
if sys.version[0] in '2':
   log.log(40,"this tool only support for python 3.x")
   exit()

tanya = input('Do you want to check for update?[y/n]: ').lower()
if tanya == 'y':
   os.system('git pull')
   exit()
else:
   print('!type "help" for show modules\n!type "exit" for logout from tool\n!type "back" for back to main menu')
   gwe_serius()

