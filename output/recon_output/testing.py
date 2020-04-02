import os.path
import argparse
import subprocess
import sys
import os
import time
import errno
import array
import re

def process_exists(tst):
    """Check whether pid exists in the current process table."""
    retcode = tst.poll()
    if retcode is None:
       return True
    else:
       return False

#
###############################################################
#
# Begin ---->>> get_running_processes <<<-----
#
def get_running_processes():
#
    running_processes = 0
    for s in process_array:
        if process_exists(s):
           running_processes = running_processes + 1
    return running_processes
#
# End End End ---->>> get_running_processes <<<-----
#

###############################################################
#
# Begin ---->>> Main program <<<-----
#
# The debugf flag essentially displays trace messages to aid in
# troubleshooting.  It must be 'yes' to show the messages.
#

max_concurrent_scans = 2
sleep_seconds = 0

ip_array = ['192.168.1.1']

#####################################################################
#
# Beginning of process execution and throttling loop.
#
process_array = []
running_scans = 0
if max_concurrent_scans > len(ip_array):
   max_concurrent_scans = len(ip_array)

while running_scans > 0 or len(ip_array) > 0:
   if running_scans < max_concurrent_scans:
      number_to_kickoff = max_concurrent_scans - running_scans
      if len(ip_array) > 0:
         for startloop in range(0,number_to_kickoff):
            ip_address = ip_array[0]
            p = subprocess.Popen(["nmap", "-F", (ip_address)[0]],stdout=subprocess.PIPE)
            process_array.append(p)
            del ip_array[0]

   running_scans = get_running_processes()
   #print 'Running scans: '+str(running_scans)
  # Sleep for awhile so as not to waste too much system resources rechecking.
   time.sleep(sleep_seconds)
#
# End of process execution and throttling loop.
print "all scans done."