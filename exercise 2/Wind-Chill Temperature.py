ta = float(input("Enter the temperature in Fahrenheit: "))
while -58>ta or ta>41:
    print("Temperature must be between -58F and 41F")
    ta = float(input("Please re-enter the temperature in Fahrenheit: "))
else:
    print("temperature is:", ta)

v = float (input("Enter the wind speed in miles per hour: "))
while v<2:
    print("Speed must be greater than or equal to 2")
    v = float(input("Please re-enter the wind speed in miles per hour: "))
else:
    twc = 35.74 +0.6215*ta - (35.74*v**0.16)+(0.4275*ta*v**0.16)
    twc = round(twc, 1)
    twc = "{:.3f}".format(twc)
    print("The wind chill index is", twc)