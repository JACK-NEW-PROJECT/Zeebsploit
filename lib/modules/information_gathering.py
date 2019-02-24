#-*- coding: utf-8 -*-
import requests,re,marshal,hashlib,whois
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from .color import R,G,B,Y,W

hider = {"User-Agent":UserAgent().random}

class cms_detector:

      @property
      def req(self):
          return b'\xdaF1482f3f1d83cdacf018a60f7b44be2cae9244161a54c3909561d19160f0baf6de8575a'

      def cms_detector(self,target):
          self.target = target
          with requests.Session() as ses:
               res = ses.get(f"https://whatcms.org/APIEndpoint/Detect?key={marshal.loads(self.req)}&url={self.target}").json()['result']
               for a,b in res.items():
                   print(f"{B}[+]{W} {a} : {b}")

class header_information(object):

      def header(self,target):
          self.target = target
          res = requests.get(
                self.target,
                headers=hider
                )
          print(f"{G}[#]{W} Hash sha256  Page : {hashlib.sha256(res.text.encode('utf-8')).hexdigest()}")
          for a,b in res.headers.items():
              print(f"\t{a}:{b}")

class geoloc(object):

      def geo_location(self,target):
          self.target = target
          resp = requests.get(f"http://ip-api.com/json/{self.target}",headers=hider).json()
          for a,b in resp.items():
              print(f"{B}[+]{W} {a}: {b}")
               
          
class email_search(object):

      @property
      def pattern(self):
          return '[\\w\\-][\\w\\-\\.]+@[\\w\\-][\\w\\-\\.]+[a-zA-Z]{1,4}'

      def Email_search(self,target):
          self.target = target
          resp = requests.get(self.target).text.encode('utf-8')
          hs = re.findall(self.pattern,str(resp))
          if len(hs) == 1:
             print(f'{G}[+]{W} Found : {hs}')
          elif len(hs) > 1:
             for x in hs:
                 print(f'[+]Found : {x}')
          elif len(hs) == 0:
             print(f'{R}[-]{W} No Email Found')
          else:
             print(f'{R}[-]{W} No Email Found')


class trace(object):

      @property
      def req(self):
          return "https://api.hackertarget.com/mtr/?q={}"
          
      def traceroute(self,target):
          self.target = target
          resp = requests.get(self.req.format(self.target)).text
          print(resp)


class robot(object):

      def Robot(self,target):
          self.target = target
          resp = requests.get(f"{self.target}/robots.txt")
          if resp.status_code == 200:
             print('{G}[*]{W} robot.txt Found')
             print(resp.text)
          else:
             print('[-]robot.txt not found')



