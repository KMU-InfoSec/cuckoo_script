# install python libraries (cuckoo sandbox on Ubuntu/Debian-based distributions)
sudo apt-get install python python-pip python-dev libffi-dev libssl-dev
sudo apt-get install python-virtualenv python-setuptools
sudo apt-get install libjpeg-dev zlib1g-dev swig

# install mongodb
sudo apt-get install mongodb

# install virtualbox
sudo apt-get install virtualbox

# install tcpdump
sudo apt-get install tcpdump apparmor-utils
sudo aa-disable /usr/sbin/tcpdump

sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump

sudo pip install m2crypto

# add user "cuckoo"
sudo adduser cuckoo
sudo usermod -a -G vboxusers cuckoo

# install cuckoo
sudo pip install -U setuptools
sudo pip install -U cuckoo

cuckoo --cwd cuckoo
cuckoo community