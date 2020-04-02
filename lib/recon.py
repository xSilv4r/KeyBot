
#!/usr/bin/env python3
import os
import json
import subprocess 
import ast 
import time

from lib.data import fg_colors
from lib.data import RECON_PATH

ip_array = []
ports_array = []
sleep_seconds = 10
process_array = []

def process_exists(tst):
    """Check whether pid exists in the current process table."""
    retcode = tst.poll()
    if retcode is None:
       return True
    else:
       return False

def get_running_processes():
    running_processes = 0
    for s in process_array:
        if process_exists(s):
           running_processes = running_processes + 1
    return running_processes

def version_detection(output_filename):
    max_concurrent_scans = 2
    running_scans = 0
    # proc = subprocess.run(
    # args = ["/bin/bash", "./lib/bash.sh", "{}.json".format(output_filename)],
    # universal_newlines = False,
    # stdout = subprocess.PIPE)
    # OBJECT=proc.stdout.decode("utf-8")
    # OBJECT = ast.literal_eval(OBJECT) 
    with open('{}.json'.format(output_filename), 'r') as f:
        content = ast.literal_eval(f.read())
        OBJECT ={}
        for i in content:
            port=i['ports'][0]['port'] 
            ip=i['ip']
            if ip not in OBJECT:
                OBJECT[ip]=[port]
            else:
                OBJECT[ip].append(port)

    # for key,value in OBJECT.items():
    #     open_ports=""
    #     print(key)
    #     for i in range(len(value)):
    #         open_ports+="{},".format(value[i])

    #     nmap(key,open_ports)

    for key,value in OBJECT.items():
        open_ports=""
        for i in range(len(value)):
            open_ports+="{},".format(value[i])

        ip_array.append(key)
        ports_array.append(open_ports)
    
    if max_concurrent_scans > len(ip_array):
        max_concurrent_scans = len(ip_array)

    while running_scans > 0 or len(ip_array) > 0:
        if running_scans < max_concurrent_scans:
            number_to_kickoff = max_concurrent_scans - running_scans
            if len(ip_array) > 0:
                for startloop in range(0,number_to_kickoff):
                    ip_address = ip_array[0]
                    p = subprocess.Popen(["nmap", "-sV","-p",(ports_array)[0],
                    "--open","-Pn","-n","-T4","-oX",(RECON_PATH/ip_array[0]),(ip_array)[0]],stdout=subprocess.PIPE)
                    process_array.append(p)
                    del ip_array[0]
                    del ports_array[0]
        running_scans = get_running_processes()
        
        print('Running scans: '+str(running_scans))
    # Sleep for awhile so as not to waste too much system resources rechecking.
        time.sleep(sleep_seconds)

    print("%s[+]%s Version detection done."%(fg_colors.lightgreen,fg_colors.reset))
    #cmd="rm {}.json".format(output_filename)
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