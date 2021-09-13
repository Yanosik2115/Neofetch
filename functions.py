import datetime
import os
import platform
import subprocess
import sys
import warnings
from enum import Enum

import psutil


class GetOS:
    def get_OS():
        if sys.platform.startswith("linux"):
            return "Linux"
        elif sys.platform.startswith("win32") or sys.platform.startswith("win64"):
            return "Windows"
        elif sys.platform == "darwin":
            return "darwin"

    OS = get_OS()


class SysFiles(Enum):
    proc = "/proc/"
    ver = "version"
    mem = "meminfo"
    cpu = "cpuinfo"


def get_output(cmd):
    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE
    ).communicate()
    return p[0].decode("utf-8")


class InformationManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def openF(self):
        if GetOS.OS == "Linux":
            r = open("%s%s" % (SysFiles.proc.value, self.file_name))
            return r
        else:
            raise warnings.warn(message="Cannot read CPU information", stacklevel=2)


class CPUInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def cpu_info():
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.cpu.value)
            return " ".join(x.openF().readlines()[4].split()[3:])
        elif GetOS.OS == "darwin":
            r = get_output("sysctl -n machdep.cpu.brand_string")
            return r


class ProcInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def environment():
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.ver.value)
            return x.openF().read().split()[5][1:]
        if GetOS.OS == "darwin":
            pass

    def platform():
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.ver.value)
            return x.openF().read().split()[0]
        elif GetOS.OS == "darwin":
            x = get_output("sw_vers")
            return x.split()[1:3]

    def kernel():
        # if GetOS.OS == "Linux":
        #     x = InformationManager(SysFiles.ver.value)
        #     return x.openF().read().split()[2]
        # elif GetOS.OS == "darwin":
        #     x = platform.release()
        #     return x
        x = platform.release()
        return x


class MemoryInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def total_memory_info():
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.mem.value)
            mem = x.openF().readlines()[0:2]
            memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
            return memT[0]
        elif GetOS.OS == "darwin":
            return psutil.virtual_memory()[0]

    def free_memory_info():
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.mem.value)
            mem = x.openF().readlines()[0:2]
            memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
            return memT[1]
        elif GetOS.OS == "darwin":
            return psutil.virtual_memory()[3]


class BaseLibraryFunctions:
    def time_since_start():
        if GetOS.OS is not "darwin":
            return str(os.popen("uptime -p").read()[:-1])
        return str(os.popen("uptime").read()[:-1])

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
