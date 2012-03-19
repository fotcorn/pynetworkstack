sudo brctl addbr br0
sudo brctl addif br0 eth0
sudo ifconfig eth0 0.0.0.0 promisc up
sudo ifconfig br0 192.168.2.230 netmask 255.255.255.0 broadcast 192.168.2.255
sudo route add default gw 192.168.2.1

sudo openvpn --mktun --dev tap0 --user corn --group corn
sudo brctl addif br0 tap0
sudo ifconfig tap0 0.0.0.0 promisc up






auto lo
iface lo inet loopback

auto eth0
iface eth0 inet manual

auto br0
iface br0 inet dhcp
        bridge_ports eth0
        bridge_stp off
        bridge_fd 0
        bridge_maxwait 0