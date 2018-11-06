#! /bin/bash

vboxmanage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1
sudo cuckoo &
sleep 20
sudo cuckoo process instance1 & sudo cuckoo process instance2 & sudo cuckoo process instance3 & sudo cuckoo process instance4 & sudo cuckoo process instance5 & sudo cuckoo process instance6 &
sudo cuckoo web -H localhost -p 8080 & sudo cuckoo api -H localhost -p 8090
#sudo rm -rf /home/wins/tasklist.pickle
#sudo /usr/sbin/cron

