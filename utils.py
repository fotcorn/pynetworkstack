

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

