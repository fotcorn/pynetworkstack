import os
import struct

from fcntl import ioctl
from select import select
from binascii import hexlify

TUNSETIFF = 0x400454ca
TAP_MODE = 0x0002


f = os.open("/dev/net/tun", os.O_RDWR)
ifs = ioctl(f, TUNSETIFF, struct.pack("16sH", "tap0", TAP_MODE))

while True:
    select([f], [], [])[0][0]
    data = os.read(f, 1024)
    print hexlify(data)



