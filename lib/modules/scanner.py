#-*- coding: utf-8 -*-
import requests,re,os,sys,time,urllib3
from bs4 import BeautifulSoup as bs
from .sqlerror import sql_errors
from .color import R,G,B,Y,W
requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class subdomain(object):

      url = 'https://dnsdumpster.com'

      def subdomain_scanner(self,domain):
          self.domain = domain
          __content = requests.get(subdomain.url).text
          __process = bs(__content,'html.parser').find_all('input')
          token = re.findall('value="(.*?)"',str(__process))[0]
          resp = requests.post(
                              subdomain.url,
                              headers={'Referer':subdomain.url},
                              cookies={'csrftoken':token},
                              data = {'csrfmiddlewaretoken': token, 'targetip': self.domain}
                 )
          num = 0
          ok = re.findall('http://(.*?)"',str(resp.text))
          for i in ok:
              num += 1
              print(f'{R}{num}{W}. {i}')

               
class sqli_scan(object):


      def SQLi_scanner(self,url):
          _vuln = 0
          vuln = {}
          self.url = url
          resp = requests.get(self.url+"'").text
          for a,b in sql_errors.items():
              if re.search(b,resp):
                 _vuln += 1
                 vuln.update(Type=a)
                 vuln.update(Error=b)
              else:
                 pass
                 
          if _vuln > 0:
             print(f"{G}[!]{W} Vulnerability")
             for x_,x__ in vuln.items():
                 print(f"{x_} : {x__}")
          else:
             print(f'{R}[x]{W} Not Vulnerability')


class xss_scan(object):


      def xss_scanner(self,target):         
          self.target = target
          with open(f'{os.getcwd()}/lib/wordlist/xss.txt') as payload:
               for pilod in payload:
                   pld = pilod.rstrip()
                   resp = requests.get(f"{self.target}{pld}").text
                   if pld in resp:
                      print(f"{G}[*]{W} Potential Vulnerability : {self.target}{pld}")
                      print("\n")
                   else:
                      print(f"{R}[-]{W} Not Vulnerability : {self.target}{pld}")
                      



class lfi_scan(object):

      def LFI_scanner(self,target):
          self.target = target
          path = '../'
          for scan in range(1,17):
              pth = path*scan
              res = requests.get(f'{self.target}{pth}etc/passwd').text
              if "root:x:0:0" in res:
                  print(f'{G}[*]{W} Vulnerability : {self.target}{pth}etc/passwd')
              else:
                  print(f'{R}[x]{W} Not Vulnerability : {self.target}{pth}etc/pasdwd')
                  
class adfin:

      def admin_page_finder(self,target):
          self.target = target
          with open(f"{os.getcwd()}/lib/wordlist/adfin.txt") as panel:
                for login in panel:
                     page = login.rstrip()
                     resp = requests.get(f"{self.target}/{page}")
                     if resp.status_code == 200:
                        print(f"{G}[+]{W} Found : {self.target}/{page}")
                     else:
                        print(f"{R}[-]{W} Not Found : {self.target}/{page}")

              
class takeover:

      @property
      def req(self):
          return {'Cargo': '<title>404 &mdash; File not found</title>', 'Tave': '<h1>Error 404: Page Not Found</h1>', 'Shopify': 'Sorry\\, this shop is currently unavailable\\.', 'Webflow': '<p class=\\"description\\">The page you are looking for doesn\\\'t exist or has been moved.</p>', 'Heroku': 'no-such-app.html|<title>no such app</title>|herokucdn.com/error-pages/no-such-app.html', 'Wordpress': 'Do you want to register', 'Tictail': 'to target URL: <a href=\\"https://tictail.com|Start selling on Tictail.', 'Tumbler': "Whatever you were looking for doesn\\'t currently exist at this address.", 'Thinkific': 'You may have mistyped the address or the page may have moved.', 'Fastly': 'Fastly error\\: unknown domain\\:', 'Acquia': 'The site you are looking for could not be found.|If you are an Acquia Cloud customer and expect to see your site at this address', 'Pantheon': 'The gods are wise, but do not know of the site which you seek.', 'Intercom': "This page is reserved for artistic dogs\\.|Uh oh\\. That page doesn\\'t exist</h1>", 'AWS/S3': 'The specified bucket does not exit', 'GetResponse': 'With GetResponse Landing Pages, lead generation has never been easier', 'Brightcove': '<p class=\\"bc-gallery-error-code\\">Error Code: 404</p>', 'Smartling': 'Domain is not configured', 'TeamWork': "Oops - We didn\\'t find your site.", 'ZenDesk': 'Help Center Closed', 'Jetbrains': 'is not a registered InCloud YouTrack.', 'Ghost': 'The thing you were looking for is no longer here\\, or never was', 'Github': "There isn\\'t a Github Pages site here\\.", 'Mashery': 'Unrecognized domain <strong>', 'Desk': "Sorry\\, We Couldn\\'t Find That Page", 'CloudFront': 'ERROR\\: The request could not be satisfied', 'Surge': 'project not found', 'S3Bucket': 'The specified bucket does not exist', 'Kajabi': "<h1>The page you were looking for doesn\\'t exist.</h1>", 'ActiveCampaign': 'alt=\\"LIGHTTPD - fly light.\\"', 'Helpscout': 'No settings were found for this company:', 'Aftership': 'Oops.</h2><p class=\\"text-muted text-tight\\">The page you\\\'re looking for doesn\\\'t exist.', 'Campaignmonitor': 'Double check the URL or <a href=\\"mailto:help@createsend.com', 'Wishpond': '<h1>https://www.wishpond.com/404?campaign=true', 'Bigcartel': '<h1>Oops! We couldn&#8217;t find that page.</h1>', 'Unbounce': 'The requested URL / was not found on this server|The requested URL was not found on this server', 'BitBucket': 'Repository not found', 'Aha': 'There is no portal here \\.\\.\\. sending you back to Aha!', 'Uservoice': 'This UserVoice subdomain is currently available!', 'StatuPage': 'You are being <a href=\\"https://www.statuspage.io\\">redirected', 'Simplebooklet': 'We can\\\'t find this <a href=\\"https://simplebooklet.com', 'Proposify': 'If you need immediate assistance, please contact <a href=\\"mailto:support@proposify.biz', 'Vend': "Looks like you\\'ve traveled too far into cyberspace.", 'Helpjuice': "We could not find what you\\'re looking for.", 'Tilda': 'Domain has been assigned', 'Surveygizmo': 'data-html-name', 'FeedPress': 'The feed has not been found\\.', 'Pingdom': 'pingdom'}
          
          
      def subdomain_takeover(self,target):
          self.target = target
          _vuln = ""
          resp = requests.get(f'{self.target}')
          for a,b in self.req.items():
              if re.search(b,resp.text,re.I) and re.search('[300-499]',str(resp.status_code),re.I):
                 _vuln += a
                 break
              else:
                 pass
          if _vuln != "":
             print(f'{G}[+]{W} Vulnerability Takeover Found : {_vuln}')
          else:
             print(f"{R}[x]{W} Not Vulnerability Takeover")


              
