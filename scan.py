import os

def portScan(startPort,endPort,rate):
    cmd = "masscan -p "
    cmd+= startPort
    cmd+= "-"
    cmd+= endPort
    cmd+= ""