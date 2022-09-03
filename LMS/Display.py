import ListSplit

# module/function -> displays all the books available in the list
def display_available_books():
    books = ListSplit.processed_file()
    print("<<<<<<<<<< Books available for lending are >>>>>>>>>>")
    for num, book_info in enumerate(books):
        print(num + 1,".","Book:",book_info["name"]," | ",
             "Author:",book_info["author"]," | ","Stock Available:",
             book_info["quantity"]," | ","Cost pre unit:",book_info["price"])
        print()
    