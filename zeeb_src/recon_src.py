#-*- coding: utf-8 -*-
from .lib import (
    waf_detect,
    infoga
)

from .utils import (
    infoga_modules,
    show,
    log,
    description,
    proto,
    no_proto,
    waf_debug,
    json_respon
)
import requests,readline,marshal,whois
from bs4 import BeautifulSoup as bs

log = log(__name__)
mod = infoga_modules
uag = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
def main():
    while True:
          try:
              inp = input('zsf(\033[91mfootprinting\033[0m): ').lower()
              if inp == mod[0]:
                 url = input('host: ')
                 auth = b'\xdaF1482f3f1d83cdacf018a60f7b44be2cae9244161a54c3909561d19160f0baf6de8575a'
                 r = requests.get(
                    f'https://whatcms.org/APIEndpoint/Detect?key={marshal.loads(auth)}&url={url}'
                 )
                 json_respon(r.json()['result'])
              elif inp == mod[1]:
                   url = proto(input('url: '))
                   r = requests.get(
                    url,
                    headers = uag,
                    timeout = 7,
                    verify=False
                   )
                   log.log(50,f'Server: {infoga.server(r)}')
                   log.log(50,f'X-Powered-By: {infoga.x_powered(r)}')
                   if infoga.click_jacking(r) == None:
                      log.log(20,'target might be vulnerability clickjacking')
                   if infoga.xss_protect(r) == None:
                      log.log(20,f'no xss protection')
                   if infoga.cors_wildcard(r) == True:
                      log.log(50,'cors wildcard detected')
                   log.log(50,f'sha256 content: {infoga.sha_content(r)}')
                   print('show all result')
                   json_respon(r.headers)
              elif inp == mod[2]:
                   tgt = no_proto(input('host/Ip: '))
                   r = requests.get(f'http://ip-api.com/json/{tgt}')
                   json_respon(r.json())
              elif inp == mod[3]:
                   url = proto(input('url: '))
                   r = requests.get(
                    url,
                    verify=False,
                    headers = uag
                   )
                   if infoga.email_search(r) == None:
                      log.log(30,'no email found')
                   else:
                      for i in infoga.email_search(r):
                          log.log(50,f'found: {i}')
              elif inp == mod[4]:
                   tgt = no_proto(input('host/Ip: '))
                   r = requests.get('https://api.hackertarget.com/mtr/?q={tgt}')
                   print(r.text)
              elif inp == mod[5]:
                   url = proto(input('url: '))
                   r = requests.get(
                    url,
                    headers = uag,
                    verify=False
                   )
                   if r.status_code == 200:
                      log.log(50,'robot.txt found')
                      print(r.text)
                   else:
                      log.log(30,'robot.txt not found')
              elif inp == mod[6]:
                   dom = no_proto(input('domain: '))
                   r = requests.post(
                    'https://domains.yougetsignal.com/domains.php',
                    data = {
                        'remoteAddress':dom,
                        'key':''
                    }
                   )
                   if r.json()['status'] == 'Success':
                      for domain,_ in r.json()['domainArray']:
                          log.log(10,f'{domain}')
                   else:
                      log.log(30,f'{r.json["status"]}')
              elif inp == mod[7]:
                   xxx = whois.whois(input('host: '))
                   print(xxx)
              elif inp == mod[8]:
                   url = proto(input('url: '))
                   r = requests.get(
                    url,
                    headers = uag,
                    verify=False
                   )
                   x = bs(r.text,'lxml')
                   p = infoga.html_form(x)
                   if len(p.values()) == 0:
                      log.log(30,'no html form found')
                   else:
                      json_respon(p)
              elif inp == mod[9]:
                   url = proto(input('url: '))
                   r = requests.get(
                    url,
                    headers = uag,
                    allow_redirects=True,
                    timeout=7
                   )
                   x = waf_debug(waf_detect,r)
                   x.main()
              elif inp == 'back':
                   break
              elif inp == 'exit':
                   exit()
              elif inp == 'help':
                   show(infoga_modules,description['information gathering'])
              else:
                 print(f'\033[91m!\033[0m no command {inp}')
          except Exception as e:
              print(e)         
          except KeyboardInterrupt:
              exit()               