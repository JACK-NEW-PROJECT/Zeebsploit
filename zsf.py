#-*- coding: utf-8 -*-
# codename: JaxBCD
# github: https://github.com/jaxBCD

import sys,readline,os
from zeeb_src import main

tanya = input('Do you want to check for update?[y/n]: ').lower()
if tanya == 'y':
   os.system('git pull')
   exit()
else:
   main()