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


# Include the following to test more than 2 hosts
runuser -l auditor -c 'sshpass -p "p16036657" ssh-copy-id -o StrictHostKeyChecking=no auditor@192.168.2.113'
runuser -l auditor -c 'sshpass -p "p16036657" ssh-copy-id -o StrictHostKeyChecking=no auditor@192.168.2.114'
echo "192.168.2.113   target3.foo.local       target3" >> /etc/hosts
echo "192.168.2.114   target4.foo.local       target4" >> /etc/hosts



# Required during development
yum -y install git

# To replicate OSCAP testing
# sudo yum -y install openscap-scanner scap-security-guide
# sudo sed -i   -e 's|idref="cpe:/o:redhat:enterprise_linux|idref="cpe:/o:centos:centos|g'   -e 's|ref_id="cpe:/o:redhat:enterprise_linux|ref_id="cpe:/o:centos:centos|g'   /usr/share/xml/scap/ssg/content/ssg-rhel*.xml
# sudo oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_C2S --results-arf arf.xml --report report.html /usr/share/xml/scap/ssg/content/ssg-rhel7-ds.xml

# oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_C2S --results arf.xml /usr/share/xml/scap/ssg/content/ssg-rhel7-ds.xml
# oscap xccdf remediate --results arf.xml arf.xml