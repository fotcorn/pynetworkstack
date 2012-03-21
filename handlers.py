from datastructs import EthernetFrame, Arp
from utils import ip_to_int

ARP_PROTOCOL = 0x806
IP_PROTOCOL = 0x800

mac_address = 1234
ip_address = '192.168.2.231'


class EthernetHandler(object):
    def recive(self, data):
        frame = EthernetFrame()
        frame.decode(data)
        if frame.protocol == IP_PROTOCOL:
            ip_handler(frame)
        elif frame.protocol == ARP_PROTOCOL:
            arp_handler.recive(frame)
    
    def send(self, payload, target_mac):
        pass

#################################

class ARPHandler(object):
    def recive(self, ethernet_frame):
        if ethernet_frame.target_ip == ip_address:
            arp_response = Arp()
            arp_response.hw_type = 1
            arp_response.proto_type = 0x800
            arp_response.hw_size = 6
            arp_response.proto_size = 4
            arp_response.opcode = 2
            arp_response.sender_mac = '???'
            arp_response.sender_ip = ip_to_int(ip_address)
            arp_response.target_mac = ethernet_frame.sender_mac
            arp_response.target_ip = ethernet_frame.sender_ip
            
            ethernet_handler.send(arp_response.encode(), ethernet_frame.sender_mac)
        

def ip_handler(ethernet_frame):
    pass

#######################

def icmp_handler(ip_frame):
    pass

def udp_handler(ip_frame):
    pass

def tcp_handler(ip_frame):
    pass


ethernet_handler = EthernetHandler()
arp_handler = ARPHandler()