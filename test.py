from os import close
import platform
import sys 

file1 = open('/proc/cpuinfo', 'r')

cpu = ' '.join(file1.readlines()[4].split()[3:])

print(cpu)

file1.close()


# uname = platform.uname()


# print(uname.version.split()[0])
#print(platform.architecture()[0])
#print(platform.machine())