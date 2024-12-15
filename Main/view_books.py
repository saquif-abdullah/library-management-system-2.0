
import my_tools
import read_books

def viewBooks(file_name):
    my_tools.Clear()
    
    print("\n\n\n_____________All Books__________\n\n")

    books = read_books.readBooks(file_name)
    for i in range(len(books)):
        print(f"\n    ID : {i}.")
        book = books[i]
        for key, value in book.items():
            print(f"      {key}     : {value}")
    
  
    

