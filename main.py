import random
from enum import Enum
import functions as f


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

class Random():
    def rand():
        rand = random.randint(0, 5)
        return rand

    random = rand() 


def count_max_char():
    max_char = 0
    with open(f"./ASCII/ASCII%s.txt" % (Random.random), "r") as r:
        for line in r:
            if len(line) > max_char:
                max_char = len(line)
        return max_char


with open(f"./ASCII/ASCII%s.txt" % (Random.random), "r") as r:

    max_char = count_max_char() + 5
    print(f"{Bcolors.HEADER.value}")

    for value, lines in enumerate(r):
        if value == 1:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.HEADER.value}"
                + f.BaseLibraryFunctions.get_name()
            )
        elif value == 2:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKCYAN.value}"
                + "=" * len(f.BaseLibraryFunctions.get_name())
            )
        elif value == 3:
            print(
                f"{Bcolors.HEADER.value}"
                + lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Current Directory: "
                + f"{Bcolors.HEADER.value}"
                + f.BaseLibraryFunctions.get_current_dir()
            )
        elif value == 4:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Uptime: "
                + f"{Bcolors.HEADER.value}"
                + f.BaseLibraryFunctions.time_since_start()
            )
        elif value == 5:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Platform: "
                + f"{Bcolors.HEADER.value}"
                + f.ProcInfo.proc_info()[0]
                + " "
                + f.platform.architecture()[0]
                + " "
                + f.platform.machine()
            )
        elif value == 5:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Machine: "
                + f"{Bcolors.HEADER.value}"
                + f.ProcInfo.proc_info()[9]
                + " "
                + f"{Bcolors.OKBLUE.value}Cores: "
                + f"{Bcolors.HEADER.value}"
                + f.BaseLibraryFunctions.cores_count()
            )
        elif value == 6:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Kernel: "
                + f"{Bcolors.HEADER.value}"
                + f.ProcInfo.proc_info()[2]
            )
        elif value == 7:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}CPU: "
                + f"{Bcolors.HEADER.value}"
                + f.CPUInfo.cpu_info()
            )
        elif value == 7:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Memory: "
                + f"{Bcolors.HEADER.value}"
                + f.MemoryInfo.free_memory_info()
                + "/"
                + f.MemoryInfo.total_memory_info()
            )
        elif value == 8:
            print(
                lines.strip("\n")
                + " " * (max_char - len(lines))
                + f"{Bcolors.OKBLUE.value}Young Leosia Ep: "
                + f"{Bcolors.HEADER.value}"
                + f.BaseLibraryFunctions.time_till()
            )
        else:
            print(lines.strip("\n"))
