
import main
import my_tools
import read_books
import write_books

def editBook(file_name):
    my_tools.Clear()
    print("\n_____________Edit Book__________\n\n")
    
    ob = main.LibraryManagementSystem()

    print("    1. Search book for Edit")
    print("    2. View all books for choosing book to Edit")

    key = int(input("\n    Choose an option : "))

    if key == 1: 
        ob.searchBook()
    elif key == 2:
        ob.viewBooks()
    else:
        print("    Envalid input.")
    
    to_edit = int(input("\n\n    Enter ID of the book : "))

    books = read_books.readBooks(file_name)
    
    print("\n\n    Old Data")
    for key, value in books[to_edit].items():
        print(f"      {key} : {value}")
    
    keys = books[to_edit].keys()
    print("\n    Enter new Data.")
    for key in keys:
        if key == "isbn" or key == "time":
            continue
        books[to_edit][key] = input(f"      {key} : ")
    
    
    write_books.writeBooks(file_name, books)
    print("\n    Book Edited Successfully")
