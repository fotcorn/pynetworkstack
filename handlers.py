from datastructs import EthernetFrame, Arp
from utils import ip_to_int

ARP_PROTOCOL = 0x806
IP_PROTOCOL = 0x800

mac_address = None
ip_address = None


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
ethernet_handler = EthernetHandler()
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
            arp_response.sender_mac = mac_address
            arp_response.sender_ip = ip_address
            arp_response.target_mac = ethernet_frame.sender_mac
            arp_response.target_ip = ethernet_frame.sender_ip
            
            ethernet_handler.send(arp_response.encode(), ethernet_frame.sender_mac)
arp_handler = ARPHandler()

class IPHandler():
    def recive(self, ethernet_frame):
        pass
    
    def send(self, payload, dest_ip):
        pass 
ip_handler = IPHandler()

#######################

class ICMPHandler():
    def recive(self, ip_frame):
        pass
icmp_handler = ICMPHandler()

class TCPHandler():
    def recive(self, ip_frame):
        pass
tcp_handler = TCPHandler()
    
class UDPHandler():
    def recive(self, ip_frame):
        pass
udp_handler = UDPHandler()


