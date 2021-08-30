import os 
import sys
import platform

time = os.popen('uptime -p').read()[:-1]
arch = platform.architecture()
mach = platform.machine()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f'{bcolors.WARNING}.....................' + f'{bcolors.FAIL}/´¯¯/' + f'{bcolors.OKBLUE}          Current Directory: ' + f'{bcolors.HEADER}' + os.getcwd())
print(f'{bcolors.WARNING}...................' + f'{bcolors.FAIL},/¯.../' + f'{bcolors.OKBLUE}          Uptime: ' + f'{bcolors.HEADER}' + time) 
print(f"{bcolors.WARNING}..................." + f"{bcolors.FAIL}/..../'" + f'{bcolors.OKBLUE}          Platform: ' + f'{bcolors.HEADER}' + sys.platform + ' ' + platform.architecture()[0] + ' ' + platform.machine())
print("............../´¯/'..'/´¯¯`·¸")
print(".........../'/.../..../....../¨¯")
print("..........('(....´...´... ¯~/'..')")
print("...........\..............'...../")
print("............\....\.........._.·´")
print(".............\..............(")
print('..............\..............(')