import json

numbers = ['2', '3', '4', '5']

filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)
