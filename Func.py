import os
import sys
import platform
import psutil
import datetime

uname = platform.uname()


def time_since_start():

    return os.popen("uptime -p").read()[:-1]


def get_current_dir():

    return os.getcwd()


def cpu_count():

    cpucount = psutil.cpu_count(logical=True)

    return str(cpucount)


def proc_info():
    with open("/proc/version", "r") as r:
        return r.read().split()


def cpu_info():

    with open("/proc/cpuinfo", "r") as r:
        return " ".join(r.readlines()[4].split()[3:])


def mem_info():
    with open("/proc/meminfo", "r") as r:
        memT = []

        mem = r.readlines()[0:2]

        memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]

        return memT


def time_till():
    to_preorder = datetime.datetime(2021, 9, 24, 0, 0)

    today = datetime.datetime.now()

    time = to_preorder - today

    return str(time)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print(
    " " * 20
    + f"{bcolors.FAIL}/´¯¯/"
    + f"{bcolors.OKBLUE}           Current Directory: "
    + f"{bcolors.HEADER}"
    + get_current_dir()
)
print(
    " " * 19
    + f"{bcolors.FAIL}/¯.../"
    + f"{bcolors.OKBLUE}           Uptime: "
    + f"{bcolors.HEADER}"
    + time_since_start()
)
print(
    " " * 18
    + f"{bcolors.FAIL}/..../'"
    + f"{bcolors.OKBLUE}           Platform: "
    + f"{bcolors.HEADER}"
    + proc_info()[0]
    + " "
    + platform.architecture()[0]
    + " "
    + platform.machine()
)
print(
    " " * 13
    + f"{bcolors.FAIL}/´¯/'..'/´¯¯`·¸"
    + f"{bcolors.OKBLUE}        Machine: "
    + f"{bcolors.HEADER}"
    + proc_info()[9]
    + " "
    + f"{bcolors.OKBLUE} Cores: "
    + f"{bcolors.HEADER}"
    + " "
    + f"{cpu_count()}"
)
print(
    " " * 10
    + f"{bcolors.FAIL}/'/.../..../....../¨')"
    + f"{bcolors.OKBLUE}    Kernel: "
    + f"{bcolors.HEADER}"
    + proc_info()[2]
)
print(
    " " * 9
    + f"{bcolors.FAIL}('(....´...´... ¯~/'..')"
    + f"{bcolors.OKBLUE}   CPU: "
    + f"{bcolors.HEADER}"
    + cpu_info()
)
print(
    " " * 10
    + f"{bcolors.FAIL}\..............'...../"
    + f"{bcolors.OKBLUE}    Memory: "
    + f"{bcolors.HEADER}"
    + mem_info()[1]
    + " / "
    + mem_info()[0]
)
print(
    " " * 11
    + f"{bcolors.FAIL}\....\.........._.·´"
    + f"{bcolors.OKBLUE}     Young Leosia Ep: "
    + f"{bcolors.HEADER}"
    + time_till()
)
print(" " * 12 + f"{bcolors.FAIL}\..............(")
print(" " * 13 + f"{bcolors.FAIL}\..............(")
