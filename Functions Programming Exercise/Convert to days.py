def get_days():
    h = float(input("Enter number of hours: "))
    m = float(input("Enter number of minutes: "))
    s = float(input("Enter number of seconds: "))
    h = h/24 #there are 24 hours in a day
    m = (m/60)/24 #there are 60 minutes in an hour
    s = (s/3600)/24 #there are 3600 seconds in an hour
    return h+m+s

def convert_to_days():
    d = get_days() #with the return command this should give d a general value
    print("the number of days is:", round(d,4)) #round ,4 here rounds it off to 4 decimal places

convert_to_days()