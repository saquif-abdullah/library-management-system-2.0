
import my_tools
import read_books
import write_books
import read_lend_book
import write_lend_book


def returnLendedBook(file_name, lender_file):
    my_tools.Clear()
    print("\n\n\n_____________Return Books__________\n\n")

    borrower_name = input("    Enter your name : ")
    books = read_books.readBooks(file_name)
    lended_books = read_lend_book.readLendBook(lender_file)
    
    if borrower_name not in lended_books:
        print("    Sorry, You didn't borrow any book")
        return
    
    ids = list(map(int, input("    Enter IDs of books you want to return : ").split()))
    quantity = list(map(int, input("    Enter quantity respectively           : ").split()))


    for i in range(len(ids)):
        lended_books[borrower_name][str(ids[i])] -= quantity[i]
        books[ids[i]]["quantity"] += quantity[i]
    
    write_lend_book.writeLendBook(lender_file, lended_books)
    write_books.writeBooks(file_name, books)

    print("\n\n    Books returned successfully.")


