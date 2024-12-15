
import my_tools
import write_books
import read_books


def addBook(file_name):
    
    my_tools.Clear()
    print("\n\n\n_____________Add Books__________\n\n")

    book = {}
    book["title"] = input("    Title         : ")
    book["author"] = input("    Author : ")
    book["price"] = input("    price : ")
    book["quantity"] = int(input("    Quantity : "))
    book["year"] = input("    Publishing year : ")
    
    
    book["isbn"] = my_tools.randomIsbn()
    book["time"] = my_tools.currentTime()
    
    
    

    books = read_books.readBooks(file_name)
    books.append(book)
    write_books.writeBooks(file_name, books)

    print("    \nBook added successfully.")
    
    



