#-*- coding: utf-8 -*-
from prettytable import PrettyTable

class Helper:


      def infoga_helper():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          infoga_modules = {'Detect_cms':'a tool for detecting cms on a web',
                            'Port_Scanner':'Scan Open Port use Nmap',
                            'ip_Geolocation':'Scan Location Host or Ip',
                            'Whois':'request and response protocol for web data',
                            'Email_Extractor':'EXtract Email from web',
                            'Traceroute':'to show the route the package has passed',
                            'Robot.Txt':'Scan Robot.txt from Web',
                            'header_check':'Response Header Checker',
                            '---More---':'Coming Soon the following version'}
          for dat,ls in infoga_modules.items():
              pt.add_row([dat,ls])
          print(pt)

      def scanner_helper():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          scanner_modules = {'Subdomain_Scanner':'Scan Subdomain for Web',
                             'SQLi_Scanner':'Scan Sql Injection Vulnerability',
                             'XSS_Scanner':'Scan XSS Injection Vulnerability',
                             'LFI_Scanner':'Local File Includes Scanner etc/passwd',
                             'Admin_finder':'Scan Admin Login page',
                             'directory_scanner':'scan directory on web use dirhunt',
                              '---More---':'Coming Soon the following version'}

          for dat,ls in scanner_modules.items():
              pt.add_row([dat,ls])
          print(pt)


      def exploit_modules():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          exploit_modules = {'Webdav_File_Upload':'--None--',
                             'Dvr_cam_leak_credential':'TBK DVR4104 / DVR4216 - Credentials Leak (Get User and password',
                             'Wp_Content_Injection':'WP Content Injection File upload version:4.7 and 4.7.1',
                             'Wp_Revslider':'Wordpress Revslider Plugin Shell Auto Upload',
                             'Wp_showbiz':'Wordpress Showbiz Pro shell Auto Upload',
                             'Wp_Learndash':'Wordpress Learndash shell Auto Upload',
                             'Joomla_com_fabrik':'Joomla Component_Fabrik Auto Shell Upload',
                             'Joomla_ads_manager':'Joomla ads manager component auto shell upload',
                             'apache_struts2_rce':'CVE: 2017-5638 - Apache Struts2 S2-045',
                             '---More---':'Coming Soon the following version'}

          for dat,ls in exploit_modules.items():
              pt.add_row([dat,ls])
          print(pt)

      def utama():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          utama = {'Exploit':'Exploitation Modules',
                   'Scanners':'Scanners Modules',
                   'infoga':'information Gathering Modules'}

          for dat,la in utama.items():
              pt.add_row([dat,la])
          print(pt)

