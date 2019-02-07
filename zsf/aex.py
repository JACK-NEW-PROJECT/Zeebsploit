#-*- coding: utf-8 -*-
from .lib.infoga import infoga as inf
from .lib.exploit import exploit as exp
from .lib.scan import scanner as scan
from .core.temp import *
from requests.exceptions import *
from .core.helper import Helper as help
from . import zeeb_mank as zm
import readline,socket,os
readline.set_pre_input_hook()

campret = '[!] Type "Exit" For Exit from This Tool\n[!] Type "help" for show modules\n'
mps = '[!] Type "Back" for Back To main menu'


class AEX:


      def __init__(aex, tgt):
          aex.tgt = tgt

      @property
      def cms_scan(aex):
          try:
             has = inf(aex.tgt).detect_cms
             for dat, ls in has.items():
                 print('')
                 print(dat+":"+str(ls))
          except ConnectionError:
             print(red('[x]')+'Internet Connection Error')

      @property
      def portscan(aex):
          if aex.tgt.startswith('https://'):
             inf(aex.tgt[8:]).scan_port
          elif aex.tgt.startswith('http://'):
              inf(aex.tgt[7:]).scan_port
          else:
              pass

      @property
      def header(aex):
          try:
             has = inf(aex.tgt).hider
             for dat,ls in has.items():
                 print(dat+":"+ls)
          except ConnectionError:
             print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
             print(yellow('[!]')+' try start with http:// or https')

      @property
      def ip_geoloc(aex):
          try:
              has = inf(aex.tgt).IP_geoloc
              for dat,ls in has.items():
                  print(dat+" : "+str(ls))
          except ConnectionError:
              print(red('[x]')+' Internet Connection Error')

      @property
      def whois(aex):
          try:
              has = inf(aex.tgt).whois
              for dat,ls in has.items():
                  print('')
                  print(dat+" : "+str(ls))
          except socket.gaierror:
              print(red('[x]')+' Internet Connection Error')

      @property
      def extract_email(aex):
          try:
              if not aex.tgt.startswith('http://'):
                 has = inf('http://'+aex.tgt).scan_email
              elif not aex.tgt.startswith('https://'):
                 has = inf('https://'+aex.tgt).scan_email
              else:
                 has = inf(aex.tgt).scan_email
              for dat,ls in has.items():
                  print(green('[+]')+'Found : '+ls)
          except ConnectionError:
              print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
              print(yellow('[!]')+' try start with http:// or https')

      @property
      def traceroute(aex):
           has = inf(aex.tgt).traceroute
           print(has)

      @property
      def robot(aex):
          try:
              print(inf(aex.tgt).robot)
          except ConnectionError:
              print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
              print(yellow('[!]')+' try start with http:// or https')

class scanners:

      def __init__(slf, tgt):
          slf.tgt = tgt

      @property
      def subdomain_scanner(slf):
          con = 0
          if slf.tgt.startswith('https://'):
             ft = scan(slf.tgt[8:]).subdo
          elif slf.tgt.startswith('http://'):
             ft = scan(slf.tgt[7:]).subdo
          else:
             ft = scan(slf.tgt).subdo
          for i in ft:
              con += 1
              print(green(str(con))+". "+i)

      @property
      def sqli_scan(slf):
          try:
             if '=' not in slf.tgt:
                print("")
                print(red("[!] No paramater Found in ")+slf.tgt)
                print("")
             else:
                ft = scan(slf.tgt).sql_scan
                for dat,ls in ft.items():
                    print(green('[*]')+' Vulnerability')
                    print(dat+" : "+red(ls))
          except ConnectionError:
              print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
              print(yellow('[!]')+' try start with http:// or https')

      @property
      def xss_scanner(slf):
          try:
             if '=' not in slf.tgt:
                print("")
                print(red("[!]")+" No paramater Found in "+slf.tgt)
                print("")
             else:
               ft = scan(slf.tgt).xss_scan
               print(ft)
          except ConnectionError:
               print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
               print(yellow('[!]')+' try start with http:// or https')

      @property
      def lfi_scan(slf):
          try:
             if '=' not in slf.tgt:
                print("")
                print(red("[!]")+" No paramater Found in "+slf.tgt)
                print("")
             else:
                scan(slf.tgt).lfi_scan
          except ConnectionError:
               print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
               print(yellow('[!]')+' try start with http:// or https')

      @property
      def admin_page_finder(slf):
          try:
             scan(slf.tgt).adfin
          except ConnectionError:
               print(red('[x]')+' Internet Connection Error')
          except MissingSchema:
               print(yellow('[!]')+' try start with http:// or https')

      @property
      def dirhunt(slf):
          os.system('dirhunt %s ' % (slf.tgt))


