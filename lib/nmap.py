import os

from lib.data import RECON_PATH

def version_detection(scan_output):
    open_ports
    nmap_targets
    cmd="nmap -sVC" #version detection
    cmd=+" -p {}".open_ports
    cmd+=" --open" #show only open ports
    cmd+=" -Pn" #skip host discovery
    cmd+=" -n" #no dns resolution
    cmd+=" -T4" #timing template
    cmd+=" -iL {}".nmap_targets
    cmd+=" -oX {}".scan_output #output file
    os.system(cmd)
    cmd="rm {}".RECON_PATH/scan_output
    print("Version detection done.")