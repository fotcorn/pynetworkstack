from binascii import unhexlify

from pynetstack.datastructs import ARPPacket
from pynetstack.tests.utils import print_object
from datastructs import EthernetFrame


data = unhexlify('ffffffffffff14dae94c72670806000108000604000114dae94c7267c0a80266000000000000c0a802fa000000000000000000000000000000000000')

ethernet_frame = EthernetFrame()
ethernet_frame.decode(data)

frame = ARPPacket()
frame.decode(ethernet_frame.payload)

print_object(frame)

encoded = frame.encode()

if ethernet_frame.payload[:28] == encoded:
    print 'encoding ok'
else:
    print 'encoding failed'
