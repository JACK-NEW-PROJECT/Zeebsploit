#-*- coding: utf-8 -*-
from prettytable import PrettyTable

class Helper:


      def infoga_helper():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          infoga_modules = {'cms detector':'a tool for detecting cms on a web',
                            'port scanner':'Scan Open Port use Nmap',
                            'information header':'response header information',
                            'ip geolocation':'detect the location of an ip or host',
                            'email searcher':'searching email from web',
                            'traceroute':'to show the route the package has passed',
                            'robot.txt detector':'Scan Robot.txt from Web',
                            'whois lookup':'looking for registered users or\n recipients of Internet resource rights',
                            '---More---':'Coming Soon the following version'}
          for dat,ls in infoga_modules.items():
              pt.add_row([dat,ls])
          print(pt)

      def scanner_helper():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          scanner_modules = {'subdomain scanner':'Scan Subdomain for Web',
                             'sqli scanner':'Scan Sql Injection Vulnerability',
                             'xss scanner':'Scan XSS Injection Vulnerability',
                             'lfi scanner':'Local File Includes Scanner etc/passwd',
                             'admin login finder':'Scan Admin Login page',
                             'directory scanner':'scan directory on web use dirhunt',
                             'subdomain takeover':'scan type subdomain takeover',
                              '---More---':'Coming Soon the following version'}

          for dat,ls in scanner_modules.items():
              pt.add_row([dat,ls])
          print(pt)


      def exploit_modules():
          pt = PrettyTable()
          pt.field_names = ['Modules','Description']
          exploit_modules = {'wp content injection':'wordpress content injection version 4.7 or 4.7.1',
                             'wp revslider':'wordpress plugin revslider remote file upload',
                             'wp learndash':'wordpress leardash remote file upload',
                             'wp swhobiz':'wordpress plugin showbiz remote file upload',
                             'joomla com fabrik':'joomla component fabrik file upload',
                             'joomla manager get config':'joomla component manager auto get config',
                             'joomla jdownload':'joomla component jdownloads remote file upload',
                             'joomla ':'Joomla ads manager component auto shell upload',
                             'apache struts rce':'CVE: 2017-5638 - Apache Struts2 S2-045\n remote command execution',
                             'drupal8 rce':'drupal version 8 remote command execution',
                             'dvr cam leak credenyial':'TBK DVR4104 / DVR4216 \n- Credentials Leak (Get User and password',
                             'webdav file upload':'Nothing',
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
