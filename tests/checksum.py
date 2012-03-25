from pynetstack.utils import internet_checksum
from pynetstack.tests.data import icmp_packet
from binascii import hexlify, unhexlify

icmp_packet = unhexlify(icmp_packet)

checksum = icmp_packet[2:4]

print 'excepted checksum: %s' % hexlify(checksum)

data = icmp_packet[:2] + '\0' * 2 + icmp_packet[4:]

res = internet_checksum(data)
if res == checksum:
    print 'checksum ok'
else:
    print 'checksum wrong'

