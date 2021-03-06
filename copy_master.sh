#!/bin/bash
OS_LATEST=$(ls -lat /home/ec2-user/opensanctions/data/json | head -2 | tail -1 | awk '{print $9}')
echo $OS_LATEST
cp /home/ec2-user/opensanctions/data/json/$OS_LATEST /var/opensanctions/master.json
rm -f /var/opensanctions/master.zip && zip -j /var/opensanctions/master.zip /var/opensanctions/master.json
scp -P 23000 /var/opensanctions/master.zip Swiftdfeed@agilertech.com:/home/Swiftdfeed/opensanctions/master.zip
ls -d -1 /home/ec2-user/opensanctions/data/json/*.* | grep -v $OS_LATEST | xargs sudo rm
