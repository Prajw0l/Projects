import DT
import ListSplit


# module/function -> takes a request of a book and lends it
def return_book():
    ''' Function to return and update the book in library.'''
    books_in_stock = ListSplit.processed_file()
    borrower_name = input("Enter the first name of the borrower: ")
    borrow_file = "Borrow_"+borrower_name+".txt"
    data = ""
    try:
        with open(borrow_file,"r")as f:           
            lines = f.readlines()
            lines = [borrow_file.strip("$") for borrow_file in lines]

        with open(borrow_file,"r") as f:
            data = f.read()
          
    except:
        print("The borrower name is incorrect, please try again!")
        return_book()

    re_file = "Return_"+borrower_name+".txt"
    with open(re_file,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ borrower_name+"\n")
        f.write("    Date: " + DT.getDate()+"    Time:"+ DT.getTime()+"\n\n")
        f.write("{: <5} {: <25} {: <15} {: <1}".format("S.N.","Bookname","Cost","\n\n"))

    for i in range(len(books_in_stock)):
        if books_in_stock[i]["name"] in data:
            with open(re_file,"a") as f:
                f.write("{: <5} {: <25} {: <15} {: <1}".format(str(i+1),books_in_stock[i]["name"],books_in_stock[i]["price"],"\n"))
                books_in_stock[i]["quantity"] = int(books_in_stock[i]["quantity"]) + 1


    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        try:
            day=int(input())
            fine=0.5*day
            with open(re_file,"a")as f:
                f.write("\t\t\t\tFine:"+str(fine),"\n")
        except ValueError:
            print("Please enter the days in numerical format") 

    elif(stat.upper()=="N"):
        with open(re_file,"a")as f:
            f.write("\t\t\t\t\t No fine charge.")
    else:
        print("Please choose as instructed")

    re_file = "Return_"+borrower_name+".txt"    
    with open(re_file,"r") as f:
        data = f.read()
        print(data)
    
    with open("Stock.txt","w+") as f:
            for i in range(len(books_in_stock)):
                f.write(books_in_stock[i]["name"]+","+books_in_stock[i]["author"]+","+
                        str(books_in_stock[i]["quantity"])+","+books_in_stock[i]["price"]+"\n")





