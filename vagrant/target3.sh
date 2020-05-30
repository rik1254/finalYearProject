# An 'out of the box' installation. 
# Some configuration changes may exist due to the use of pre-configured vagrant boxes.
adduser auditor
echo -e "p16036657\np16036657" | passwd auditor
echo "auditor ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers