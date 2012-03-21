import struct
from utils import int_to_ip

class EthernetFrame():
    source = destination = protocol = payload = None
    
    def decode(self, data):
        packet = struct.unpack('!IHIHH', data[:14])
        self.destination = packet[0]*65536 + packet[1]
        self.source = packet[2]*65536 + packet[3]
        self.protocol = packet[4]
        self.payload = data[14:]
    
    def encode(self):
        return ''
    
    def __str__(self):
        return hex(self.protocol) + ': ' + hex(self.source) + ' -> ' + hex(self.destination)
    
class Arp():
    hw_type = proto_type = hw_size = proto_size = opcode = sender_mac = sender_ip = target_mac = target_ip = None
    
    def decode(self, data):
        packet = struct.unpack('!HHBBHIHIIHI', data)
        self.hw_type = packet[0]
        self.proto_type = packet[1]
        self.hw_size = packet[2]
        self.proto_size = packet[3]
        self.opcode = packet[4]
        self.sender_mac = packet[5]*65536 + packet[6]
        self.sender_ip = packet[7]
        self.target_mac = packet[8]*65536 + packet[9]
        self.target_ip = packet[10]

    def encode(self):
        return ''
    
    def __str__(self):
        return str(self.opcode) + ': ' + hex(self.sender_mac) + ' / ' + int_to_ip(self.sender_ip) + \
            ' -> ' + hex(self.target_mac) + ' / ' + int_to_ip(self.target_ip)
