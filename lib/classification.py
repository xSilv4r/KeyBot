import json

def get_pocfile(keyword):
    with open('./lib/mapping.json') as json_file:
        data = json.load(json_file)

    for each in data:
        if each in keyword:
            return data[each]

    return None