#!/usr/bin/env python
import subprocess

interface = input("interface > ")
new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# This code executes additional commands that are seperated by a semi-colon
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)