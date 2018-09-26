echo "Guest Routing Start"
iptables -t nat -A POSTROUTING -o eno1np0 -s 192.168.56.0/24 -j MASQUERADE
iptables -P FORWARD DROP
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -s 192.168.56.0/24 -j ACCEPT
iptables -A FORWARD -s 192.168.56.0/24 -d 192.168.56.0/24 -j ACCEPT
echo 1 | tee -a /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1
echo "Guest Routing Complete"

