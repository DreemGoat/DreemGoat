def get_days():
    h = float(input("Enter number of hours: "))
    m = float(input("Enter number of minutes: "))
    s = float(input("Enter number of seconds: "))
    h = h/24
    m = (m/60)/24
    s = (s/3600)/24
    return h+m+s

def convert_to_days():
    d = get_days()
    print("the number of days is:", round(d,4))

convert_to_days()