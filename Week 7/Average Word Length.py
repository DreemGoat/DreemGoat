import os
os.chdir("/Users/dep50/OneDrive/Documents/Coding Projects/DreemGoat/Week 7")
file = open("Poems of Arthur Hugh Clough.txt","r")
a = file.read() #turns file into a string
print(len(a)) #len counts the length of words
file.close