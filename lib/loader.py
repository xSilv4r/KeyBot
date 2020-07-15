#!/usr/bin/env python3
import sys
import os
import queue
import glob
import json

from lib.data import th,poc_array,targets,results_data
from lib.classification import get_pocfile
from lib.nmap_parser import get_targets

def loadModule(pocfile):
    if pocfile:
        name="pocs.{}".format(pocfile)
        try:
            module = __import__(name)
        except ImportError:
            print("Import failed.")
            return None
        
        for n in name.split(".")[1:]:
            module= getattr(module, n)

        if not hasattr(module, 'poc'):
            print("Can't find essential method POC in current script Please modify your script/PoC.")
        else:
            poc = {'module':module,'name':module.__name__}
            poc_array.append(poc)
            return module
    else:
        return None

def loadTargets():
    files = [f for f in glob.glob("./output/recon_output/*")]
    print("[!] Loading targets")
    for f in files:
        tgs = get_targets(f)
        if tgs is not None:
            for target in tgs:
                targets.append(target)

def loadPayloads():
    print('[!] Initialize targets...')
    th.queue = queue.Queue()
    for item in targets:
        pocfile = get_pocfile(item['service'])
        module = loadModule(pocfile)
        if module:
            target = {'ip_addr':item['ip'],'port':item['port'],'service':item['service']}
            th.queue.put(target)
            print("[+] target added: {}:{}, {}".format(item['ip'],item['port'],item['service']))
        if not(module):
            print("[!] Can't find PoCs for these targets but data will be saved...")
            res = {"target":item['ip'],"port":item['port'],"service":item['service'],"poc":"none","exploit_status":False}
            results_data.append(res)
            with open('./output/final_output/data.json', 'w') as outfile:
                json.dump(results_data, outfile)
            print("Data saved : {}".format(res))

    print('[+] Total targets: %s' % str(th.queue.qsize()))
