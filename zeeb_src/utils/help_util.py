#-*- coding: utf-8- -*-
m = '\033[91m'
p = '\33[0m'
h = '\033[92m'
b = '\033[94m'
k = '\033[93m'

exploit_modules = {
    'wordpress':[
        'wp content injection',
        'wp revslider',
        'wp learndash',
        'wp showbiz',
        'wp audio control',
        'wp geoplace3',
        'wp pugeot'
    ],
    'joomla':[
        'com fabrik',
        'com ads manager',
        'joomanager get config',
        'com jdownload'
    ],
    'other':[
        'webdav',
        'elfinder',
        'apache struts 2',
        'drupal version 8',
        'drupal version 7',
        'dvr cam'
    ]
}

scanners_modules = [
    'subdomain scanner',
    'xss scanner',
    'sqli scanner',
    'lfi scanner',
    'subdomain takeover',
    'admin finder',
    'wp plugin',
    'wp theme',
    'joomla component',
    'dirhunt',
    'sensitive file'
]

information_gathering_modules = [
    'cms detector',
    'information headers',
    'ip geo location',
    'email search',
    'traceroute',
    'robot.txt',
    'reverse ip',
    'whois',
    'html form',
    'waf detect'
]

description = {
    'exploit':[
        'wordpress content injection version 4.7 and 4.7.1',
        'wordpress plugin revslider arbitrary file upload',
        'wordpress learndash arbitrary file upload',
        'wordpress plugin showbiz atbitrary file upload',
        'wordpress audio control arbitrary file upload',
        'wordpress geoplace3 arbitrary file upload',
        'wordpress pugeot music arbitrary file upload',
        'joomla component fabrik arbitrary file upload',
        'joomla component manager mistake configuration auto get config',
        'joomla component jdownload arbitrary file upload',
        'joomla component ads manager arbitrary file upload',
        'webdav arbitrary file upload',
        'elfinder remote file upload',
        'apache struts 2 remote command execution',
        'drupalgeddon version 7 remote command execution ',
        'drupalgeddon version 7 remote command execution ',
        'TBK DVR4104 / DVR4216 - Credentials Leak get user and password',
        

    ],
    'scanners':[
        'subdomain enumeration use DNSdumpster',
        'cross site scripting payload scanner',
        'sqli injection scanner',
        'local file include /etc/passwd scanner',
        'subdomain misconfiguration takeover detector',
        'admin panel login finder',
        'wordpress plugin directory scanner',
        'wordpress theme directory scanner',
        'joomla component directory scanner',
        'directory hunter'
        'sensitive file scanner'
    ],
    'information gathering':[
        'content management system detector',
        'get information headers',
        'host/ip geo location lookup',
        'email extractor',
        'to show the route the package has passed',
        'robot.txt file detector',
        'reverse ip lookup',
        'looking for registered users or recipients of Internet resource rights',
        'html from discovered detector',
        'web application firewall detector',
    ]
}

art = f'''
        /`\/`\ {h}  Aink Zeeber Mank{p} !!
       _|`==`|_                         |version|:{b} 1.1{p}
      (._`""`_.)     {m}  ___             _  {p}
       /{m}o{p} \/{m}o{p} \ {m}        _/ _  _ |_  _ |_) |  _  o _|_{p}
   .---\__/\__/---.  {m}  /__(/_(/_|_)_> |   | (_) |  |_{p}
 .-'\     \/     /`-.    
  '-.\   {m}407{p}    /.-'       {k}[by]{p}: 407 Authentic Exploit      
     )\        /(          {k}[codename]{p}: JaxBCD
       \ ,  , /            exploits({h}{len(description["exploit"])}{p})          
       _>|\/|<_            recon({h}{len(description["information gathering"])}{p})
     -==='  '===-          scanners({h}{len(description["scanners"])}{p})
     '''

def show(x,y):
    print('\n')
    mak = '{0:<%s}  {1}' % max([len(i)for i in x ])
    print(mak.format('modules','description'))
    print(mak.format('-------','-----------'))
    for i in range(len(x)):
        print(mak.format(x[i],y[i]))
    print('\n')
