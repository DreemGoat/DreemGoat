def convert_to_celcius(Tf): #(Tf) here is necessary as it won't be inputted if it's a blank parameter
    Tc = 5/9*(Tf-32)
    return Tc
def convert_to_kelvin(Tc): #(Tc) here is necessary as it won't be inputted if it's a blank parameter
    Tk = Tc +273.15
    return Tk
def convert_temp():
    Tf = float(input("Enter a tempterature in Fahrenheit: "))
    print("The temperature in Fahrenheit is: ", Tf)
    print("The temperature in Celcius is: ",convert_to_celcius(Tf))
    print("The temperature in Kelvin is: ",convert_to_kelvin(convert_to_celcius(Tf))) #writing the functions in the print is shorter and has the same end result
convert_temp()