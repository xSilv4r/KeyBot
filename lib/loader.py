#!/usr/bin/env python3
import sys
import os
import queue
from lib.data import th,poc_array
from lib.classification import get_pocfile

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


def loadPayloads(targets):
    print('Initialize targets...')
    th.queue = queue.Queue()
    for item in targets:
        for k,v in item.items():
            pocfile = get_pocfile(v)
            module = loadModule(pocfile)
            if module:
                th.queue.put(k)
                print("target added: {}".format(k))

    print('Total targets: %s' % str(th.queue.qsize()))
