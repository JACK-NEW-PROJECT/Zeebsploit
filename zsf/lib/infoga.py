#-*- coding: utf-8 -*-

import requests, os, marshal, re, socket
from fake_useragent import UserAgent
import whois

class infoga:

      agen = {"User-Agent":UserAgent().random}
      _WASEK ={"A": b'\xdaF1482f3f1d83cdacf018a60f7b44be2cae9244161a54c3909561d19160f0baf6de8575a'}
      url = "https://whatcms.org/APIEndpoint/Detect?key=","http://ip-api.com/json/%s","https://api.hackertarget.com/mtr/?q="

      def __init__(self, Host):
          self.Host = Host


      @property
      def detect_cms(self):
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
               HS = ses.get(infoga.url[0]+marshal.loads(infoga._WASEK['A'])+"&url="+self.Host).json()["result"]
          return HS

      @property
      def scan_port(self):
          os.system('nmap --open %s' % self.Host)

      @property
      def hider(self):
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
               hid = ses.get(self.Host)
          return hid.headers,hid.text

      @property
      def IP_geoloc(self):
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
               geo = ses.get(infoga.url[1] % (self.Host)).json()
          return geo

      @property
      def whois(self):
          WHOIS = whois.whois(self.Host)
          return WHOIS

      @property
      def scan_email(self):
          email = {}
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
               content = ses.get(self.Host).text
               MAIL = re.findall('[\\w\\-][\\w\\-\\.]+@[\\w\\-][\\w\\-\\.]+[a-zA-Z]{1,4}', content)
               email.update(mailing=str(MAIL))
          return email

      @property
      def traceroute(self):
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
          return  ses.get(infoga.url[2]+self.Host).text

      @property
      def robot(self):
          with requests.Session() as ses:
               ses.headers.update(infoga.agen)
               rbt = ses.get(self.Host+"/robots.txt")
               if rbt.status_code == 200:
                  print("(Robot.txt) :  \033[92mFOUND\033[0m")
                  print(rbt.content)
               else:
                  print('(Robot.txt) : \033[91m Not FOUND\033[0m')

