#!/usr/bin/env python

import scapy.all as scapy

"""
    This method gives all the Mac address of 
    pc that are register on networks
    
"""


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:  # this loop will add all MAC address and add in client list varibale
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


"""
    This method prints the obtain mac Address in 
    readable pattern
"""


def print_result(results_list):
    print("IP\t\t\tMAC Address\n.....................................")
    for client in results_list:
        print(client)


if __name__ == "__main__":
    scan_result = scan("192.168.43.172")
    print_result(scan_result)

    print_result(scan("10.0.2.1/24"))
