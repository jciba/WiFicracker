import subprocess
from subprocess import PIPE, Popen

interface = []

nic = ""

ssid = ""

def interface_check():
    global interface
    global eg
    #interface = input("Please enter the name of the wireless interface: ")
    proc = Popen(["iw", "dev"], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        ln = line.decode('utf8').split()
        if(ln[0]=='Interface'):
            interface.append(ln)
    proc.wait()
    proc.kill()

def interface_select():
    global interface
    global nic
    print("Availiable interfaces \n")
    x = 0
    for line in interface:
        print(str(x) + " "+ line[1])
        x += 1

    w = int(input("Please enter ID of a wireless interface you wish to use: "))
    print("\n")

    nic = interface[w][1]
def get_ssid():
    global nic
    proc = Popen(["airodump-ng", nic], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        print(line)

def start_monitor():
    global nic
    proc = Popen(["airmon-ng", "check", "kill"],stdout=PIPE, stderr=PIPE)
    proc.wait()
    proc.kill()
    subprocess.call("airmon-ng start "+ nic,shell=True)
interface_check()
interface_select()
print("Using: " + nic)
#start_monitor()
#get_ssid()
