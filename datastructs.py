import struct
from pynetstack.utils import int_to_ip, decode_mac, encode_mac

class EthernetFrame():
    source = destination = protocol = payload = None
    
    def decode(self, data):
        packet = struct.unpack('!IHIHH', data[:14])
        self.destination = decode_mac(packet[0], packet[1])
        self.source = decode_mac(packet[2], packet[3])
        self.protocol = packet[4]
        self.payload = data[14:]
    
    def encode(self):
        data = struct.pack('!IH', *encode_mac(self.destination))
        data += struct.pack('!IH', *encode_mac(self.source))
        data += struct.pack('!H', self.protocol)
        data += self.payload
        if len(data) < 60: # add trailer if packet to short
            data += '\0' * (60 - len(data))
        return data
    
    def __str__(self):
        return hex(self.protocol) + ': ' + hex(self.source) + ' -> ' + hex(self.destination)
    
class Arp():
    hw_type = proto_type = hw_size = proto_size = opcode = sender_mac = sender_ip = target_mac = target_ip = None
    
    def decode(self, data):
        if len(data) < 28:
            return None
        data = data[:28]
        packet = struct.unpack('!HHBBHIHIIHI', data)
        self.hw_type = packet[0]
        self.proto_type = packet[1]
        self.hw_size = packet[2]
        self.proto_size = packet[3]
        self.opcode = packet[4]
        self.sender_mac = decode_mac(packet[5], packet[6])
        self.sender_ip = packet[7]
        self.target_mac = decode_mac(packet[8], packet[9])
        self.target_ip = packet[10]

    def encode(self):
        data = struct.pack('!HHBBH', self.hw_type, self.proto_type, self.hw_size, self.proto_size, self.opcode)
        data += struct.pack('!IH', *encode_mac(self.sender_mac))
        data += struct.pack('!I', self.sender_ip)
        data += struct.pack('!IH', *encode_mac(self.target_mac))
        data += struct.pack('!I', self.target_ip)
        return data
    
    def __str__(self):
        return str(self.opcode) + ': ' + hex(self.sender_mac) + ' / ' + int_to_ip(self.sender_ip) + \
            ' -> ' + hex(self.target_mac) + ' / ' + int_to_ip(self.target_ip)
