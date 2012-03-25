import struct
from pynetstack.utils import int_to_ip, decode_mac, encode_mac, net_checksum

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
    
class ARPPacket():
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

class IPPacket():
    
    version = header_length = tos = length = id = flags = ttl = protocol = header_checksum = source = destination = payload = None
    
    def decode(self, data):
        version_hl = struct.unpack('!B', data[0])[0]
        self.version =  (version_hl & 0xF0) >> 4
        self.header_length = (version_hl & 0x0F) * 4 # convert to num bytes
        
        header = data[1:self.header_length]
        packet = struct.unpack('!BHHHBBHII', header)
        
        self.tos = packet[0]
        self.length = packet[1]
        self.id = packet[2]
        self.flags = packet[3]
        self.ttl = packet[4]
        self.protocol = packet[5]
        self.header_checksum = packet[6]
        self.source = packet[7]
        self.destination = packet[8]
        self.payload = data[self.header_length:self.length]
                
    def encode(self):
        pass
    
    
class ICMPPacket():
    
    type = code = checksum = id = sequence_number = data = None
    
    
    def decode(self, data):
        packet = struct.unpack('!BBHHH', data[:8])
        self.type = packet[0]
        self.code = packet[1]
        self.checksum = packet[2]
        self.id = packet[3]
        self.sequence_number = packet[4]
        self.data = data[8:]
    
    def encode(self):
        data = struct.pack('!BBHHH', self.type, self.code, 0, self.id, self.sequence_number)
        data += self.data
        checksum = struct.pack('H', net_checksum(data))
        data = data[:2] + checksum + data[4:]
        return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    