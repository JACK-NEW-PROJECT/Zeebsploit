#-*- coding: utf-8 -*-
import requests,hashlib,re,marshal,whois

class cms_detector(object):

      def detect(self,target):
          self.target = target
          auth = b'\xdaF1482f3f1d83cdacf018a60f7b44be2cae9244161a54c3909561d19160f0baf6de8575a'
          r = requests.get(
            f'https://whatcms.org/APIEndpoint/Detect?key={marshal.loads(auth)}&url={self.target}'
          )
          return r.json()['result']      

class header_information(object):

      def header(self,target):
          self.target = target
          r = requests.get(
            self.target
          )         
          r.headers.update(sha256_page=hashlib.sha256(r.content).hexdigest())
          return r.headers

class ip_geo_location(object):

      def geo(self,target):
          self.target = target
          r = requests.get(
            f'http://ip-api.com/json/{self.target}'
          )          
          return r.json()

class email_search(object):

      def search(self,target):
          self.target = target
          r = requests.get(self.target)
          x = re.findall(
            r'[\\w\\-][\\w\\-\\.]+@[\\w\\-][\\w\\-\\.]+[a-zA-Z]{1,4}',
            r.text
          )
          return x

class traceroute(object):

      def trace(self,target):
           self.target = target
           r = requests.get(
            f"https://api.hackertarget.com/mtr/?q={self.target}"
           )
           return r.text

class robot_file_detector(object):

      def robot(self,target):
          self.target = target
          r = requests.get(
            f'{self.target}/robots.txt'
          )
          return r
          
class reverse_ip_lookup(object):

      def reverse(self,target):
          self.target = target
          r = requests.post(
            "https://domains.yougetsignal.com/domains.php",
            data = {
                'remoteAddress':self.target,
                'key':''
            }
          )
          return r.json()



          