
import json

def readBooks(file_name):
    with open(file_name, 'r') as file:
        li = json.load(file)
    return li

