import subprocess

def getOutput(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.PIPE).communicate()

    print(p[0].decode('utf-8'))

getOutput('cat /proc/meminfo')