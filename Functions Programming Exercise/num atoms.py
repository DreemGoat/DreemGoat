def num_atoms(x,y=196.97): #a value must be put for X, while Y has an optional default value
    W=(x/y*(6.022*(10**23))) #this is the formula for Atomic Weight
    print(W)
num_atoms(10)         #(x=10, y=196.97)
num_atoms(10,12.001)  #(x=10, y=12.001)
num_atoms(10,1.008)   #(x=10, y=1.008)