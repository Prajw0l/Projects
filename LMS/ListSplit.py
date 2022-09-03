
#1st function -> reads data from the file 
def read_file():
      ''' takes a text file and reads data from it and returns lines of values'''
      file = open("Stock.txt",'r')
      lines = file.readlines()
      file.close()
      return lines

# 2nd function -> processes the raw data and stores it in a dictionary which is then contained by a list.
def processed_file():
    raw_data = read_file()
    books = []
    ''' takes raw data and puts it into a dictionary'''
    for line in raw_data:
            name, author, quantity, price = tuple(line.replace('\n','').split(','))
            information = {"name": name ,"author": author,"quantity": quantity,"price": price}
            books.append(information)     
    return books

