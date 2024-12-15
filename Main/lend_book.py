
import main
import write_lend_book
import read_lend_book
import read_books
import write_books





def lendBook(file_name, lender_file):
    print("\n\n\n_____________Borrow Book__________\n\n")

    ob = main.LibraryManagementSystem()
    

    print("    1. Search book for borrow")
    print("    2. View all books for choosing book to borrow")

    key = int(input("\n    Choose an option : "))

    if key == 1: 
        ob.searchBook()
    else:
        ob.viewBooks()

    
    borrower_name = input("\n    Please enter your name : ")
    ids = list(map(int, input("    Enter books IDs with space to borrow : ").split()))


    availavle = []
    unavailable = []
    books = read_books.readBooks(file_name)

    for id in ids:
        availavle.append(id) if books[id]["quantity"] > 0 else unavailable.append(id)
    
    print("\n    Available books to borrow : ", *availavle)
    print("    Unavailable books to borrow : ", *unavailable)
    yn = int(input("\n    Enter 1 if you want to borrow the available books : "))


    def process():
        lend_books = read_lend_book.readLendBook(lender_file)
        print(lend_books)
        # lend_books[borrower_name] = {"ids": ids}


    if yn == 1:
        process()
        print("\n    Books borrowed Successfully.")
         

    



    # write_lend_book.writeLendBook(lender_file, lend_books) 

    
    
