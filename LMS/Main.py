import Return
import ListSplit
import DT
import Borrow
import Display

'''
user input
reading files
generating borrowing/ returning notes
'''
def start():
    option = 0
    while(True):
        print(" ======LIBRARY MENU=======")
        print("Enter 1. To Display all available books")
        print("Enter 2. To lend a book")
        print("Enter 3. To add a returned a book")
        print("Enter 4. To Exit")
        print()
        try:
            option = int(input("Select a choice from 1-4: "))
            print()
        except ValueError:
            print("Invalid Choice!")
            continue
        if option <=0 or option > 4:
            print("Invalid Choice!")

        if option == 1:
            Display.display_available_books()
        elif option == 2:
            Display.display_available_books()
            Borrow.lendBook()
        elif option == 3:
            Return.return_book()
        elif option == 4:
                ("Thank you for using the library management system. Good Bye!")
                break
        
                
start()          