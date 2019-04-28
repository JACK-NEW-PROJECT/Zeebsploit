#-*- coding: utf-8 -*-
import re,hashlib

class waf_detect(object):

      @classmethod    
      def cloudfront(cls,r):
          serv = 'CloudFront'
          if any(p in r.headers.keys() for p in ('Via','X-cache')) and any(serv.lower() in isi for isi in r.headers.values()):
             return True
          if r.headers.get('Server') == serv:
             return True
          return

      @classmethod
      def incapsula(cls,r):
          if 'X-Iinfo' in r.headers.keys() or r.headers.get('X-CDN') == 'Incapsula':
              return True
          return

      @classmethod
      def distil(cls,r):
          if r.headers.get('x-distil-cs'):
             return True
          return

      @classmethod
      def cloudflare(cls,r):
          if 'CF-RAY' in r.headers.keys() or r.headers.get('Server') == 'cloudflare':
              return True
          return

      @classmethod
      def edgecast(cls,r):
          if 'Server' in r.headers.keys() and 'ECD' in r.headers['Server']:
             return True

      @classmethod
      def maxcdn(cls,r):
          if 'Server' in r.headers.keys() and 'NetDNA-cache' in r.headers['Server']:
              return True
          return

      @classmethod
      def sucuri(cls,r):
          if any((r.headers.get('Server') == 'Sucuri/Cloudproxy','X-Sucuri-ID' in r.headers.keys(),'X-Sucuri-Cache' in r.headers.keys(),'Access Denied - Sucuri Website Firewall' in r.text)):
             return True
          return

      @classmethod
      def reblaze(cls,r):
          if r.headers.get('Server') == 'Reblaze Secure Web Gateway' or r.cookies.get('rbzid'):
             return True
          return

class footprinting_handler(object):

      @classmethod
      def server(cls,r):
          return r.headers.get('server')

      @classmethod
      def x_powered(cls,r):
          return r.headers.get('X-Powered-By')

      @classmethod
      def click_jacking(cls,r):
          if r.headers.get("X-Frame-Options") == None:
             return None
          else:
             return True

      @classmethod
      def xss_protect(cls,r):
         if r.headers.get("X-XSS-PROTECTION") == None:
            return None
         else:
            return True

      @classmethod
      def cors_wildcard(cls,r):
          if r.headers.get("Access-Control-Allow-Origin") == "*":
             return True
          else:
             return None

      @classmethod
      def sha_content(cls,r):
          page = hashlib.sha256(r.content).hexdigest()
          return page

      @classmethod
      def html_form(cls,sop):
          f = {}
          form = sop.select('form')
          for x in form:
              f['action'] = x.get('action')
              if f['action'] == '#':
                 continue
              f['class'] = x.get('class')
              f['id'] = x.get('id')
              f['method'] = x.get('method')
          return f

      @classmethod
      def email_search(cls,r):
          email = re.findall('[\\w\\-][\\w\\-\\.]+@[\\w\\-][\\w\\-\\.]+[a-zA-Z]{1,4}',r.text)        
          if len(email) == 0:
             return None
          else:
             return email

