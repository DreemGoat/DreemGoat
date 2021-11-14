import os
os.chdir("/Users/dep50/OneDrive/Documents/Coding Projects/DreemGoat/Week 7")
fInput = open("Poems of Arthur Hugh Clough.txt","r")
output = open("numbered Poems of Arthur Hugh","w") #the new file name
count = 0
for line in fInput: # this loop transfers the strings in fInput
    count = count + 1
    output.write("{:2d} {}".format(count,line)) #this formats the file to number the lines
output.close()