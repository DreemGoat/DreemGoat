from ShoppingDEP import Grocery
list = []
def cart():
    num = int(input("Enter number of items: "))
    while num <= 0:
        print("please enter a number greater than 0")
        num = (input("Re-Enter number of items: "))
    else:
        x = range(num)
        for i in x:
            c1 = Grocery()
            c1.setfood(input("Enter food: "))
            amount = float(input("Enter amount in pounds: "))
            while amount == 0 or amount <= 0:
                print("please enter a number greater than 0")
                amount = float(input("Re-Enter amount in pounds:"))
            else:
                c1.setamount(amount)
                list.append(c1)

def showlist(list):
    for x in list:
        print("Item:", x.getfood())
        print("Amount:", x.getamount())
        print("Price per pound:", x.getprice())
        print("Price of order:", x.totalprice())
        print("")

def prices(list):
    Totalprice = 0
    for x in list:
        Totalprice = x.totalprice()+Totalprice
    print("The total cost is: ", Totalprice)

def shop():
    cart()
    print("Here is the summary of the items you purchased")
    showlist(list)
    prices(list)

shop()