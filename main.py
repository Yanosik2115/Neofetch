import os 
import sys
import platform
import psutil

time = os.popen('uptime -p').read()[:-1]

uname = platform.uname()

cpucount = psutil.cpu_count(logical=True)

str(cpucount)

file1 = open('/proc/version', 'r')

proc =  file1.read().split()

file2 = open('/proc/cpuinfo', 'r')

cpu = ' '.join(file2.readlines()[4].split()[3:])

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


print(' '*20 + f'{bcolors.FAIL}/´¯¯/' + f'{bcolors.OKBLUE}           Current Directory: ' + f'{bcolors.HEADER}' + os.getcwd())
print(' '*19 + f'{bcolors.FAIL}/¯.../' + f'{bcolors.OKBLUE}           Uptime: ' + f'{bcolors.HEADER}' + time) 
print(' '*18 + f"{bcolors.FAIL}/..../'" + f'{bcolors.OKBLUE}           Platform: ' + f'{bcolors.HEADER}' + proc[0] + ' ' + platform.architecture()[0] + ' ' + platform.machine())
print(' '*13 + f"{bcolors.FAIL}/´¯/'..'/´¯¯`·¸" + f'{bcolors.OKBLUE}        Machine: ' + f'{bcolors.HEADER}' + proc[9] + ' ' + f'{bcolors.OKBLUE} Cores: ' + f'{bcolors.HEADER}' + ' ' + f'{str(cpucount)}')
print(' '*10 + f"{bcolors.FAIL}/'/.../..../....../¨')" + f'{bcolors.OKBLUE}    Kernel: ' + f'{bcolors.HEADER}' + proc[2])
print(' '*9 +  f"{bcolors.FAIL}('(....´...´... ¯~/'..')" + f'{bcolors.OKBLUE}   CPU: ' + f'{bcolors.HEADER}' + cpu)
print(' '*10 + f"{bcolors.FAIL}\..............'...../")
print(' '*11 + f"{bcolors.FAIL}\....\.........._.·´")
print(' '*12 + f"{bcolors.FAIL}\..............(")
print(' '*13 + f'{bcolors.FAIL}\..............(')

file1.close()
file2.close()