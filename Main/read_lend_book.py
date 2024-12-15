
import json

def readLendBook(file_name):
    with open(file_name, 'r') as file:
        lend_books = json.load(file)
    return lend_books
