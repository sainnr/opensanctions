#!/bin/bash
OS_LATEST=$(ls -lat /home/ec2-user/opensanctions/data/json | head -2 | tail -1 | awk '{print $9}')
echo $OS_LATEST
scp -P 23000 /home/ec2-user/opensanctions/data/json/$OS_LATEST Swiftdfeed@agilertech.com:/home/Swiftdfeed/opensanctions
