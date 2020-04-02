with open('multitest.conf', 'r') as f:
    for line in f:
        if line.find("output/recon_output/") != -1:
            b = line.rpartition('/')
            print(b[2].strip())
            