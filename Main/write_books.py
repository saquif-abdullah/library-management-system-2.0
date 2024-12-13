
import json


def writeBooks(file_name, books):
    with open(file_name, 'w') as file:
        json.dump(books, file, indent = 4)

