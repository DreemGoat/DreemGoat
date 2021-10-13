import math

x = int(input("Enter a numerator, Value must be greater than 0: "))
while x <= 0:
    print("Invalid, number must be positive.")
    x = int(input("Re-Enter a numerator: "))
else:
    print("numerator =", x)
y = int(input("Enter a denominator,Value must be greater than 0: "))
while x <= 0:
    print("Invalid, number must be positive.")
    y = int(input("Re-Enter a numerator: "))
else:
    print("denominator =", y)
z= math.gcd(x,y)
if x < y:
    print(x,"/",y,"is a proper fraction")
    if x/2 = int:
        print("the f")
elif x > y:
    print(x,"/",y,"is an improper fraction")