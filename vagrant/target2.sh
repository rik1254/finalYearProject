#! /bin/bash
# This script is used to configure the "uncompliant" machine.
adduser auditor
echo -e "p16036657\np16036657" | passwd auditor
echo "auditor ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

yum -y install prelink
yum -y install setroubleshoot
yum -y install msctrans
yum -y install xorg-x11*
yum -y install ypbind
yum -y install rsh
yum -y install talk
yum -y install telnet
yum -y install openldap-clients