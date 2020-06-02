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
    
    #proc = Popen(["sudo","iw", "dev"], stdout=PIPE, stderr=PIPE)
    proc = subprocess.run(["sudo","iw", "dev"],capture_output=True,text=True)
    w = proc.stdout.split()
    x = len(w)    
    for i in range(0,x):
        if (w[i] == "Interface"):
            interface.append(w[i+1])
            #print(w[i+1])
 
def interface_select():
    global interface
    global nic
    global monNic
    print("Availiable interfaces \n")
    x = 0
    for line in interface:
        print(str(x) + " "+ line)
        x += 1

    w = int(input("Please enter ID of a wireless interface you wish to use: "))
    print("\n")

    nic = interface[w]

    print("Using: " + nic)

def get_ssid():
    global nic
    proc = Popen(["airodump-ng", nic], stdout=PIPE, stderr=PIPE)
    for line in proc.stdout:
        print(line)

def check_processes():
    global nic
    global monNic
    proc = subprocess.run(["sudo","airmon-ng", "check",],capture_output=True,text=True)
    print(proc.stdout)

def start_monitor():
    global nic
    global monNic
    print("Attempting to stop all processes that may cause issues")
    #proc = Popen(["sudo","airmon-ng", "check","kill"],stdout=PIPE, stderr=PIPE)
    #proc.communicate(timeout=20)
    proc = subprocess.run(["sudo","airmon-ng", "check","kill"],capture_output=True,text=True)
    for line in proc.stdout:
        print(line)    
    
    print("Processes terminated")

    print("Starting monitor mode")
    proc = Popen(["sudo","-i","airmon-ng", "start",nic],stdout=PIPE, stderr=PIPE)
    
    #proc.communicate(timeout=20)
    for line in proc.stdout:
        ln = line.decode('utf8').split()
        for x in ln:
            print(x)

    
    monNic = nic + "mon"

def stop_monitor():
    global nic
    global monNic
    proc = subprocess.run(["sudo","airmon-ng", "stop",monNic],capture_output=True,text=True)
    print("Stopping monitor mode")
    
    


#info()
interface_check()
interface_select()
check_processes()
#start_monitor()

#get_ssid()

#stop_monitor()
