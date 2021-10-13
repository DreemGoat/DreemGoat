e1 = float(input("Enter length of edge1: "))
e2 = float(input("Enter length of edge2: "))
e3 = float(input("Enter length of edge3: "))
if e1+e2>e3 and e2<e1+e3 and e2+e3>e1:
    p = eval("e1+e2+e3")
    print("The perimeter is", p)
else:
    print("Perimeter cannot be calculated: the input is invalid")