from pynetstack.datastructs import EthernetFrame, Arp

ARP_PROTOCOL = 0x806
IP_PROTOCOL = 0x800

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
        print 'arp packet from %s to %s' % (hex(ethernet_frame.source), hex(ethernet_frame.destination))
        
        arp_packet = Arp()
        arp_packet.decode(ethernet_frame.payload)
        
        if arp_packet.target_ip == ip_address:
            arp_response = Arp()
            arp_response.hw_type = 1
            arp_response.proto_type = 0x800
            arp_response.hw_size = 6
            arp_response.proto_size = 4
            arp_response.opcode = 2
            arp_response.sender_mac = mac_address
            arp_response.sender_ip = ip_address
            arp_response.target_mac = arp_packet.sender_mac
            arp_response.target_ip = arp_packet.sender_ip
            
            ethernet_handler.send(arp_response.encode(), ethernet_frame.sender_mac, ARP_PROTOCOL)
arp_handler = ARPHandler()

class IPHandler():
    def recive(self, ethernet_frame):
        print 'ip packet from %s to %s' % (ethernet_frame.source, ethernet_frame.destination)
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


