import DT
import ListSplit


def lendBook():  
    books_in_stock  = ListSplit.processed_file()
    success = False
    total_cost = 0
    count=1
    while success == False:
        ''' code for asking the name of the borrower''' 
        while(True):
            firstName=input("Enter the first name of the borrower: ")
            if firstName.isalpha():
                break
            print("please input alphabet from A-Z")
        
        while(True):
            lastName=input("Enter the last name of the borrower: ")
            if lastName.isalpha():
                break
            print("please input alphabet from A-Z")
        print(" ")
        
        file = "Borrow_"+firstName+".txt"
        with open(file,"w+") as f:
            f.write("               Library Management System  \n")
            f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
            f.write("    Date: "+DT.getDate()+"    Time:"+DT.getTime()+"\n\n")
            f.write("{: <5} {: <25} {: <25} {: <15} {: <1}".format("S.N.", "Book", "Author","Price","\n\n")) 
        
        while success == False:
            print("Please enter the asked Details below: ")
            print("-------------------------------------")
            for num, book_info in enumerate(books_in_stock):
                print(">>>Enter",num,"to borrow book",book_info["name"])
            
            try: 
                a = int(input()) 
                
                try:
                    if(int(books_in_stock[a]["quantity"])>0):

                        print("Success! Book is available")
                        print("--------------------------")
                        with open(file,"a") as f:
                            f.write("{: <5} {: <25} {: <25} {: <15} {: <1}".format(str(count)+".",books_in_stock[a]["name"],books_in_stock[a]["author"],books_in_stock[a]["price"],"\n"))
                        
                        price = books_in_stock[a]["price"]
                        price = price.strip("$")
                        total_cost += float(price)
                        
                        with open("Stock.txt",'w') as books:
                             books.truncate()
                             quantity = books_in_stock[a]["quantity"]
                             remaining = int(quantity)-1
                             books_in_stock[a]["quantity"] = str(remaining)
                             for available_books in books_in_stock:
                                 if int(available_books["quantity"]) <= 0:
                                     continue
                                 else:
                                     print(available_books["name"]+","+
                                           available_books["author"]+","+ 
                                           available_books["quantity"]+ ","+
                                           available_books["price"],file=books)


                        #for borrowing multiple books
                        loop=True
                        while loop==True:
                            print("Do you want to borrow more books, Press Y for Yes and N for No.\n")
                            choice=str(input())
                            
                            if(choice.upper()=="Y"):
                                
                                print("Please enter the asked Details below:")
                                
                                for i in range(len(books_in_stock)):
                                    print(">>>Enter",i,"to borrow book",books_in_stock[i]["name"])
                                
                                a = int(input())
                                
                                if(int(books_in_stock[a]["quantity"])>0):
                                    print("Book is available")
                                    count=count+1
                                    with open(file,"a") as f:
                                        f.write("{: <5} {: <25} {: <25} {: <15} {: <1}".format(str(count)+".",books_in_stock[a]["name"],books_in_stock[a]["author"],books_in_stock[a]["price"],"\n"))
                                    
                                   
                                    price = books_in_stock[a]["price"]
                                    price = price.strip("$")
                                    total_cost += float(price)
                                    
                                    with open("Stock.txt",'w') as books:
                                            books.truncate()
                                            quantity = books_in_stock[a]["quantity"]
                                            remaining = int(quantity)-1
                                            books_in_stock[a]["quantity"] = str(remaining)
                                            for available_books in books_in_stock:
                                                if int(available_books["quantity"]) <= 0:
                                                    continue
                                                else:
                                                    print(available_books["name"]+","+
                                                          available_books["author"]+","+ 
                                                          available_books["quantity"]+ ","+
                                                          available_books["price"],file=books)
                                            success=False     
                                else:
                                    loop = False
                                    print("Sorry the books selected is not available!")
                                    break
                            
                            elif (choice.upper()=="N"):                      
                                loop=False
                                success=True
                            
                            else:
                                print("Please choose as instructed")
                        

                    else:
                        print("Book is not available")
                       
                        lendBook()
                        success=False
                
                except IndexError:
                    print(" ")
                
                    print("Please choose book acording to their number.")
            
            except ValueError:
                print(" ")
                print("Please input the appropriate details.")
    
    with open(file,"a") as f:
        f.write("\t\t\t\t\t\tTotal price: $"+str(total_cost)+"\n")        
    
    file = "Borrow_"+firstName+".txt"    
    with open(file,"r") as f:
        data = f.read()
        print(data)

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
