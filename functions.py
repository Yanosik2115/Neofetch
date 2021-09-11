import os, sys
import platform
import psutil
import datetime
from enum import Enum


class sysFiles(Enum):
    proc = "/proc/"
    ver = "version"
    mem = "meminfo"
    cpu = "cpuinfo"


def get_OS():
    if sys.platform.startswith("linux"):  # variations: linux2,linux-i386 (any others?)
        return "Linux"
    elif sys.platform.startswith("win32"):
        return 'Windows'
    elif sys.platform == "darwin":       
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


def get_name():
    return platform.node()


def time_till():
    till_date = datetime.datetime(2021, 9, 24, 0, 0)
    today = datetime.datetime.now()
    time_left = till_date - today

    return str(time_left)


def funny_things():
    # platform
    procInfo.proc_info()[0]

    platform.architecture()[0]

    platform.machine()

    # machine
    procInfo.proc_info()[9]

    # kernel
    procInfo.proc_info()[2]
