#-*- coding: utf-8 -*-
from .information_gathering import modules as _
from .tmp.modules import log_,information_gathering_modules,show,description
import whois

logging = log_()
class infoga(
    _.cms_detector,
    _.header_information,
    _.ip_geo_location,
    _.email_search,
    _.traceroute,
    _.robot_file_detector,
    _.reverse_ip_lookup):
      pass
      
class infoga_main(object):

      def url(self,x):
          self.x = x
          if self.x.startswith('https://') or self.x.startswith('http://'): return self.x
          else:
             if self.x.startswith('www'): return f'https://{self.x}'
             else: return f'http://{self.x}'                

      def main(self):
          mod = information_gathering_modules          
          info = infoga()
          while True:
                try:
                    inp = input('zsf(\033[91minformation-gathering\033[0m): ').lower()
                    if inp == mod[0]:
                       hasil = info.detect(input('host: '))
                       for a,b in hasil.items():
                           logging.log(10,f'{a}: {b}')
                    elif inp == mod[1]:
                       hasil = info.header(self.url(input('url: ')))
                       for a,b in hasil.items():
                           logging.log(10,f'{a}: {b}')       
                    elif inp == mod[2]:
                       hasil = info.geo(input('host/ip: '))
                       for a,b in hasil.items():
                           logging.log(10,f'{a}: {b}')
                    elif inp == mod[3]:
                       hasil = info.search(self.url(input('url: '))) 
                       if len(hasil) == 0:
                          logging.log(30,'email not found')
                       else:
                          for x in hasil:
                              logging.log(10,f'found: {x}')
                    elif inp == mod[4]:
                       hasil = info.trace(input('host: '))   
                       print(hasil)
                    elif inp == mod[5]:
                       hasil = info.robot(self.url(input('url: ')))   
                       if hasil.status_code == 200:
                          logging.log(50,f'found robot file')
                          print(hasil.text)
                       else:
                          logging.log(30,'robot file not found!')
                    elif inp == mod[6]:
                       hasil = info.reverse(input('domain: '))
                       if hasil['status'] == 'Success':
                          for domain,_ in hasil['domainArray']:
                              print(domain)
                       else:
                          logging.log(30,f'Failed: {hasil["message"]}') 
                    elif inp == mod[7]:
                       xxx = whois.whois(input('host: '))
                       print(xxx)
                    elif inp == 'exit':
                       exit()
                    elif inp == 'help':
                       show(information_gathering_modules,description['information gathering'])
                    elif inp == 'back':
                       break
                       print('\n')
                    else:
                       print(f'\033[91m!\033[0m no module: {inp}') 
                except Exception as e:
                    print(e)
                except KeyboardInterrupt:
                    exit()                   
