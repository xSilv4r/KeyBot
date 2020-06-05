from loader import loadModule, loadPayloads
from pocengine import run
from data import th


targets=[{'192.168.1.1':'ftp D-Link/Comtrend DSL modem ftp firmware update'}, {'192.168.1.1': 'ssh Dropbear sshd 0.46'}, {'192.168.1.1': 'telnet'}, {'192.168.1.1': 'tcpwrapped'}]

loadPayloads(targets)
run()

