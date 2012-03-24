

def int_to_ip(i):
    return '%s.%s.%s.%s' % (
            (i & 0xFF000000) >> 24,
            (i & 0x00FF0000) >> 16,
            (i & 0x0000FF00) >> 8,
            (i & 0x000000FF))

def ip_to_int(ip):
    splits = ip.split('.')
    return ((int(splits[0]) << 24) + (int(splits[1]) << 16) + 
            (int(splits[2]) << 8) + (int(splits[3]) << 0))


# first 4 bytes, second 2 bytes
# usage: packet = struct.unpack('!IH', data)
# decode_mac(packet[0], packet[1])
def decode_mac(first, second):
    return first*65536 + second

# returns a touple (first_4_bytes, second_2_bytes)
# usage: struct.pack('!IH', *encode_mac(mac))
def encode_mac(mac_address):
    return (mac_address >> 16, mac_address & 0xFFFF)