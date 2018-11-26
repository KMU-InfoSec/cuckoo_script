#!/bin/sh

# install python libraries (cuckoo sandbox on Ubuntu/Debian-based distributions)
apt-get install python python-pip python-dev libffi-dev libssl-dev -y
apt-get install python-virtualenv python-setuptools -y
apt-get install libjpeg-dev zlib1g-dev swig -y

# install mongodb
apt-get install mongodb -y

# install virtualbox
apt-get install virtualbox -y

# install tcpdump
apt-get install tcpdump apparmor-utils -y
sudo aa-disable /usr/sbin/tcpdump

sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump

pip install m2crypto

# add user "cuckoo"
sudo adduser cuckoo
sudo usermod -a -G vboxusers cuckoo

# install cuckoo
pip install -U setuptools
pip install -U cuckoo

cuckoo --cwd cuckoo
cuckoo community
