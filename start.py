#!/usr/bin/env python3
from time import ctime
import subprocess

from lib.data import *
from lib.recon import version_detection
from lib.loader import loadModule, loadPayloads, loadTargets
from lib.pocengine import run, output2file
from misc.banner import banner
from lib.data import fg_colors

def config_generation():
    config_filename = CONF_PATH/input("%s[-]%s Enter configuration filename:\n"%(fg_colors.blue,fg_colors.reset))
    f = open("{}.conf".format(config_filename), "w")
    l = input("%s[-]%s Enter ip/range:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("range = {}\n".format(l))
    l = input("%s[-]%s Enter port/range:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("ports = {}\n".format(l))
    l = input("%s[-]%s Enter rate:\n"%(fg_colors.blue,fg_colors.reset))
    f.write("rate = {}\n".format(l))
    f.write("output-format = json\n")
    l = input("%s[-]%s Enter output-filename (output will be in json format):\n"%(fg_colors.blue,fg_colors.reset))
    output_filename = RECON_PATH/l
    f.write("output-filename = {}.json\n".format(output_filename))
    f.close()
    return config_filename,output_filename

def port_scanner(config_filename,output_filename):
    print("[!] Starting port scan.")
    subprocess.run(["masscan","-c","{}.conf".format(config_filename)], stdout=subprocess.DEVNULL)
    print("%s[+]%s Port scanning done."%(fg_colors.lightgreen,fg_colors.reset))
    print("[!] Starting port probing.")
    version_detection(output_filename)
    print("[+] Port probing done.")
    print("[!] Starting POC engine.")
    loadTargets()
    loadPayloads()
    run()
    #print("[+] Saving output.")
    #output2file()


def menu():
    print("%sStarting KeyBot at {}%s\n".format(ctime())%(fg_colors.red,fg_colors.reset))
    print('''%sMenu :%s
%s[1]%s Scan from existing configuration.
%s[2]%s Create new configuration.'''%(fg_colors.green,fg_colors.reset,
                                      fg_colors.blue,fg_colors.reset,
                                      fg_colors.blue,fg_colors.reset,))
    choice = input()
    if choice == '1':
        config_filename = CONF_PATH/input("%s[-]%sEnter configuration filename\n"%(fg_colors.blue,fg_colors.reset))
        with open('{}.conf'.format(config_filename), 'r') as f:
            for line in f:
                if line.find("output/recon_output/") != -1:
                    x = line.rpartition('/')
                    output_filename = RECON_PATH/x[2].strip()
        port_scanner(config_filename,output_filename)
    if choice == '2':
        config_filename,output_filename=config_generation()
        port_scanner(config_filename,output_filename)

        
if __name__ == "__main__":
    banner()
    menu()
