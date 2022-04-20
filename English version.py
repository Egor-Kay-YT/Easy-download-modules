#import the os from installation
import os
#greeting
installation = input('Hi, this is the installation of modules\nPlease enter the module:')
#installation
os.system(f'pip install {installation}')
#done
print('[!]Modules successfully installation!')