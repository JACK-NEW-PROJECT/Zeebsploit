#-*- coding: utf-8 -*-
# https://github.com/jaxBCD
# codename : jaxbcd
# facebook : https://www.facebook.com/jaka.lesmana.794628
# Team : 407 Authentic exploit
from __future__ import print_function
import sys,os
from zsf.zeeb_mank import *
print_function

if sys.version[0] in '2':
   print('[!] Use Python 3 To Run This Tool')
else:
   if sys.platform in ['linux','linux2']:
       while True:
             try:
                 op = input('[?] Do you Want To check For update? [y/n]').lower()
                 if 'y' in op:
                     os.system('git pull')
                     print('[!] Success Now type python3 zeebsploit.py')
                     break
                 elif 'n' in op:
                     main()
                 else:
                     print('[!] Type y or n only')
             except KeyboardInterrupt:
                 break
             except EOFError:
                 break

   else:
       print('[!] Sorry This Tool only Support For Linux ')
