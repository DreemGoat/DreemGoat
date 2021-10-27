def calc_weight_on_planet(x,gravity=23.1):
    N = x * (gravity/9.8) #this is the formula to find out weight on other planets, assuming that Earth's gravity is 9.8m/s**2)
    print(N)
calc_weight_on_planet(120,9.8) #(x=120,y=9.8)
calc_weight_on_planet(120) #(x=120,y=23.1)
calc_weight_on_planet(120,23.1) #(x=120,y=23.1)