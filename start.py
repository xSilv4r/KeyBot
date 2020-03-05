#!/usr/bin/env python3
import datetime
import os

from lib.data import *
from misc.banner import banner

def configGeneration():
    file_name = CONF_PATH/input("Enter configuration filename:\n")
    f = open("{}.conf".format(file_name), "w")
    print(file_name)
    l = input("Enter ip/range:\n")
    f.write("range = {}\n".format(l))
    l = input("Enter port/range:\n")
    f.write("ports = {}\n".format(l))
    l = input("Enter rate:\n")
    f.write("rate = {}\n".format(l))
    f.write("output-format = json\n")
    l = input("Enter output-filename (output will be in json format):\n")
    f.write("output-filename = {}.json\n".format(RECON_PATH/l))
    f.close()
    return file_name

def portScanner():
    file_name=configGeneration()
    cmd="masscan -c "
    cmd+="{}".format(file_name)
    cmd+=".conf --banners"
    os.system(cmd)


if __name__ == "__main__":
    banner()
    now = datetime.datetime.now()
    print("KeyBot starting at {}".format(now.isoformat()))
    portScanner()
    print("finished scan")