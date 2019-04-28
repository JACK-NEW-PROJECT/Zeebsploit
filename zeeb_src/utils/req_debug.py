#-*- coding: utf-8 -*-
from .logger import logger

log = logger(__name__)

def proto(url):
    if url.startswith('http://') or url.startswith('https://'):
       return url
    else:
       if url.startswith('www'):
          return f'https://{url}'
       else:
          return f'http://{url}'

def no_proto(url):
    if url.startswith('https://'):
       return url[8:]
    elif url.startswith('http://'):
       return url[7:]
    else:
       return url

def upload_debug(r1,r2):
    log.log(10,f'upload in : {r1.url}')
    log.log(10,f'response code: {r1.status_code}')
    log.log(10,f'checking file: {r2.url} status: {r2.status_code}')
    if r2.status_code == 200:
       log.log(50,f'vulnerability')
       log.log(50,f'uploaded to: {r2.url}')
    else:
       log.log(30,f'not vulnerability')

def json_respon(json):
    for x,y in json.items():
        log.log(10,f'{x}: {y}')



class waf_debug(object):

      def __init__(self,func,resp):
          self.func = {
            'CloudFront':func.cloudfront,
            'CloudFlare':func.cloudflare,
            'Incapsula':func.incapsula,
            'MaxCDN':func.maxcdn,
            'Edgecast':func.edgecast,
            'Distil Networks':func.distil,
            'Sucuri':func.sucuri,
            'Reblaze':func.reblaze
          }
          self.resp = resp
          self.val = False
          
      def _get_detect(self,x):
          log.log(50,f'waf detected: {x}')
          self.val = True
          
      def fetch(self):
          for a,b in self.func.items():
              res = b(self.resp)
              if res:
                 self._get_detect(a)
                 
      def main(self):  
          self.fetch()
          if not self.val:
             log.log(20,f'did not detect waf')









