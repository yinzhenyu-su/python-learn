import json

filename = 'numbers.json'
with open(filename) as file_obj:
    content = json.load(file_obj)
    print(content)
