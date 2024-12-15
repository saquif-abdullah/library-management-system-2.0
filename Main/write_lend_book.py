
import json

def writeLendBook(file_name, lend_books):
    with open(file_name, 'w') as file:
        json.dump(lend_books, file, indent = 4)