class exploitation:

     def __init__(self, tgt):
         self.tgt = tgt

     def webdav_file_upload(self, file, name):
         try:
             self.file = file
             self.name = name
             if '.' not in self.name:
                self.name = self.name+'.html'
             else:
                self.name = self.name
             exp(self.tgt).webdav_file_upload(self.file, self.name)
         except ConnectionError:
             print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
             print(yellow('[!]')+' try start with http:// or https')

     @property
     def dvr(self):
         try:
            exp(self.tgt).DVRs_credential_exposed
         except Exception as e:
            print(red('[-]')+'Not Vulnerability')
            print('Error :',e)
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')


     def wp_rest_api(self, file):
         try:
            self.file = file
            exp(self.tgt).wordpress_content_injection(self.file)
         except ValueError:
            print(yellow('[!]')+'Post ID must number !')
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')

     @property
     def revslider(self):
         try:
            exp(self.tgt).WP_revslider_file_upload
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')

     @property
     def showbiz(self):
         try:
           exp(self.tgt).WP_showbiz_file_upload
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')

     @property
     def learndash(self):
         try:
            exp(self.tgt).WP_learn_dash_file_upload
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')


     def fabrik(self):
         try:
            exp(self.tgt).com_fabrik()
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')

     @property
     def struts(self):
         try:
             ab = exp(self.tgt).struts_rce('whoami')
             if len(ab) < 20:
                print(green('[!]')+ ' Vulnerability ')
                print('Type "exit" for stop')
                while True:
                      cmn = str(input('command > '))
                      if 'exit' in cmn: break
                      else:exp(self.tgt).struts_rce(cmn)
             else:
                print(red('[-]')+'  Not Vulnerability')
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')

     @property
     def joomla_ads_manager(self):
         try:
            exp(self.tgt).joomla_ads_manager
         except ConnectionError:
            print(red('[x]')+' Internet Connection Error')
         except MissingSchema:
            print(yellow('[!]')+' try start with http:// or https')






def exploiter():
    print('\n')
    print(campret)
    print(mps)
    print('\n')
    while True:
          try:
              aex = input('[zsf/\033[91mexploit\033[0m/]> ').lower()
              if 'webdav_file_upload' in aex:
                 tgt = input('Url : ')
                 file = input('Path your File : ')
                 name = input('upload file with name : ')
                 print('\n')
                 exploitation(tgt).webdav_file_upload(file,name)
                 print('\n')
              elif 'dvr_cam_leak_credential' in aex:
                 print('\n')
                 exploitation(input('Host : ')).dvr
                 print('\n')
              elif 'wp_content_injection' in aex:
                 tgt = input('Url : ')
                 file = input("path your file : ")
                 print('\n')
                 exploitation(tgt).wp_rest_api(file)
                 print('\n')
              elif 'wp_revslider' in aex:
                 print('\n')
                 exploitation(input('Url : ')).revslider
                 print('\n')
              elif 'wp_showbiz' in aex:
                 print("\n")
                 exploitation(input('Url : ')).showbiz
                 print('\n')
              elif 'wp_learndash' in aex:
                 print('\n')
                 exploitation(input('Url : ')).learndash
                 print('\n')
              elif 'joomla_com_fabrik' in aex:
                 print('\n')
                 exploitation(input('Url : ')).fabrik()
                 print('\n')
              elif 'apache_struts2_rce' in aex:
                 print('\n')
                 exploitation(input('Url : ')).struts
                 print('\n')
              elif 'joomla_ads_manager' in aex:
                 print('\n')
                 exploitation(input('Url : ')).joomla_ads_manager
                 print("\n")
              elif 'exit' in aex:
                 exit('Exit !')
              elif 'back' in aex:
                 zm.bingung()
              elif 'help' in aex:
                 print('\n')
                 print('[!] type one of the module names to use')
                 help.exploit_modules()
                 print('\n')
              else:
                 print('')
                 print('No command '+aex)
                 print("") 
          except EOFError:
              break
          except KeyboardInterrupt:
              break



