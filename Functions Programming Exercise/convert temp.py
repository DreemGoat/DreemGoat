def convert_to_celcius(Tf):
    Tc = 5/9*(Tf-32)
    return Tc
def convert_to_kelvin(Tc):
    Tk = Tc +273.15
    return Tk
def convert_temp():
    Tf = float(input("Enter a tempterature in Fahrenheit: "))
    print("The temperature in Fahrenheit is: ", Tf)
    print("The temperature in Celcius is: ",convert_to_celcius(Tf))
    print("The temperature in Kelvin is: ",convert_to_kelvin(convert_to_celcius(Tf)))
convert_temp()