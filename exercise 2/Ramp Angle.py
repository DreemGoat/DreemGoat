import math
g =9.8
m = float(input("Enter the mass of the cart(in kg): "))
F = float(input("Enter the force to push the cart (in N): "))
t = math.sinh(F/(m*g))
t = math.degrees(t)
print("The angle of the ramp is", round(t,1), "degrees")