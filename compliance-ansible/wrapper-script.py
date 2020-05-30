##################################
# Notes
# This is still under development and currently only works with the CIS
#     standard 2.2.0, which is hardcoded.
# A full release roadmap can be found within the design documentation.

##################################
#! /bin/python3

import os
import sys
import time
import subprocess
import datetime
import signal

from os import walk

# Used to identify the width of the console window and print banners
#     appropriately.
# It is not dynamic and is only set at runtime.
rows, columns = os.popen('stty size', 'r').read().split()

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)

##################################
# Start
# Starting screen for the application
# Presents a warning before use.
##################################

# Compliance Scanner
# P16036657
# CTEC3301


def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    section = '''
  _____                       _ _
 /  __ \                     | (_)
 | /  \/ ___  _ __ ___  _ __ | |_  __ _ _ __   ___ ___
 | |    / _ \| '_ ` _ \| '_ \| | |/ _` | '_ \ / __/ _ \\
 | \__/\ (_) | | | | | | |_) | | | (_| | | | | (_|  __/
  \____/\___/|_| |_| |_| .__/|_|_|\__,_|_| |_|\___\___|
 _____                 | |
/  ___|                |_|
\ `--.  ___ __ _ _ __  _ __   ___ _ __
 `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
/\__/ / (_| (_| | | | | | | |  __/ |
\____/ \___\__,_|_| |_|_| |_|\___|_|

             Created by:  Rikki Wright
             Module Code: CTEC3301 '''
# Font source: http://patorjk.com/software/taag/#p=display&f=Doom&t=Type%20Something%20

    banner(section)
    #time.sleep(0.5)

    section = '''
 _    _  ___  ______ _   _ _____ _   _ _____
| |  | |/ _ \ | ___ \ \ | |_   _| \ | |  __ \\
| |  | / /_\ \| |_/ /  \| | | | |  \| | |  \/
| |/\| |  _  ||    /| . ` | | | | . ` | | __
\  /\  / | | || |\ \| |\  |_| |_| |\  | |_\ \\
 \/  \/\_| |_/\_| \_\_| \_/\___/\_| \_/\____/

     Using this compliance scanner for automated remediation
     may cause irreversible damage to the target system.
     Please ensure systems are NOT production and all data
     is sufficiently backed up.'''

    banner(section)
    #time.sleep(1)
    mainMenu()

##################################
# Banner
# Generic banner function
##################################


def banner(section):

    print("*" * int(columns))
    print(f"{section}")
    print("*" * int(columns))

##################################
# Main menu
# Main menu for the application
##################################


def mainMenu():
    section = "Main Menu"
    banner(section)

    selection = input("""
                A: New Scan
                B: View Installed Modules
                C: Setup Guide
                D: Help
                Q: Quit/Log Out

                Please enter your choice: """)

    # Forces input to lowercase so user can enter A or a and still work.
    if selection.lower() == "a":
        verifyScan()
    elif selection.lower() == "b":
        installedModules()
    elif selection.lower() == "c":
        guide()
    elif selection.lower() == "d":
        instructions()
    elif selection.lower() == "q" or selection.lower() == "quit":
        sys.exit
    else:
        print("\n\nPlease select a listed option.\n")
        print("Please try again\n\n")
        time.sleep(0.5)
        mainMenu()

##################################
# To main menu or quit
# Menu used to exit non-interactive pages
##################################


def menuOrQuit():
    print("What would you like to do?")
    selection = input('''
                A: To main menu
                Q: Quit

                Please enter your choice: ''')

    # Forces input to lowercase so user can enter A or a and still work.
    if selection.lower() == "a":
        os.system('cls' if os.name == 'nt' else 'clear')
        mainMenu()
    elif selection.lower() == "q" or selection.lower() == "quit":
        sys.exit
    else:
        print("\n\nPlease select a listed option.\n")
        print("Please try again\n\n")
        time.sleep(0.5)
        menuOrQuit()


##################################
# Setup Guide
# Setup guide to explain how to configure the application
##################################
def guide():
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Guide"
    banner(section)

    guide = '''
        Guide
        1. Define the list of hosts to use for this scan.
           *** This version uses a predefined host list which can be changed
               at ./customer/inventory
        2.
        \n\n\n\n
        '''

    print(guide)

    menuOrQuit()


##################################
# Instructions
# Instructions and help for how to use the application
##################################
def instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Instructions"
    banner(section)

    instructions = '''
        New Scan:
            A new scan will initiate the scanning process. A prompt will guide
            the process including the customer name and scan type.

            Scan Type:
                This application will perform both an initial audit and
                remediation. The remediation will take approximately twice as
                long to ensure patches are applied.

        View Installed Modules:
            This application will be able to accept multiple modules if the
            appropriate Ansible playbooks are provided and stored in the
            correct location.

                Ansible:
                    Ansible is a configuration management and application
                    deployment tool. It is used within this application to
                    perform the audit and remediation steps.

        Help:
            Presents this screen.

        Quit:
            Exits the application. Entering 'q' or 'quit' at any prompt will
            exit the application.
        \n\n\n\n
        '''

    print(instructions)

    menuOrQuit()


##################################
# Installed modules
# Lists all installed modules
##################################
def installedModules():
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Installed Modules"
    banner(section)

    installed_modules = '''
        Currently installed modules.
        '''

    print("This section is currently unavailable\n")

    menuOrQuit()


##################################
# Verify Scan
# Verifies users have correctly configured the application
##################################
def verifyScan():
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Start Scan"
    banner(section)

    print("Have you followed the setup guide?")
    selection = input('''
                Y: Yes
                N: No
                Q: Quit

                Please enter your choice: ''')

    # Forces input to lowercase so user can enter A or a and still work.
    if selection.lower() == "y" or selection.lower() == "yes":
        scan('', '')

    elif selection.lower() == "n" or selection.lower() == "no":
        guide()

    elif selection.lower() == "q" or selection.lower() == "quit":
        sys.exit

    else:
        print("\n\nPlease select a listed option.\n")
        print("Please try again\n\n")
        time.sleep(0.5)
        verifyScan()


##################################
# Scan
# Initiates a new scan. Options of audit or remediation
##################################
def scan(scan_type, customer):
    print(f'{customer,scan_type}')
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Start Scan"
    banner(section)

    if scan_type == '':
        customer = input("Please enter a customer name: \n")
        customer = sanitiseInput(customer)
        selection = input('''
                        A: Audit
                        R: Remediation
                        Q: Quit

                        Please enter your choice: ''')

        if selection.lower() == "a" or selection.lower() == "audit":
            scan("audit", customer)
        elif selection.lower() == "r" or selection.lower() == "remediation":
            scan("remediation", customer)
        elif selection.lower() == "q" or selection.lower() == "quit":
            sys.exit
        else:
            print("\n\nPlease select a listed option.\n")
            print("Restarting scan journey\n\n")
            time.sleep(1)
            selection = ''
            scan('', '')

    else:
        if scan_type == "audit":
            #Run command with --check
            #command = f'ansible-playbook playbooks/cis_2.2.0/cis_2.2.0-test.yml '\
                #f'--check -e customer={customer} -e scan_type={scan_type}'
            command = f'ansible-playbook playbooks/cis_2.2.0/cis_2.2.0.yml '\
                f'--check -e customer={customer} -e scan_type={scan_type}'
            os.system(command)
            generateResults(customer, scan_type)

        else:
            #Run command without --check
            #command = f'ansible-playbook playbooks/cis_2.2.0/cis_2.2.0-test.yml '\
                #f'-e customer={customer} -e scan_type={scan_type}'
            command = f'ansible-playbook playbooks/cis_2.2.0/cis_2.2.0.yml '\
                f'-e customer={customer} -e scan_type={scan_type}'

            # Runs remediation scan twice. First to make changes, second to confirm changes
            os.system(command)
            os.system(command)
            generateResults(customer, scan_type)


##################################
# Generate results
# Complies ansible results and outputs in simple format
##################################
def generateResults(customer, scan_type):

    # Clears terminal and creates banner
    os.system('cls' if os.name == 'nt' else 'clear')
    section = "Results"
    banner(section)

    # Creates Scanner results file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
    file_name = f'{customer}-{scan_type}-{timestamp}.txt'

    # Opens Ansible generated results files
    results = os.listdir("playbooks/cis_2.2.0/results/")
    cust_scan = f'{customer}-{scan_type}-'
    count = 0
    hosts = []

    # Identifies hostnames
    for x in range(len(results)):
        if cust_scan in results[x]:
            hosts.append(results[x].replace(cust_scan, '').replace('.txt', ''))
        else:
            continue

    # Reads identified files by hostname
    for x in range(len(hosts)):
        host = hosts[x]
        with open(f'playbooks/cis_2.2.0/results/{cust_scan}{host}.txt') as f:
            lines = f.read().splitlines()

        # Temporary array to hold failed results
        tmp_array = []
        for line in lines:
            tmp_array.append(line.strip().split(' ', 1))
        tmp_array.pop(0)

        for x in range(len(tmp_array)):
            checks = len(tmp_array)
            if tmp_array[x][1] == "failed":
                count += 1
            else:
                continue

        # Calculates compliance score based on results
        compliance = round((100 - ((100/int(checks)) * int(count))), 2)

        # Outputs results to a file and screen
        f = open(f'audit-results/{file_name}', "a+")
        f.write(f'{host} is {compliance}% compliant. It has failed {count} of {checks} tasks.\n')
        f.close
        print(f'Check type: {scan_type}. {host} is {compliance}%'
              f' compliant. It has failed {count} of {checks} tasks.')

        count = 0

    print(f'\n\nFile for this scan can be found here: ./audit-results/{file_name}')

    # Asks user to run remediation scan IF the type is an audit
    if scan_type == "audit":
        remediationMenu("Do you want to run the remediation process?", customer, "remediation")
    else:
        sys.exit


##################################
# Generic menu to accept or quit
##################################
def remediationMenu(text, customer, scan_type):
    selection = input('''
                Y: Yes
                N: No (This will terminate the application)

                Please enter your choice: ''')

    # Forces input to lowercase so user can enter A or a and still work.
    if selection.lower() == "y" or selection.lower() == "yes":
        scan(scan_type, customer)
    elif selection.lower() == "n" or selection.lower() == "no":
        sys.exit
    else:
        print("\n\nPlease select a listed option.\n")
        print("Please try again\n\n")
        time.sleep(0.5)
        remediationMenu(text, customer, scan_type)


##################################
# Sanitise user input
##################################
def sanitiseInput(input):
    input = input.replace(' ', '_')
    char = ['\\', '`', '*', '{', '}', '[', ']', '(', ')', '<',
            '>', '#', '+', '!', '$', '\'', '\"']

    for ch in char:
        input = input.replace(ch, '')
    return(input)


##################################
# Start application
##################################
start()
