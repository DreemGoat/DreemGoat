def calc_new_height():
    w = float(input("Enter the current width: "))
    h = float(input("Enter the current height: "))
    d = float(input("Enter the desired width: "))
    m = h/w*d #this is the formula for adjusting aspect ratios
    print("The corresponding height is:", m)
calc_new_height()