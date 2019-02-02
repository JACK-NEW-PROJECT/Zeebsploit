#-*- coding: utf-8 -*-
# https://github.com/jaxBCD
# codename : jaxbcd
# facebook : https://www.facebook.com/jaka.lesmana.794628
# Team : 407 Authentic exploit
from __future__ import print_function
import sys,os
from zsf.zeeb_mank import *
print_function

if sys.version[0] == '2':
   print('\n')
   print('[!] This Tool Only support for python 3.x')
   print('\n')
   sys.exit()
else:
   while True:
         beb = input('[?] Do you want to check For update ? [y/n] ').lower()
         if beb == 'y':
            os.system('git pull')
            print('[!] Type python zeebsploit.py to run the tool\n')
         elif beb == 'n':
            main()
         else:
            print('[!] Type "y" or "n" only')

