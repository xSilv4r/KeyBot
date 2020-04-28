from lib.data import fg_colors

def banner():
    print('''%s
 | |/ /         |  _ \      | |  
 | ' / ___ _   _| |_) | ___ | |_ 
 |  < / _ \ | | |  _ < / _ \| __|
 | . \  __/ |_| | |_) | (_) | |_ 
 |_|\_\___|\__, |____/ \___/ \__|
            __/ |                
           |___/                 
%s'''%(fg_colors.green,fg_colors.reset))
    
    print("# Authors: %sShady, Aziz%s.\n"%(fg_colors.lightcyan,fg_colors.reset))