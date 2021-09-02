from os import RTLD_LAZY, close, memfd_create
import platform
import sys 
import datetime
import random

rand = random.randint(0,5)

print(rand)

max_char = 0
lines_num = 0
    
def count_max_char():
    max_char = 0

    with open(f'/home/yanosik/Py/neofetch/ASCII/ASCII%s.txt' % (rand), 'r') as r:    
        for count, line in enumerate(r):
            if len(line) > max_char:
                max_char = len(line)
        return max_char

with open(f'/home/yanosik/Py/neofetch/ASCII/ASCII%s.txt' % (rand), 'r') as r:

    max_char = count_max_char() + 5
    print(max_char)
    for lines in r:
        print(lines.strip('\n') + ' '*(max_char - len(lines)) + ' ?')
        

# with open(f'/home/yanosik/Py/neofetch/ASCII/ASCII%s.txt' % (rand), 'r') as r:
#     for lines in r:
#         print(lines.strip('\n'))
    


#print(len(line.strip('\n')))

#print(count + 1)
