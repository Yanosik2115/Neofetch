from os import close, memfd_create
import platform
import sys 
import datetime

to_preorder = datetime.datetime(2021,9,24, 0, 0)

today = datetime.datetime.now()

time = to_preorder - today

print(to_preorder)
print(today)
print(time)

# file1 = open('/proc/meminfo', 'r')

# mem = file1.readlines()[0:2]
# memTotal = ' '.join(mem[0].split()[1:])
# memFree = ' '.join(mem[1].split()[1:])

# print(memTotal)
# print(memFree)

# file1.close()


# uname = platform.uname()


# print(uname.version.split()[0])
#print(platform.architecture()[0])
#print(platform.machine())