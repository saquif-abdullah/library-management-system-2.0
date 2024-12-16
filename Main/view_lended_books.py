import my_tools
import read_books
import read_lend_book


def viewLendedBooks(file_name, lender_file):
    
    my_tools.Clear()
    print("\n\n\n_____________View Lended Books__________\n\n")
    lended_books = read_lend_book.readLendBook(lender_file)
    del lended_books["None"]
    books = read_books.readBooks(file_name)
    
    
    if lended_books:
        for borrower, book in lended_books.items():
            print(f"\n    Bowwer Name : {borrower}")
            for id, quantity in book.items():
                id = int(id)
                print(f"      Book Title : {books[id]["title"]}, Borrowed quantity : {quantity} copy")

    else:
        print("    No Book is borrowed.")    
