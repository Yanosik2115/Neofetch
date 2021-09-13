import psutil

def cores_count():
        cpucount = psutil.cpu_count(logical=True)
        print (cpucount)

cores_count()