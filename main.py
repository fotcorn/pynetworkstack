import os
import struct

from fcntl import ioctl
from select import select
from binascii import hexlify

TUNSETIFF = 0x400454ca
SIOCGIFHWADDR = 0x8927
TAP_MODE = 0x0002

# connect to tap device
f = os.open("/dev/net/tun", os.O_RDWR)
ifs = ioctl(f, TUNSETIFF, struct.pack("16sH", "tap0", TAP_MODE))

# get generated mac address of tap device
ifr = 'tap0' + '\0' * 28
r = ioctl(f, SIOCGIFHWADDR, ifr)
mac_address = int(hexlify(r[18:24]), 16)



while True:
    select([f], [], [])[0][0]
    data = os.read(f, 1024)
    print hexlify(data)


