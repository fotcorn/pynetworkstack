from binascii import unhexlify
import struct

from pynetstack.datastructs import EthernetFrame, Arp
from pynetstack.utils import ip_to_int

data = unhexlify('00000806ffffffffffffe4115b2ca6d808060001080006040001e4115b2ca6d8c0a802e6000000000000c0a802e7')

ethernet_frame = EthernetFrame()
ethernet_frame.decode(data[4:])

protocols = { 0x806: Arp }


if ethernet_frame.protocol in protocols:
    protocol_frame = protocols[ethernet_frame.protocol]()
    protocol_frame.decode(ethernet_frame.payload)

    arp_response = Arp()
    arp_response.hw_type = 1
    arp_response.proto_type = 0x800
    arp_response.hw_size = 6
    arp_response.proto_size = 4
    arp_response.opcode = 2
    arp_response.sender_mac = '???'
    arp_response.sender_ip = ip_to_int('192.168.2.231')
    arp_response.target_mac = protocol_frame.sender_mac
    arp_response.target_ip = protocol_frame.sender_ip
