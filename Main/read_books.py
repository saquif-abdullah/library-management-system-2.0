
import json

def readBooks(file_name):
    with open(file_name, 'r') as file:
        books = json.load(file)
    return books

