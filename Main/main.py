
### Saquif :: _DhumkeTU_ :: 13/12/2024 :: 04:43 PM

import my_tools
import add_book
import view_books
import search_book
import edit_book
import delete_book
import lend_book

class LibraryManagementSystem:

    def __init__(self):
        
        self.file_name = "../Dataset/library.json"
        self.lender_file = "../Dataset/lend_books.json"
        self.menu = {
            1: "Add Book",
            2: "View All Books",
            3: "Search Book",
            4: "Edit Book",
            5: "Delete Book",
            6: "Lend Book",
            7: "Exit"
        }
        
    
    def mainMenu(self):
        my_tools.Clear()
        print("\n________Saquif__DhumkeTU________")
        print("\n_____________Main Menu__________\n\n")
        for index, message in self.menu.items():
            print(f"    {index}. {message}\n")
    
    def addBook(self):
        add_book.addBook(self.file_name)
    
    def viewBooks(self):
        view_books.viewBooks(self.file_name)
    
    def searchBook(self):
        search_book.searchBook(self.file_name)
    
    def editBook(self):
        edit_book.editBook(self.file_name)
    
    def deleteBook(self):
        delete_book.deleteBook(self.file_name)
    
    def lendBook(self):
        lend_book.lendBook(self.file_name, self.lender_file)
    
    def exitProgram():
        exit()
    
    def menuOrExit(self):
        return my_tools.menuOrExit()
        



def main():

    my_tools.Clear()
    print("\n________Saquif__DhumkeTU________")
    
    print("\n   ___Welcome to my Library___")
    print()
    input("\n   Press Enter to continue :: ")
    
    
    ob = LibraryManagementSystem()
    ob.menu_function_map = {
        1: ob.addBook,
        2: ob.viewBooks,
        3: ob.searchBook,
        4: ob.editBook,
        5: ob.deleteBook,
        6: ob.lendBook,
    }

    
    while True:
        ob.mainMenu()
        try:
            key = int(input("    Choose an option : "))
            
            if not(key>=1 and key<=7):
                print("\n\n    Invalid Input.")
                key = ob.menuOrExit()
                # print(key)
                if key == 1:
                    continue
                else:
                    exit()

            elif key == 7:
                exit()
            elif key in ob.menu_function_map:
                ob.menu_function_map[key]()
           
        except ValueError:
            print("\n\n    Value Error")
        

        if ob.menuOrExit() == 2:
            exit()
    




if __name__ == "__main__":
    main()
