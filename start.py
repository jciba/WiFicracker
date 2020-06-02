import subprocess
from subprocess import PIPE, Popen

interface = []
nic = ""
ssid = ""
monNic = ""

def info():
    print("running this software may harm your computer\n\n")
    print("!!!Running this software may impact some processes on your computer!!!\n")
    print("If you encounter issues please REBOOT\n")

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

    print("Using: " + nic)

def get_ssid():
    global nic
    proc = Popen(["airodump-ng", nic], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        print(line)

def start_monitor():
    global nic
    global monNic
    proc = Popen(["sudo","-i","airmon-ng", "check","kill"],stdout=PIPE, stderr=PIPE)
    proc.wait()
    for line in proc.stdout:
        print(line)
    proc.wait()
    proc.kill()
    proc = Popen(["sudo","-i","airmon-ng", "start",nic],stdout=PIPE, stderr=PIPE)
    proc.wait()
    for line in proc.stdout:
        ln = line.decode('utf8').split()
        for x in ln:
            print(x)

    proc.kill()
    monNic = nic + "mon"

def stop_monitor():
    global nic
    global monNic
    
    print(monNic)


info()
interface_check()
interface_select()
start_monitor()

#get_ssid()

stop_monitor()
