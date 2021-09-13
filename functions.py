import os, sys
import platform
import psutil
import datetime
from enum import Enum
import subprocess
import warnings


class SysFiles(Enum):
    proc = "/proc/"
    ver = "version"
    mem = "meminfo"
    cpu = "cpuinfo"

def get_output(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE).communicate()

    return(p[0].decode('utf-8'))

def get_OS():
    if sys.platform.startswith("linux"):  # variations: linux2,linux-i386 (any others?)
        return "Linux"
    elif sys.platform.startswith("win32"):
        return 'Windows'
    elif sys.platform == "darwin":       
        return "darwin"

class InformationManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def openF(self):
        if get_OS() == "Linux":
            r = open("%s%s" % (SysFiles.proc.value, self.file_name))
            return r
        elif get_OS() == 'darwin':
            r = get_output('sysctl -n machdep.cpu.brand_string')
            return r
        else:
            raise warnings.warn(message='Cannot read CPU information', stacklevel=2) 
class CPUInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def cpu_info():
        x = InformationManager(SysFiles.cpu.value)
        return " ".join(x.openF().readlines()[4].split()[3:])


class ProcInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def proc_info():
        OS = get_OS()

        if OS == 'Linux':
            x = InformationManager(SysFiles.ver.value)
            return x.openF().read().split()
        elif OS == 'darwin':
            x = InformationManager()
            return x.openF()
            


class MemoryInfo(InformationManager):
    def __init__(self, file_name):
        super().__init__(file_name)

    def total_memory_info():
        x = InformationManager(SysFiles.mem.value)
        mem = x.openF().readlines()[0:2]
        memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
        return memT[0]

    def free_memory_info():
        x = InformationManager(SysFiles.mem.value)
        mem = x.openF().readlines()[0:2]
        memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
        return memT[1]

class BaseLibraryFunctions():
    
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

    def machine_info():
        # platform
        ProcInfo.proc_info()[0]

        platform.architecture()[0]

        platform.machine()

        # machine
        ProcInfo.proc_info()[9]

        # kernel
        ProcInfo.proc_info()[2]
