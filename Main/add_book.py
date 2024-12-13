
import my_tools
import write_books



def addBook(file_name):
    my_tools.Clear()
    print("\n________Saquif__DhumkeTU________")
    print("\n_____________Add Books__________\n\n")

    book = {}
    book["title"] = input("    Title         : ")
    book["author"] = input("    Author : ")
    book["year"] = input("    Publishing year : ")
    book["price]"] = input("    Price : ")
    book["quantity"] = input("    Quantity : ")

    book["isbn"] = my_tools.randomIsbn()
    book["time"] = my_tools.currentTime()

    books = []
    books.append(book)
    

    write_books.writeBook(file_name, books)
    print("Book added successfully.")
    key = my_tools.menuOrExit()
    if key == 2:
        exit()




