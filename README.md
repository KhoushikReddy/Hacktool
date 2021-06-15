# Hacktool
Hello, this is a basic tool which has 4 components
1. Mac address changer
2. Network scanner
3. ARP spoofing
4. Packet sniffing

The options 2,3,4 will npt work if option 1 is selected and the MAC address is changed
2. Network scanner is used to scan all the devices connected to a specific interface i.e, wired/wireless. When asked to enter Interface enter either "eth0' or "wlan0".
3. Before Executing the ARP spoofing tool enter "echo 1 > /proc/sys/net/ipv4/ip_forward" to enable port forwarding.
4. ARP spoofing is used to perform MITM(Man in the middle) attack. Enter the IP address of the victim computer first and enter the router Ip address next.
If ctrl+c is pressed then the arp tables will revert back to normal.
5. Run ARP spoofing and packet sniffing together in different terminals.
