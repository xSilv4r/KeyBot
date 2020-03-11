import json

with open('../output/recon_output/testoutput.json') as json_file:
    data=json_file.read()

json_data = json.loads("".join(data.split()).rstrip(",]") + str("]"))

for key in json_data:
    print(key )