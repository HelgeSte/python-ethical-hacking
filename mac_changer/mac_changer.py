#!/usr/bin/env python

import subprocess # kinda like system in Perl

subprocess.call("ifconfig eth0", shell=True)
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig eth0", shell=True)
# shell=True, so that we can run shell commands true this function
