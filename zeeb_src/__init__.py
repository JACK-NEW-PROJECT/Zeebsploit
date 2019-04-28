from .exploit_src import main as exploit
from .scanner_src import main as scanner
from .recon_src import main as recon
from .utils import art,show
import readline
name_modules = ['exploits','scanners','footprinting']
desc_modules = ['exec exploits modules','exec scanners modules','exec footprinting  modules']

def main():
    print(art)
    print('!type "help" for show modules\n!type "exit" for logout from tool\n!type "back" for back to main menu')
    while True:
          try:
              xx = input('zsf(\033[91mx\033[0m): ').lower()
              if xx == name_modules[0]:
                 exploit()
              elif xx == name_modules[1]:
                 scanner()
              elif xx == name_modules[2]:
                 recon()
              elif xx == 'help':
                 show(name_modules,desc_modules)
              elif xx == 'exit':
                 exit()
              elif xx == 'back':
                 pass
              else:
                 print(f'\033[91m!\033[0m no command {xx}')
          except Exception as e:
              print(e) 
          except KeyboardInterrupt:
              exit()