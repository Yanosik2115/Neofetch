import os
import platform
import psutil
import datetime
from enum import Enum

class sysFiles(Enum):
    proc ='/proc/'
    ver = 'version'
    mem = 'meminfo'
    cpu = 'cpuinfo'

def get_OS():
    uname = platform.uname()[0]
    if uname == "Linux":
        return "Linux"
    elif uname == "Windows":
        return "Windows"
    elif uname == "MacOS":
        return "MacOS"

class informationManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def openF(self):
        if get_OS() == "Linux":
            r = open("%s%s" % (sysFiles.proc.value, self.file_name))
            return r

class CPUInfo(informationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def cpu_info():
        x = informationManager(sysFiles.cpu.value)
        return " ".join(x.openF().readlines()[4].split()[3:])

class procInfo(informationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def proc_info():
        x = informationManager(sysFiles.ver.value)
        return x.openF().read().split()

class memoryInfo(informationManager):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def total_memory_info():
        x = informationManager(sysFiles.mem.value)
        mem = x.openF().readlines()[0:2]
        memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
        return memT[0]

    def free_memory_info():
        x = informationManager(sysFiles.mem.value)
        mem = x.openF().readlines()[0:2]
        memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
        return memT[1]

def time_since_start():
    return os.popen("uptime -p").read()[:-1]

def get_current_dir():
    return os.getcwd()

def cores_count():
    cpucount = psutil.cpu_count(logical=True)
    return str(cpucount)

def time_till():
    till_date = datetime.datetime(2021, 9, 24, 0, 0)
    today = datetime.datetime.now()
    time_left = till_date - today

    return str(time_left)

def funny_things():
    #platform
    procInfo.proc_info()[0]
    
    platform.architecture()[0]
    
    platform.machine()

    #machine
    procInfo.proc_info()[9]

    #kernel 
    procInfo.proc_info()[2]

# print(
#     " " * 20
#     + f"{Bcolors.FAIL.value}/´¯¯/"
#     + f"{Bcolors.OKBLUE.value}           Current Directory: "
#     + f"{Bcolors.HEADER.value}"
#     + get_current_dir()
# )
# print(
#     " " * 19
#     + f"{Bcolors.FAIL.value}/¯.../"
#     + f"{Bcolors.OKBLUE.value}           Uptime: "
#     + f"{Bcolors.HEADER.value}"
#     + time_since_start()
# )
# print(
#     " " * 18
#     + f"{Bcolors.FAIL.value}/..../'"
#     + f"{Bcolors.OKBLUE.value}           Platform: "
#     + f"{Bcolors.HEADER.value}"
#     + procInfo.proc_info()[0]
#     + " "
#     + platform.architecture()[0]
#     + " "
#     + platform.machine()
# )
# print(
#     " " * 13
#     + f"{Bcolors.FAIL.value}/´¯/'..'/´¯¯`·¸"
#     + f"{Bcolors.OKBLUE.value}        Machine: "
#     + f"{Bcolors.HEADER.value}"
#     + procInfo.proc_info()[9]
#     + " "
#     + f"{Bcolors.OKBLUE.value} Cores: "
#     + f"{Bcolors.HEADER.value}"
#     + " "
#     + f"{cores_count()}"
# )
# print(
#     " " * 10
#     + f"{Bcolors.FAIL.value}/'/.../..../....../¨')"
#     + f"{Bcolors.OKBLUE.value}    Kernel: "
#     + f"{Bcolors.HEADER.value}"
#     + procInfo.proc_info()[2]
# )
# print(
#     " " * 9
#     + f"{Bcolors.FAIL.value}('(....´...´... ¯~/'..')"
#     + f"{Bcolors.OKBLUE.value}   CPU: "
#     + f"{Bcolors.HEADER.value}"
#     + CPUInfo.cpu_info()
# )
# print(
#     " " * 10
#     + f"{Bcolors.FAIL.value}\..............'...../"
#     + f"{Bcolors.OKBLUE.value}    Memory: "
#     + f"{Bcolors.HEADER.value}"
#     + memoryInfo.free_memory_info()
#     + " / "
#     + memoryInfo.total_memory_info()
# )
# print(
#     " " * 11
#     + f"{Bcolors.FAIL.value}\....\.........._.·´"
#     + f"{Bcolors.OKBLUE.value}     Young Leosia Ep: "
#     + f"{Bcolors.HEADER.value}"
#     + time_till()
# )
# print(" " * 12 + f"{Bcolors.FAIL.value}\..............(")
# print(" " * 13 + f"{Bcolors.FAIL.value}\..............(")
