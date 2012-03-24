from binascii import hexlify, unhexlify

from pynetstack.datastructs import EthernetFrame
from pynetstack.tests.utils import print_object




data = unhexlify('ffffffffffff14dae94c72670806000108000604000114dae94c7267c0a80266000000000000c0a802fa000000000000000000000000000000000000')



frame = EthernetFrame()
frame.decode(data)

print_object(frame)


encoded = frame.encode()
print hexlify(encoded)

if data == encoded:
    print 'encoding ok'
else:
    print 'encoding failed'
