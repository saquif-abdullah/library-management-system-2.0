import main
import my_tools
import read_books
import write_books

def deleteBook(file_name):
    my_tools.Clear()
    print("\n_____________Delete Book__________\n\n")
    
    ob = main.LibraryManagementSystem()

    print("    1. Search book for Deleting")
    print("    2. View all books for choosing book to Delete")

    key = int(input("\n    Choose an option : "))

    if key == 1: 
        ob.searchBook()
    elif key == 2:
        ob.viewBooks()
    else:
        print("    Envalid input.")
    
    to_delete = int(input("\n\n    Enter ID of the book : "))

    books = read_books.readBooks(file_name)
    del books[to_delete]
    write_books.writeBooks(file_name, books)

    print("\n    Book Deleted Successfully")

    


    