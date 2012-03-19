from binascii import unhexlify
import struct

from datastructs import EthernetFrame



def parse_ethernet_frame(data):
    frame = EthernetFrame()
    packet = struct.unpack('!IIHIHH', data[:18])
    frame.protocol = packet[0]
    frame.destination = packet[1]*65536 + packet[2]
    frame.source = packet[3]*65536 + packet[4]
    frame.data = data[:18]
    return frame


data = unhexlify('00000806ffffffffffffe4115b2ca6d808060001080006040001e4115b2ca6d8c0a802e6000000000000c0a802e7')

print parse_ethernet_frame(data)