from binascii import unhexlify

from pynetstack.datastructs import IPPacket
from pynetstack.tests.utils import print_object
from datastructs import EthernetFrame


data = unhexlify('002129994adce4115b2ca6d8080045000034e3084000400627bac0a80274cc02a0e2c7f100505b5ae554ee9f1067801007c7302800000101080a0008715f3ab2baa3')

ethernet_frame = EthernetFrame()
ethernet_frame.decode(data)

print_object(ethernet_frame)

packet = IPPacket()
packet.decode(ethernet_frame.payload)


print_object(packet)

"""
encoded = frame.encode()

if ethernet_frame.payload[:28] == encoded:
    print 'encoding ok'
else:
    print 'encoding failed'
"""