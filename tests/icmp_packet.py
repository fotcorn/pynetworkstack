from binascii import unhexlify

from pynetstack.datastructs import EthernetFrame, IPPacket, ICMPPacket
from pynetstack.tests.data import ping_request
from pynetstack.tests.utils import print_object


data = unhexlify(ping_request)

ethernet_frame = EthernetFrame()
ethernet_frame.decode(data)

ip_packet = IPPacket()
ip_packet.decode(ethernet_frame.payload)

packet = ICMPPacket()
packet.decode(ip_packet.payload)

print_object(packet)