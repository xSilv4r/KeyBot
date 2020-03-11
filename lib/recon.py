#!/usr/bin/env python3
import os
import json
import subprocess 
import ast 

from lib.data import fg_colors
from lib.data import RECON_PATH

def version_detection(output_filename):
    proc = subprocess.run(
    args = ["/bin/bash", "./lib/bash.sh", "{}.json".format(output_filename)],
    universal_newlines = False,
    stdout = subprocess.PIPE)
    OBJECT=proc.stdout.decode("utf-8")
    OBJECT = ast.literal_eval(OBJECT) 

    for key,value in OBJECT.items():
        open_ports=""
        print(key)
        for i in range(len(value)):
            open_ports+="{},".format(value[i])

        nmap(key,open_ports)

    print("%s[+]%s Version detection done."%(fg_colors.lightgreen,fg_colors.reset))
    cmd="rm {}.json".format(output_filename)
    os.system(cmd)  


def nmap(ip,open_ports):
    cmd="nmap -sVC " #version detection
    cmd+=str(ip)
    cmd+=" -p {}".format(open_ports)
    cmd+=" --open" #show only open ports
    cmd+=" -Pn" #skip host discovery
    cmd+=" -n" #no dns resolution
    cmd+=" -T4" #timing template
    cmd+=" -oX {}".format(RECON_PATH/ip) #output file
    os.system(cmd)
