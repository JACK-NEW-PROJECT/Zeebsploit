from .tmp.temp import logo
from .tmp.temp import __name as asc
from .tmp.help import Helper as _help
from .process import information_gathering as infoga
from .process import exploitation as exploit
from .process import __scanner as scan
from .modules.color import R,G,B,Y,W


class zeeb_sploit(object):

      def zeebsploit_framework(self):
          print(f"\n{Y}[!]{W} Type {R}'Exit'{W} for out from this Tool\n")
          print(f"\n{Y}[!]{W} Type {G}'Help'{W} for show modules\n")
          while True:
                 try:
                    zsf = str(input('[zsf]: ')).lower()
                    if   zsf == 'exploit':
                         exploit()
                    elif zsf == 'infoga':
                         infoga()
                    elif zsf == 'scanner':
                         scan()
                    elif zsf == 'help':
                         print(f'\n{Y}[!]{W} Type one of the modules name to use \n')
                         _help.utama()
                    elif zsf == 'exit':
                         exit('Exit...')
                    else:
                         print(f'\n - No Command {zsf}\n')
                 except KeyboardInterrupt:
                    exit('aborted...') 
                 except EOFError:
                    exit('aborted...')
def main():
    for i in range(10):
        asc()
    print(logo)
    zeeb_sploit().zeebsploit_framework()





