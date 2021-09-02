import random
from enum import Enum
import functions
class Bcolors(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def rand():
    rand = random.randint(0, 5)
    return rand

def count_max_char():

    max_char = 0

    with open(f"/home/yanosik/Py/neofetch/ASCII/ASCII%s.txt" % (rand()), "r") as r:
        for line in r:
            if len(line) > max_char:
                max_char = len(line)
        return max_char

with open(f"/home/yanosik/Py/neofetch/ASCII/ASCII%s.txt" % (rand()), "r") as r:

    max_char = count_max_char() + 5
    print(max_char)

    for lines in r:
        print(lines.strip("\n") + " " * (max_char - len(lines)) + " ?")
