from ShoppingDEP import Grocery #imports all functions from the ShoppingDEP file
list = []
def cart(): #the function to put in all the items from the store
    num = int(input("Enter number of items: ")) #sets the range
    while num <= 0: #a check to make sure the inputted number is over 0
        print("please enter a number greater than 0")
        num = (input("Re-Enter number of items: "))
    else:
        x = range(num) 
        for i in x:
            c1 = Grocery()
            c1.setfood(input("Enter food: "))
            amount = float(input("Enter amount in pounds: "))
            while amount <= 0: #a check to make sure the inputted number is over 0
                print("please enter a number greater than 0")
                amount = float(input("Re-Enter amount in pounds:"))
            else:
                c1.setamount(amount)
                list.append(c1) #adds everything to the list

def showlist(list): #lists everything
    for x in list:
        print("Item:", x.getfood())
        print("Amount:", x.getamount())
        print("Price per pound:", x.getprice())
        print("Price of order:", x.totalprice())
        print("") #left empty for formatting

def prices(list): #calculates the total price of the orders
    Totalprice = 0
    for x in list:
        Totalprice = x.totalprice()+Totalprice 
    print("The total cost is: ", Totalprice)

def shop(): #the main function that calls everything other function
    cart()
    print("Here is the summary of the items you purchased")
    showlist(list)
    prices(list)

shop()