#!/usr/bi/env python

import subprocess
import optparse
import re


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC address to add to the interface")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    pattern = r"(\w\w:){5}\w\w"
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # The following causes TypeError (string on a bytes-like object error)
    # mac_address_search_result = re.search(pattern, ifconfig_result) # Causes TypeError (string on a bytes-like object error)
    mac_address_search_result = re.search(pattern, str(ifconfig_result)) # Fixes TypeError

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


def main():
    options = get_argument()
    interface = options.interface
    new_mac = options.new_mac

    original_mac = get_current_mac(interface)
    if options.new_mac != original_mac:
        print("Changing MAC address")
        change_mac(interface, new_mac)
    else:
        print("No need to change MAC address, since it already got the correct address.")
    current_mac = get_current_mac(interface)
    if current_mac == new_mac:
        print("The MAC for " + interface + " is equal to the argument " + new_mac)
    else:
        print(new_mac + " != " + current_mac)


if __name__ == "__main__":
    main()

