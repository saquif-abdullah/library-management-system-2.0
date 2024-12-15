
import read_books
import my_tools


def searchBook(file_name):
    my_tools.Clear()
    print("\n_____________Search__________\n\n")
        
    books = read_books.readBooks(file_name)
    books_id = []

    to_find = input("    Enter title/author/price/quantity/year/isbn/time_of_insert to find the book : ")
    cnt_books = False
    for i in range(len(books)):
        book = books[i]
        for idx, desc in book.items():
            if to_find == desc:
                cnt_books += 1
                books_id.append(i)
                print(f"\n    ID : {i}")
                for key, value in book.items():
                    print(f"      {key}     : {value}")
                break
    
    if cnt_books != 0:
        print(f"\n\n    We found {cnt_books} above books in matched with {to_find}")
    else:
        print(f"    Sorry no book matched with :: {to_find}")
    
    