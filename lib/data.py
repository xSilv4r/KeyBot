#!/usr/bin/env python3
from pathlib import Path

#PATHS
POCS_PATH = Path("./pocs/")
CONF_PATH = Path("./configurations/")
RECON_PATH = Path("./output/recon_output/")

#COLORS
class fg_colors:
    reset='\033[0m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'