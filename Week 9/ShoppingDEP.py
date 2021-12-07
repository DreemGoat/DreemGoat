class Grocery:
    def __init__(self,food="Dry Cured Iberian Ham",amount=1):
        self.__food = food 
        self.__amount = amount #initializer module with private methods

    def setfood(self,food): #the command to set food
        self.__food = food

    def setamount(self,amount): #the command to set amount
        self.__amount = amount

    def getfood(self): #the command to get food
        return self.__food

    def getamount(self): #the command to get the amount
        return self.__amount

    def __pricelist(self): #the price list for all the food items 
        if self.__food == "Dry Cured Iberian Ham":
            price = 177.80
            return price
        elif self.__food == "Wagyu Steaks":
            price = 450.00
            return price
        elif self.__food == "Matsutake Mushrooms":
            price = 272.00
            return price
        elif self.__food == "Kopi Luwak Coffee":
            price = 306.50
            return price
        elif self.__food == "Moose Cheese":
            price = 487.20
            return price
        elif self.__food == "White Truffles":
            price = 3600.00
            return price
        elif self.__food == "Blue Fin Tuna":
            price = 3603.00
            return price
        elif self.__food == "Le Bonnotte Potatoes":
            price = 270.81
            return price

    def getprice(self): #since the pricelist is private, this command is necessary to get the prices
        return self.__pricelist()

    def totalprice(self):
        return self.__amount * self.__pricelist() #food cost calculation