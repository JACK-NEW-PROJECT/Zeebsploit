#-*- coding: utf-8 -*-
import os, requests,re,sys
import time


ip = requests.get('https://www.myip.com').text
prot = re.findall('id="ip">(.*?)</',ip)[0]
u = os.uname()
logo = """\033[92m
         00000    0000  0000  00000     0000   0000   00     000000 00 0000000
           00    00    00    00  00    00     00 00  00     00  00 00    00
          00    0000  0000  00 000    00     00000  00     00  00 00    00\033[0m
         00    00    00    00   00      00  00     00     00  00 00    00
        00000 0000  0000  0000000    00000 00     000000 000000 00    00
                                                      [codename] : \033[93mJaxBCD\033[0m
                                                      [version]  : \033[94m1.0\033[0m
        BY : \033[92m407 AUTHENTIC EXPLOIT\033[0m
        Your IP : \033[92m{}\033[0m
        uname : \033[92m{} {} {} {} {}\033[0m
        user@host : \033[91m{}\033[0m@\033[91m{}\033[0m
                 """.format(prot,u.sysname,u.nodename,u.release,u.version,u.machine,os.getlogin(),u.nodename)



def red(tx):
    return('\033[91m'+tx+'\033[0m')

def blue(tx):
    return('\033[94m'+tx+'\033[0m')

def green(tx):
    return('\033[92m'+tx+'\033[0m')

def yellow(tx):
    return('\033[93m'+tx+'\033[0m')



def loading(tx):
    for i in tx + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(3./30)
