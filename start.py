import subprocess
from subprocess import PIPE, Popen

interface = ""
eg = False
ssid = ""

def interface_check():
    global interface
    global eg
    interface = input("Please enter the name of the wireless interface: ")
    proc = Popen(["iw", "dev"], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        ln = line.decode('utf8').split()
        if(ln[0]=='Interface' and ln[1] == interface):
            eg = True
            print(eg)
    proc.kill()

def get_ssid():
    global interface
    proc = Popen(["airodump-ng", interface], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        print(line)

def start_monitor():
    global interface
    proc = Popen(["airmon-ng", "check", "kill"],stdout=PIPE, stderr=PIPE)
    proc.wait()
    proc.kill()
    subprocess.call("airmon-ng start "+ interface,shell=True)
interface_check()
start_monitor()
print("hello")
#get_ssid()
