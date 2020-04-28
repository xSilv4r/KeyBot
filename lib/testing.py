import glob

mylist = [f for f in glob.glob("../output/recon_output/*.xml")]

print(mylist)