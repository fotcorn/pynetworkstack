from binascii import unhexlify
import struct

from datastructs import EthernetFrame, Arp


data = unhexlify('00000806ffffffffffffe4115b2ca6d808060001080006040001e4115b2ca6d8c0a802e6000000000000c0a802e7')

ethernet_frame = EthernetFrame()
ethernet_frame.decode(data[4:])

protocols = { 0x806: Arp }


if ethernet_frame.protocol in protocols:
    protocol_frame = protocols[ethernet_frame.protocol]()
    protocol_frame.decode(ethernet_frame.payload)
    
    