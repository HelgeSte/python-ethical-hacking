#!/usr/bin/env python
import subprocess

interface = "eth0"
new_mac = "00:22:22:33:69:69"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# This code executes additional commands that are seperated by a semi-colon
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface, shell=True)