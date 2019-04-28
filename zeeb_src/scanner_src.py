#-*- coding: utf-8 -*-
from .lib import (
    sub_enum,
    fuzzer
)
from .utils import (
    scanners_modules,
    log,
    sql_errors,
    takeover_re,
    proto,
    no_proto,
    show,
    description
    
)
import os,readline,asyncio
log = log(__name__)

mod = scanners_modules
def main():
    while True:  
          try:
              inp = input('zsf(\033[91mscanner\033[0m): ').lower()
              if inp == mod[0]:
                 x = sub_enum(no_proto('domain: '))
                 log.log(10,'mapping subdomain...')
                 x.DNSdumpster()
                 for i in x.raw_result:
                     print(f'- {i}')
              elif inp == mod[1]:
                   url = proto(input('url: '))
                   if '=' not in url:
                      log.log(20,'no parameter found')
                   else:
                      fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/xss_payload.fuzz')
                      loop = asyncio.get_event_loop()
                      loop.run_until_complete(fuz._fetch('xss'))
                      if len(fuz.raw_xss_result) == 0:
                         log.log(30,'target might be not vulnerability xss')
                      else:
                         log.log(10,'vulnerability found')
                         for i in fuz.raw_xss_result:
                             log.log(50,f'{i}')
              elif inp == mod[2]:
                   url = proto(input('url: '))
                   if '=' not in url:
                      log.log(20,'no parameter found')
                   else:
                      x = fuzzer.sqli_scan(url,sql_errors)
                      if x[0] == 0:
                         log.log(30,'not vulnerability sql injection')
                      else:
                         log.log(50,'vulnerability Found')
                         log.log(10,f'type: {x[1]}')
                         log.log(10,f'error: {x[2]}')
              elif inp == mod[3]:
                   url = proto(input('url: '))
                   if '=' not in url:
                      log.log(20,'no parameter found')
                   else:
                      fuzzer.lfi_scanner(url)
              elif inp == mod[4]:
                   url = proto(input('subdomain: '))
                   x = fuzzer.subdomain_takeover(url,takeover_re)
                   if x == '':
                      log.log(30,'no takeover detect')
                   else:
                      log.log(50,f'takeover detect: {x}')
              elif inp == mod[5]:
                   url = proto(input('url: '))
                   fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/admin-panel.fuzz')
                   loop = asyncio.get_event_loop()
                   loop.run_until_complete(fuz._fetch('None'))
                   if len(fuz.raw_fuzz) == 0:
                      log.log(30,'no panel login found')
                   else:
                      for i in fuz.raw_fuzz:
                          log.log(50,f'panel login found: {i}')
              elif inp == mod[6]:
                   url = proto(input('url: '))
                   fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/wp-plugin.fuzz')
                   loop = asyncio.get_event_loop()
                   loop.run_until_complete(fuz._fetch('None'))
                   if len(fuz.raw_fuzz) == 0:
                      log.log(30,'no plugin found')
                   else:
                      for i in fuz.raw_fuzz:
                          log.log(50,f'plugin found: {i}')
              elif inp == mod[7]:
                   url = proto(input('url: '))
                   fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/wp-theme.fuzz')
                   loop = asyncio.get_event_loop()
                   loop.run_until_complete(fuz._fetch('None'))
                   if len(fuz.raw_fuzz) == 0:
                      log.log(30,'no plugin theme found')
                   else:
                      for i in fuz.raw_fuzz:
                          log.log(50,f'plugin theme found: {i}')       
              elif inp == mod[8]:
                   url = proto(input('url: '))
                   fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/joomla-plugin.fuzz')
                   loop = asyncio.get_event_loop()
                   loop.run_until_complete(fuz._fetch('None'))
                   if len(fuz.raw_fuzz) == 0:
                      log.log(30,'no joomla component found')
                   else:
                      for i in fuz.raw_fuzz:
                          log.log(50,f'joomla component found: {i}') 
              elif inp == mod[9]:
                   url = proto(input('url: '))
                   os.system('dirhunt %s' % url)
              elif inp == mod[10]:
                   url = proto(input('url: '))
                   fuz = fuzzer(url,f'{os.getcwd()}/zeeb_src/utils/wordlist/sensitive_file.fuzz')
                   loop = asyncio.get_event_loop()
                   loop.run_until_complete(fuz._fetch('None'))
                   if len(fuz.raw_fuzz) == 0:
                      log.log(30,'no sensitive file found')
                   else:
                      for i in fuz.raw_fuzz:
                          log.log(50,f'sensitive file found: {i}')
              elif inp == 'back':
                   break
              elif inp == 'exit':
                   exit()
              elif inp == 'help':
                   show(scanners_modules,description['scanners'])
              else:
                 print(f'\033[91m!\033[0m no command {inp}')
          except Exception as e:
              print(e)
          except KeyboardInterrupt:
              exit()