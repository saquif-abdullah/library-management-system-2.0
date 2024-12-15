
import json


def writeBooks(file_name, li):
    with open(file_name, 'w') as file:
        json.dump(li, file, indent = 4)

