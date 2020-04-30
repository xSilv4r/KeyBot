#!/usr/bin/env python3
import sys
import os
import queue
import glob

from lib.data import th,poc_array,targets
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
            poc_array.append(module)
            return module
    else:
        return None

def loadTargets():
    files = [f for f in glob.glob("./output/recon_output/*")]
    print("[!] Loading targets")
    for f in files:
        tgs = get_targets(f)
        for target in tgs:
            targets.append(target)

    

def loadPayloads():
    print('[!] Initialize targets...')
    th.queue = queue.Queue()
    for item in targets:
        for k,v in item.items():
            pocfile = get_pocfile(v)
            module = loadModule(pocfile)
            if module:
                th.queue.put(k)
                print("[+] target added: {}:{}".format(k,v))

    print('[+] Total targets: %s' % str(th.queue.qsize()))
