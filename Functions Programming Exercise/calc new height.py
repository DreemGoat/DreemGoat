def calc_new_height():
    w = float(input("Enter the current width: "))
    h = float(input("Enter the current height: "))
    d = float(input("Enter the desired width: "))
    m = h/w*d
    print("The corresponding height is:", m)
calc_new_height()