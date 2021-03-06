import os
import struct

from fcntl import ioctl
from select import select
from binascii import hexlify

from pynetstack import handlers
from pynetstack.utils import ip_to_int

TUNSETIFF = 0x400454ca
SIOCGIFHWADDR = 0x8927
TAP_MODE = 0x0002

# connect to tap device
f = os.open("/dev/net/tun", os.O_RDWR)
ifs = ioctl(f, TUNSETIFF, struct.pack("16sH", "tap0", TAP_MODE))

def write_callback(ethernet_frame):
    os.write(f, struct.pack('I', ethernet_frame.protocol) + ethernet_frame.encode())
    
# get generated mac address of tap device
ifr = 'tap0' + '\0' * 28
r = ioctl(f, SIOCGIFHWADDR, ifr)
handlers.mac_address = int(hexlify(r[18:24]), 16)

handlers.ip_address = ip_to_int('192.168.2.231')

handlers.write_callback = write_callback


while True:
    select([f], [], [])[0][0]
    data = os.read(f, 1024)
    handlers.ethernet_handler.recive(data[4:])

