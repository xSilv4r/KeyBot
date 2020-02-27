import datetime
import os

def configGeneration():
    file_name = raw_input("Enter configuration filename:\n")
    f = open(file_name+".conf", "w")
    l = raw_input("Enter ip/range:\n")
    f.write("range = "+l+"\n")
    l = raw_input("Enter port/range:\n")
    f.write("ports = "+l+"\n")
    l = raw_input("Enter rate:\n")
    f.write("rate = "+l+"\n")
    l = raw_input("Enter output-format:\n")
    f.write("output-format = "+l+"\n")
    l = raw_input("Enter output-filename:\n")
    f.write("output-filename = "+l+"\n")
    f.close()
    return file_name

def portScanner():
    file_name=configGeneration()
    cmd="masscan -c "
    cmd+=file_name
    cmd+=".conf --banners"
    os.system(cmd)


if __name__ == "__main__":
    now = datetime.datetime.now()
    print "KeyBot starting at "+now.isoformat()
    portScanner()