from .exploits import exploit_main
from .infoga import infoga_main
from .scanners import scanner_main
from .tmp.modules import log_,show,art
import readline
name_modules = ['exploits','scanners','footprinting']
desc_modules = ['exec exploits modules','exec scanners modules','exec information gathering modules']
def gwe_serius():
    print(art)
    print('!type "help" for show modules\n!type "exit" for logout from tool\n!type "back" for back to main menu')
    while True:
          try:
             xxx = input('zsf(\033[91mx\033[0m): ').lower()
             if xxx == name_modules[0]:
                exploit_main().main()
             elif xxx == name_modules[1]:
                 scanner_main().main()
             elif xxx == name_modules[2]:
                 infoga_main().main()
             elif xxx == 'exit':
                 exit()
             elif xxx == 'help':
                  show(name_modules,desc_modules)
             elif xxx == 'back':
                  pass
             else:
                print(f'\033[91m!\033[0mno module: {xxx}')
          except Exception as e:
             print(e)
          except KeyboardInterrupt:
             exit()
