#-*- coding: utf-8 -*-
# https://github.com/jaxBCD
# codename : jaxbcd
# facebook : https://www.facebook.com/jaka.lesmana.794628
# Team : 407 Authentic exploit
import sys,os
from zsf.zeeb_mank import *


if sys.version[0] in '2':
   print('[!] Use Python 3 To Run This Tool')
else:
   if sys.platform in ['linux','linux2']:
       while True:
             try:
                 op = input('[?] Do you Want To check For update? [y/n]').lower()
                 if 'y' in op:
                     os.system('git pull')
                     os.system('python3 -m pip install -r requirements.txt')
                     print('[!] Success Now type "python3 zeebsploit.py"')
                     sys.exit("....")
                 elif 'n' in op:
                     main()
                 else:
                     print('[!] Type y or n only')
             except KeyboardInterrupt:
                 sys.exit('aborted..')
             except EOFError:
                 sys.exit('aborted..')

   else:
       print('[!] Sorry This Tool only Support For Linux ')