def web_scan():
    print('\n')
    print(campret)
    print(mps)
    print('\n')
    while True:
          try:
             jx = input('[zsf/\033[91mscanners\033[0m/]> ').lower()
             if 'subdomain_scanners' in jx:
                 print('\n')
                 scanners(input('HOST : ')).subdomain_scanner
                 print('\n')
             elif 'sqli_scanner' in jx:
                 print('\n')
                 scanners(input('URL : ')).sqli_scan
                 print('\n')
             elif 'xss_scanner' in jx:
                 print('\n')
                 scanners(input('URL : ')).xss_scanner
                 print('\n')
             elif 'lfi_scanner' in jx:
                 print('\n')
                 scanners(input("URL : ")).lfi_scan
                 print('\n')
             elif 'admin_finder' in jx:
                 print('\n')
                 scanners(input('URL : ')).admin_page_finder
                 print('\n')
             elif 'directory_scanner' in jx:
                 scanners(input('Url : ')).dirhunt
             elif 'exit' in jx:
                 exit('Exit !')
             elif 'back' in jx:
                 zm.bingung()
             elif 'help' in jx:
                 print('\n')
                 print('[!] type one of the module names to use')
                 help.scanner_helper()
                 print('\n')
             else:
                 print('')
                 print('No Command '+jx)
                 print('')
          except KeyboardInterrupt:
             break
          except EOFError:
             break



def infoga():
    print('\n')
    print(campret)
    print(mps)
    print('\n')
    while True:
          try:
              c = input('[zsf/\033[91mInfoga\033[0m/]> ').lower()
              if 'detect_cms' in c:
                  AEX(input('URL : ')).cms_scan
                  print('\n')
              elif 'port_scanner' in c:
                  AEX(input('HOST : ')).portscan
              elif 'header_check' in c:
                  print('\n')
                  AEX(input('URL : ')).header
                  print('\n')
              elif 'ip_geolocation' in c:
                  print('\n')
                  AEX(input('URL : ')).ip_geoloc
                  print('\n')
              elif 'whois' in c:
                  print('\n')
                  AEX(input('URL : ')).whois
                  print('\n')
              elif 'email_extractor' in c:
                  print('\n')
                  AEX(input('URL : ')).extract_email
                  print('\n')
              elif 'traceroute' in c:
                  AEX(input('URL : ')).traceroute
              elif 'robot.txt' in c:
                  print('\n')
                  AEX(input('URL : ')).robot
                  print('\n')
              elif 'exit' in c:
                  exit('Exit ! ')
              elif 'back' in c:
                  zm.bingung()
              elif 'help' in c:
                  print('\n')
                  print('[!] type one of the module names to use')
                  help.infoga_helper()
                  print('\n')
              else:
                  print('')
                  print('No Command '+c)
                  print('')
          except KeyboardInterrupt:
              break
          except EOFError:
              break
