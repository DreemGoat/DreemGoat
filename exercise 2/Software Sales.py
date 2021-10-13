r = 99
a = float(input("Enter the number of packages purchased: "))
totalAmount = 0
if a <= 9:
    discount = 0
elif a<=19:
    discount = 10
elif a<=49:
    discount = 20
elif a<=99:
    discount = 30
elif a>=100:
    discount = 40
z = round(r * a * discount / 100, 2)
totalAmount = r*a-z
z = "{:.2f}".format(z)
totalAmount = "{:.2f}".format(totalAmount)
print("discount amount @", discount,"% :", z)
print("Total amount", totalAmount )