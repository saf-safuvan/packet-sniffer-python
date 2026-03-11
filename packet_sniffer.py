from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

print("Starting packet sniffing...")

sniff(prn=packet_callback, count=20)
