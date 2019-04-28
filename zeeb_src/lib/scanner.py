#-*- coding: utf-8 -*-
import asyncio,aiohttp,requests,os,urllib3,aiofiles,re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class subdomain_enumeration(object):

      def __init__(self,domain):
          self.domain = domain
          self.url = 'https://dnsdumpster.com'
          self.uag = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
          self.dns_dumpster = []
          
      def DNSdumpster(self):
          get_token = requests.get(self.url,headers={'User-Agent':self.uag})
          token = re.findall("value=\'(.*?)\'",get_token.text)[0]
          post = requests.post(
            self.url,
            data={
                'csrfmiddlewaretoken':token,
                'domain':self.domain
            },
            cookies={
                'csrftoken':token
            },
            headers={
                'User-Agent':self.uag,
                'Referer':self.url
            }            
          )
          subdo = re.findall('http://(.+?)"',post.text)
          for x in subdo:
              self.dns_dumpster.append(x)
              
      @property        
      def raw_result(self):        
          return self.dns_dumpster

class fuzzer(object):

      def __init__(self,target,path):
          self.target = target
          self.path = path
          self.user_agent = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
          self.__xss_result = []
          self.__fuzz = []
          
      @property
      def raw_xss_result(self):
          return self.__xss_result
          
      @property    
      def raw_fuzz(self):
          return self.__fuzz
          
      async def request(self,payload,session,isi):
        try:
             async with session.get(f'{self.target}/{payload}',ssl=False) as resp:
               content = await resp.text()
               status = resp.status
               if 'xss' in isi:
                  if payload in content:
                     self.__xss_result.append(resp.url)
                     print(f'\033[92m[+]\033[0m {resp.url} : \033[92m{resp.status}\033[0m')
                  else:
                     print(f'\033[91m[-]\033[0m {resp.url} : \033[93m{resp.status}\033[0m')
               else:
                  if status == 200:
                     print(f'\033[92m[+]\033[0m {resp.url} : \033[92m{resp.status}\033[0m')
                     self.__fuzz.append(resp.url)
                  else:
                     print(f'\033[91m[-]\033[0m {resp.url} : \033[93m{resp.status}\033[0m') 
               resp.closed
        except Exception:
            pass
            
      async def _fetch(self,iii):      
        connector = aiohttp.TCPConnector(limit=None)
        async with aiohttp.ClientSession(connector=connector) as sesi:
          with open(self.path,'r') as open_files:
            tas = [self.request(pilod.rstrip(),sesi,iii)for pilod in open_files.readlines()]
            await asyncio.gather(*tas)
            
      @classmethod      
      def sqli_scan(cls,url,query_error):
          vuln = 0
          types = ''
          error = ''
          r = requests.get(
            f"{url}'",
            headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'},
            verify=False            
          )
          for a,b in query_error.items():
              if re.search(b,r.text):
                 vuln += 1
                 types += a
                 error += b
                 break
              else:
                 pass
          return vuln,types,error
          
      @classmethod    
      def subdomain_takeover(cls,url,query_error):
          vuln = ''
          r = requests.get(
            url,
            headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'},
            verify=False            
          )
          for a,b in query_error.items():
              if re.search(b,r.text,re.I) and re.search('[300-499]',str(r.status_code)):
                 vuln += a
                 break
              else:
                 pass
          return vuln 
          
      @classmethod    
      def lfi_scanner(cls,url):
          vuln = ''
          params = '../'
          for x in range(1,20):
              p = params*x
              r = requests.get(
                f'{url}{p}/etc/passwd',
                headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'},
                verify=False                
              )
              if 'root:x:0:0' in r.text:
                 print(f'\033[92m[+]\033[0m {r.url} : \033[92mvulnerability\033[0m')
              else:
                 print(f'\033[93m[-]\033[0m {r.url} : \033[93not mvulnerability\033[0m')      