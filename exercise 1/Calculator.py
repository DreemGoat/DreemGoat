x = float(input("Enter the subtotal:$"))
y = float(input("Enter the amount (as a %): "))
z = (x*y/100)
a = x+z
x = "{:.2f}".format(x)
z = "{:.2f}".format(z)
a = "{:.2f}".format(a)
print("Subtotal:$", x)
print("Tip:$", z)
print("Total:$",a)