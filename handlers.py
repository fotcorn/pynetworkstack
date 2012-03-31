from pynetstack.datastructs import EthernetFrame, ARPPacket, IPPacket,\
    ICMPPacket
from pynetstack.utils import int_to_ip

ARP_PROTOCOL = 0x806
IP_PROTOCOL = 0x800
ICMP_PROTOCOL = 0x01
UDP_PROTOCOL = 0x11
TCP_PROTOCOL = 0x06

mac_address = None
ip_address = None
write_callback = None

class EthernetHandler(object):
    
    def recive(self, data):
        frame = EthernetFrame()
        frame.decode(data)
        if frame.protocol == IP_PROTOCOL:
            ip_handler.recive(frame)
        elif frame.protocol == ARP_PROTOCOL:
            arp_handler.recive(frame)
        else:
            print '%s packet from %s to %s' % (hex(frame.protocol), hex(frame.source), hex(frame.destination))
    
    def send(self, payload, protocol, target_mac):
        frame = EthernetFrame()
        frame.source = mac_address
        frame.destination = target_mac
        frame.payload = payload
        frame.protocol = protocol
        write_callback(frame)
        
ethernet_handler = EthernetHandler()
#################################

class ARPHandler(object):
    def recive(self, ethernet_frame):
        
        
        arp_packet = ARPPacket()
        arp_packet.decode(ethernet_frame.payload)
        
        print 'arp packet from %s to %s (%s)' % (hex(ethernet_frame.source), hex(ethernet_frame.destination), int_to_ip(arp_packet.target_ip))
        
        if arp_packet.target_ip == ip_address:
            arp_response = ARPPacket()
            arp_response.hw_type = 1
            arp_response.proto_type = 0x800
            arp_response.hw_size = 6
            arp_response.proto_size = 4
            arp_response.opcode = 2
            arp_response.sender_mac = mac_address
            arp_response.sender_ip = ip_address
            arp_response.target_mac = arp_packet.sender_mac
            arp_response.target_ip = arp_packet.sender_ip
            
            ethernet_handler.send(arp_response.encode(), ARP_PROTOCOL, arp_packet.sender_mac)
arp_handler = ARPHandler()

class IPHandler():
    def recive(self, ethernet_frame):
        ip_packet = IPPacket()
        ip_packet.decode(ethernet_frame.payload)
        
        if ip_packet.destination == ip_address:
            if ip_packet.protocol == ICMP_PROTOCOL:
                icmp_handler.recive(ip_packet)
            elif ip_packet.protocol == TCP_PROTOCOL:
                tcp_handler.recive(ip_packet)
            elif ip_packet.protocol == UDP_PROTOCOL:
                udp_handler.recive(ip_packet)
        
    def send(self, payload, dest_ip):
        pass 
ip_handler = IPHandler()

#######################

class ICMPHandler():
    def recive(self, ip_packet):
        icmp_packet = ICMPPacket()
        icmp_packet.decode(ip_packet.payload)
        print 'icmp packet from %s to %s' % (int_to_ip(ip_packet.source), int_to_ip(ip_packet.destination))
        
icmp_handler = ICMPHandler()

class TCPHandler():
    def recive(self, ip_packet):
        print 'tcp packet from %s to %s' % (int_to_ip(ip_packet.source), int_to_ip(ip_packet.destination))
tcp_handler = TCPHandler()
    
class UDPHandler():
    def recive(self, ip_packet):
        print 'udp packet from %s to %s' % (int_to_ip(ip_packet.source), int_to_ip(ip_packet.destination))
udp_handler = UDPHandler()


