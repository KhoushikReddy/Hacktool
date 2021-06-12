#!usr/bin/env python

import subprocess

list_of_tools = ["1: MAC address Changer", "2: Network Scanner", "3: ARP Spoofer", "4: Packet Sniffer"]
print("Execute The program again if you want to use another tool within the program")
def tools():
    for tool in list_of_tools:
        print(tool)
    user_input = int(input("Select the tool you wish to use: "))
    return user_input

user_input = tools()

if user_input == 1:
    print("____________________________________________________________")
    print("Welcome to MAC address Changer")
    print("------------------------------------------------------------")
    interface = input("Enter Interface that needs change in mac address: ")
    new_mac = input("Enter Desired mac Address: ")
    def mac_change(interface, new_mac):
        print("[+] Changing " + interface + " Macaddress to " + new_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    mac_change(interface, new_mac)
    print("Execute The program again if you want to use another tool within the program")
    exit()


elif user_input == 2:
    print("____________________________________________________________")
    print("Welcome to network scanner")
    print("------------------------------------------------------------")

    import scapy.all as scapy


    def scan_network(ip):
        request = scapy.ARP(pdst=ip)
        sending = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # print(request.summary())
        # This is used to list the values that can be set in the function
        # scapy.ls(scapy.ARP())
        # print(sending.summary())
        request_sending = sending / request
        # print(request_sending.summary())
        answer = scapy.srp(request_sending, timeout=1)[0]
        # print(answer.summary())
        print("IP\t\t\tMAC Address\n")
        for x in answer:
            print(x[1].psrc + "\t\t" + x[1].hwdst + '\n')



    scan_network("10.0.2.1/24")
    print("Execute The program again if you want to use another tool within the program")
    exit()

elif user_input == 3:
    print("____________________________________________________________")
    print("Welcome to ARP spoofer")
    print("------------------------------------------------------------")

elif user_input == 4:
    print("____________________________________________________________")
    print("Welcome to Packet Sniffer")
    print("------------------------------------------------------------")

else:
    print("____________________________________________________________")
    print("Selection out of bounds")
    print("------------------------------------------------------------")
