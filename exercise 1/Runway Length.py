a = float(input("Enter the plane's acceleration in m/s: "))
v = float(input("Enter the plane's take-off speed in m/s**2: "))
z = ((v**2)/(2*a))
print("The minimum runway length needed for this airplane is", round(z,4), "meters")