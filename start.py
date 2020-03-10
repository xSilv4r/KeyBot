#!/usr/bin/env python3
from time import ctime
import os

from lib.data import *
from misc.banner import banner
from lib.data import fg_colors

def configGeneration():
    file_name = CONF_PATH/input("%s[-]%s Enter configuration filename:\n"%(fg_colors.blue,fg_colors.reset))
    f = open("{}.conf".format(file_name), "w")
    print(file_name)
    l = input("%s[-]%s Enter ip/range:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("range = {}\n".format(l))
    l = input("%s[-]%s Enter port/range:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("ports = {}\n".format(l))
    l = input("%s[-]%s Enter rate:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("rate = {}\n".format(l))
    f.write("output-format = json\n")
    l = input("%s[-]%s Enter output-filename (output will be in json format):\n"%(fg_colors.blue,fg_colors.reset))
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
    print("%sStarting KeyBot at {}%s\n".format(ctime())%(fg_colors.red,fg_colors.reset))
    portScanner()
    print("finished scan")