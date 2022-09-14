import json
with open('data22.json') as json_file:
    prog_dict = json.load(json_file)
    print(prog_dict['name'])
    print(prog_dict)
    print(type(prog_dict))