import os, sys
import platform
import psutil
import datetime
from enum import Enum
import subprocess
import warnings


class GetOS:
    """Returns Operating System
    """
    def get_OS() -> str:
        """Returns Operating System based on sys.platform output

        Returns
        -------
        str
            Operating System
        """
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
    """Takes required terminal command to execute 

    Parameters
    ----------
    cmd : str
        Terminal Command

    Returns
    -------
    Any
        Decoded('utf-8') terminal output 
    """
    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE
    ).communicate()
    return p[0].decode("utf-8")


class InformationManager:
    """ Opens and returns required file 
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def openF(self):
        """
        Returns required file from system 
        -------
        Any
            Returns file 
        """
        if GetOS.OS == "Linux":
            r = open("%s%s" % (SysFiles.proc.value, self.file_name))
            return r

class CPUInfo(InformationManager):
    """
    
    ----------
    InformationManager : [type]
        [description]
    """
    def __init__(self, file_name):
        super().__init__(file_name)

    def cpu_info() -> str:
        """
        Returns current operating system
        -------
        str
            Linux -> reads from /proc/cpuinfo \n
            Darwin -> returns output of "sysctl -n machdep.cpu.brand_string"
        """
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.cpu.value)
            return " ".join(x.openF().readlines()[4].split()[3:])
        elif GetOS.OS == "darwin":
            r = get_output("sysctl -n machdep.cpu.brand_string")
            return r


class ProcInfo(InformationManager):
    """
    Information about environment, platform and kernel
    ----------
    InformationManager : Class
        Opens file based on requirement information
    """
    def __init__(self, file_name):
        super().__init__(file_name)

    def environment() -> str:
        """
        Returns string of current environment
        -------
        str
            Linux -> reads from /proc/version \n
            Darwin -> returns Darwin
        """
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.ver.value)
            return x.openF().read().split()[5][1:]
        if GetOS.OS == "darwin":
            return 'Darwin'

    def platform() -> list:
        """
        Returns currently used platform
        -------
        list[str]
            Linux -> reads first line from /proc/version \n
            Darwin -> get_output('sw_vers)
        """
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.ver.value)
            return x.openF().read().split()[0]
        elif GetOS.OS == "darwin":
            x = get_output("sw_vers")
            return x.split()[1:3]

    def kernel() -> str:
        """
        Returns kernel information
        -------
        str
            platform.release()
        """
        x = platform.release()
        return x


class MemoryInfo(InformationManager):
    """
    Information about Total and Free Memory
    ----------
    InformationManager : Class
        Opens file based on requirement information
    """

    def __init__(self, file_name):
        super().__init__(file_name)

    def total_memory_info() -> str:
        """
        Returns Total Memory 
        -------
        str 
            psutil.virtual_memory()[0]
        """
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.mem.value)
            mem = x.openF().readlines()[0:2]
            memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
            return memT[0]
        elif GetOS == "darwin":
            return psutil.virtual_memory()[0]

    def free_memory_info() -> str:
        """
        Returns Free Memory
        -------
        str
            psutil.virtual_memory()[3]
        """
        if GetOS.OS == "Linux":
            x = InformationManager(SysFiles.mem.value)
            mem = x.openF().readlines()[0:2]
            memT = [" ".join(mem[0].split()[1:]), " ".join(mem[1].split()[1:])]
            return memT[1]
        elif GetOS == "darwin":
            return psutil.virtual_memory()[3]


class BaseLibraryFunctions:
    """Functions that require only python base library imports
    """
    def time_since_start() -> str:
        """returns uptime

        Returns
        -------
        str
            string contains output of 'uptime -p'
        """
        x = os.popen("uptime -p").read()[:-1]
        return str(x)

    def get_current_dir() -> str:
        """returns current directory 

        Returns
        -------
        str
            os.getcwd()
        """
        return os.getcwd()

    def cores_count() -> str:
        """Returns number of cores

        Returns
        -------
        str
            psutil.cpu_count()
        """
        cpucount = psutil.cpu_count(logical=True)
        return str(cpucount)

    def get_name() -> str:
        """Returns name of computer

        Returns
        -------
        str
            platform.node()
        """
        return platform.node()

    def time_till() -> str:
        """returns time till some event

        Returns
        -------
        str
            
        """
        till_date = datetime.datetime(2021, 9, 24, 0, 0)
        today = datetime.datetime.now()
        time_left = till_date - today
        return str(time_left)
