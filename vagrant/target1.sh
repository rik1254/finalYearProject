#! /bin/bash
# An 'out of the box' installation. 
adduser auditor
echo -e "p16036657\np16036657" | passwd auditor
echo "auditor ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers