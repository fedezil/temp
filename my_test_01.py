#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to set the primary, secondary and tertiary WLC names and IPs
after retrieving all the APs of a Catalyst 9800 Wireless Controller"""


# Imports
import re


# Collect and verify format for Primary WLC name and IP
primaryWlcName = input("\nPrimary WLC name: ")

while not re.match(".*[a-zA-Z0-9\.\-\_].*", primaryWlcName): # Accepting characters, numbers, and some special characters ('.', '-' and '_')
    primaryWlcName = input("Name not in a valid format. Please re-enter the primary WLC name: ")

primaryWlcIp = input("Primary WLC IP: ")

while not re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", primaryWlcIp):
    primaryWlcIp = input("IP address not valid. Please re-enter the primary WLC IP: ")

# Collect and verify format for Secondary WLC name and IP
secondaryWlcName = input("\nSecondary WLC name (press Enter to skip): ")

if len(secondaryWlcName) == 0: # If secondary WLC name is not specified, then automatically set name to 'null' and IP to '0.0.0.0' for both secondary and tertiary WLCs
    secondaryWlcName = "null"
    secondaryWlcIp = "0.0.0.0"
    tertiaryWlcName = "null"
    tertiaryWlcIp = "0.0.0.0"

else:
    while not re.match(".*[a-zA-Z0-9\.\-\_].*", secondaryWlcName): # Accepting characters, numbers, and some special characters ('.', '-' and '_')
        secondaryWlcName = input("Name not in a valid format. Please re-enter the secondary WLC name: ")

    secondaryWlcIp = input("Secondary WLC IP: ")

    while not re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", secondaryWlcIp):
        secondaryWlcIp = input("IP address not valid. Please re-enter the secondary WLC IP: ")

    # Collect and verify format for Tertiary WLC name and IP
    tertiaryWlcName = input("\nTertiary WLC name (press Enter to skip): ")

    if len(tertiaryWlcName) == 0: # If tertiary WLC name is not specified, then automatically set name to 'null' and IP to '0.0.0.0' for the tertiary WLC
        tertiaryWlcName = "null"
        tertiaryWlcIp = "0.0.0.0"

    else:
        while not re.match(".*[a-zA-Z0-9\.\-\_].*", tertiaryWlcName): # Accepting characters, numbers, and some special characters ('.', '-' and '_')
            tertiaryWlcName = input("Name not in a valid format. Please re-enter the tertiary WLC name: ")

        tertiaryWlcIp = input("Tertiary WLC IP: ")

        while not re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", tertiaryWlcIp):
            tertiaryWlcIp = input("IP address not valid. Please re-enter the tertiary WLC IP: ")

# Print a summary of the settings to be pushed and ask the end user for a confirmation
if secondaryWlcName == "null":
    print("""
    The script will set the primary WLC name and IP to the following:

    Primary WLC name: {}
    Primary WLC IP: {}
    """.format(primaryWlcName, primaryWlcIp))

elif tertiaryWlcName == "null":
    print("""
    The script will set primary and secondary WLC names and IPs to the following:

    Primary WLC name: {}
    Primary WLC IP: {}

    Secondary WLC name: {}
    Secondary WLC IP: {}
    """.format(primaryWlcName, primaryWlcIp, secondaryWlcName, secondaryWlcIp))

else:
    print("""
    The script will set the primary, secondary and tertiary WLC names and IPs to the following:

    Primary WLC name: {}
    Primary WLC IP: {}

    Secondary WLC name: {}
    Secondary WLC IP: {}

    Tertiary WLC name: {}
    Tertiary WLC IP: {}
    """.format(primaryWlcName, primaryWlcIp, secondaryWlcName, secondaryWlcIp, tertiaryWlcName, tertiaryWlcIp))

answer = input("Are you ok with these changes? (yes/no) ")

if re.match("no", answer, re.IGNORECASE):
    print("\nThank you, the script will stop here.\n")
