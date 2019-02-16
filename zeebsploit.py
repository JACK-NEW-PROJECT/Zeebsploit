# -*- coding: utf-8 -*-
# github  : https://github.com/jaxBCD
# contact : https://www.facebook.com/jaka.lesmana.794628
# Team : 407 Authentic Exploit
# Join my Team : https://www.facebook.com/groups/1217219985083200
import sys,os
if sys.version[0] in '2':
   print('This Tool Only support For python3')
   sys.exit()

from lib.start import main

class __main(object):

     def start(self):
         main()

while True:
       x = str(input('Do You want To Check For update? [y/n] ')).lower()
       if x == 'y':
          os.system('apt-get update && apt-get upgrade')
          os.system('git pull')
          os.system('python3 -m pip install -r requirements.txt')
          os.system('python3 -m pip install --upgrade -r requirements.txt')
          exit('')
       elif x == 'n':
            __main().start()
       else:
          print('type y/n only') 

