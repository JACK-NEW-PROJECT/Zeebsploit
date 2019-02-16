import sys,time,requests,os,re
import platform as plat
import readline

ip = requests.get('https://www.myip.com').text
prot = re.findall('id="ip">(.*?)</',ip)[0]
B = '\033[94m'
P = '\033[0m'
K = '\033[93m'
I = '\033[92m'
A = '\033[91m'
X = '\033[96m'

logo = f"""
                 -  407 AUTHENTIC EXPLOIT -
        {B}
       ____           _     ___        _       _  _
      |_  / ___  ___ | |__ / __| _ __ | | ___ (_)| |{I} {P} version :{K} 2.0{P}
     {B}  / / / -_)/ -_)| '_  \\__ \| '_ \| |/ _ \| ||  _|
      /___|\___|\___||_.__/|___/| .__/|_|\___/|_| \__|
                                |_|{P} 
      
      Codename  :{X} JaxBCD{P}
      Your IP   :{K} {prot}{P}
      platform  :{I} {plat.system()} {plat.node()} {plat.release()} {plat.version()} {plat.machine()} {plat.processor()}{P}
      user@host :{A} {os.getlogin()}{P}@{A}{plat.node()}{P}
      """      
def __name():
    a = '[\033[92m⣾\033[0m]', '[\033[92m⣽\033[0m]', '[\033[92m⣻\033[0m]', '[\033[92m⢿\033[0m]', '[\033[92m⡿\033[0m]', '[\033[92m⣟\033[0m]', '[\033[92m⣯\033[0m]', '[\033[92m⣷\033[0m]'                                   
    for i in a:
        sys.stdout.write('   Starting Zeebsploit Framework\r - %s'%i)
        sys.stdout.flush()
        time.sleep(0.10)

        
