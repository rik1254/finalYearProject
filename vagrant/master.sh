#! /bin/bash
# Prerequisite software to run the application
yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y install python2-pip
yum -y install python3
yum -y install ansible


# A user is required for ansible. This user will be allocated to the "wheel" group and SSH keys shared
adduser auditor
echo -e "p16036657\np16036657" | passwd auditor
echo "auditor ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
runuser -l auditor -c 'ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N ""'
runuser -l auditor -c 'sshpass -p "p16036657" ssh-copy-id -o StrictHostKeyChecking=no auditor@192.168.2.111'
runuser -l auditor -c 'sshpass -p "p16036657" ssh-copy-id -o StrictHostKeyChecking=no auditor@192.168.2.112'

# Only use if a DNS server isn't available
echo "192.168.2.111   target1.foo.local       target1" >> /etc/hosts
echo "192.168.2.112   target2.foo.local       target2" >> /etc/hosts


# Required during development
# Can be used to clone finalYearProject repo for easy access to code
#yum -y install git

