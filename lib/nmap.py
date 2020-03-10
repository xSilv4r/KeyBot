#!/usr/bin/env python3
import os
import json

from data import RECON_PATH

def parser():
    OBJECT = {
    "192.168.8.1" : [80,20,22],
    "192.168.8.2" : [22,21],
    "192.168.8.3" : [443]
    }

    for key,value in OBJECT.items():
        open_ports=""
        print(key)
        for i in range(len(value)):
            open_ports+="{},".format(value[i])

        version_detection(key,open_ports)    


def version_detection(ip,open_ports):
    cmd="nmap -sVC " #version detection
    cmd+=str(ip)
    cmd+=" -p {}".format(open_ports)
    cmd+=" --open" #show only open ports
    cmd+=" -Pn" #skip host discovery
    cmd+=" -n" #no dns resolution
    cmd+=" -T4" #timing template
    #cmd+=" -oX {}".scan_output #output file
    os.system(cmd)
    #cmd="rm {}".RECON_PATH/scan_output
    print("Version detection done.")

parser()