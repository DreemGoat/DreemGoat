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
    if z == 1:
        print("the proper fraction cannot be reduced further")
    elif z > 1:
        x = x/z
        y = y/z
        print("the proper fraction can be reduced to", x,"/",y)
elif x > y:
    print(x,"/",y,"is an improper fraction")
    if z == 1:
        print("the improper fraction cannot be reduced further")
    elif z > 1:
        x = x/z
        y = y/z
        print("the improper fraction can be reduced to", x,"/",y)
    if math.fmod(x,y) == 0:
        r = x/y
        print("The whole number is", r)
    elif math.fmod(x,y) > 0:
         r= (x-math.fmod(x,y))/y
         print("The mix number is", r, "and", math.fmod(x,y),"/",y)