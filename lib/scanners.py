#-*- coding: utf-8 -*-
from .scanner import scanner_modules as _
from .tmp.modules import log_,scanners_modules,description,show
import os

class scan(
    _.subdomain_scanner,
    _.xss_payload_vulnerability_scanner,
    _.sqli_scanner,
    _.lfi_scanner,
    _.subdomain_takeover_scanner,
    _.path_scanner):
      pass

logging = log_(__name__)      
class scanner_main(object):

      def url(self,x):
          self.x = x
          if self.x.startswith('https://') or self.x.startswith('http://'):return self.x
          else: 
             if self.x.startswith('www'): return f'https://{self.x}'
             else: return f'http://{self.x}'
                
      def _url(self,x):
          self.x = x
          if self.x.startswith('https://'): return self.x[8:]
          elif self.x.startswith('http://'): return self.x[7:]
          else: return self.x
                
      def plugin_scanner(self,target,abc):
          self.target = target
          self.abc = abc
          scan().main(self.target,self.abc)
          
                
      def main(self):
          scn = scan()
          mod = scanners_modules
          while True:
                try:
                    inp = input('zsf(\033[91mscanners\033[0m): ').lower()
                    if inp == mod[0]:
                       dom = self._url(input('domain: '))
                       domain = scn._start_scan(dom)
                       if len(domain) == 0:
                          logging.log(30,'no domain found!')
                       else:
                          logging.log(10,f'found: \033[92m{len(domain)}\033[0m')
                          for x in domain:
                              print(f'+ {x}')
                    elif inp == mod[1]:
                       logging.log(20,'example: http://domain.co.li/index.php?param=')
                       url = self.url(input('url: '))
                       if '=' not in url:
                          logging.log(20,'no parameter found')
                       else:
                          scn.start_scan(url)
                    elif inp == mod[2]:
                       logging.log(20,'example: http://domain.co.li/index.php?id=69')
                       url = self.url(input('url: '))     
                       if '=' not in url:
                          logging.log(20,'no parameter found') 
                       else:
                          x,y,z = scn.sqli(url)
                          if x > 0:
                             logging.log(50,'vulnerability')
                             logging.log(10,f'type: \033[93m{y}\033[0m')
                             logging.log(50,f'error: \033[91m{z}\033[0m')
                          else:
                             logging.log(20,'not vulnerability')
                    elif inp == mod[3]:
                         logging.log(20,'example: http://domain.co.li/index.php?param=')
                         url = self.url(input('url: '))
                         if '=' not in url:
                            logging.log(20,'no parameter found')
                         else:
                            scn.lfi(url)    
                    elif inp == mod[4]:
                         subdomain = self.url('url: ')
                         logging.log(10,'detecting subdomain takeover!')
                         ppk = scn.takeover(subdomain)
                         if ppk == '':
                            logging.warning(20,'not potentially a subdomain takeover')
                         else:
                            logging.log(50,'subdomain takeover detected!')
                            
                    elif inp == mod[5]:
                         self.plugin_scanner(
                            self.url(input('url: ')),
                            f'{os.getcwd()}/lib/wordlist/admin-panel.fuzz'
                         )
                    elif inp == mod[6]:
                         self.plugin_scanner(
                            self.url(input('url: ')),
                            f'{os.getcwd()}/lib/wordlist/wp-plugin.fuzz'
                         )
                    elif inp == mod[7]:
                         self.plugin_scanner(
                            self.url(input('url: ')),
                            f'{os.getcwd()}/lib/wordlist/wp-theme.fuzz'
                         )
                    elif inp == mod[8]:
                         self.plugin_scanner(
                            self.url(input('url: ')),
                            f'{os.getcwd()}/lib/wordlist/joomla-plugin.fuzz'
                         )
                    elif inp == mod[9]:
                         tgt = self.url(input('url: '))
                         os.system('dirhunt %s ' % tgt)
                    elif inp == 'exit':        
                         exit()
                    elif inp == 'help':
                         show(scanners_modules,description['scanners'])
                    elif inp == 'back':
                         break
                    else:
                       print(f'\033[91m!\033[0m no module name: {inp}')
                except Exception as e:
                    print(e)       
                except KeyboardInterrupt:
                    exit()                        