sudo service network-manager stop
sudo sysctl -w net.ipv4.ip_forward=1
sudo brctl addbr br0
sudo brctl addif br0 eth0
sudo ifconfig eth0 0.0.0.0 promisc up
sudo ifconfig br0 192.168.2.230 netmask 255.255.255.0 broadcast 192.168.2.255
sudo route add default gw 192.168.2.1

sudo openvpn --mktun --dev tap0 --user corn --group corn
sudo brctl addif br0 tap0
sudo ifconfig tap0 0.0.0.0 promisc up
