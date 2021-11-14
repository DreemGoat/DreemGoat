import os
import re
os.chdir("/Users/dep50/OneDrive/Documents/Coding Projects/DreemGoat/Week 7")
file = open("Poems of Arthur Hugh Clough.txt","r")
def hapax(file):
    words = re.findall('\w+', file.read().lower())
    freq = {key: 0 for key in words}
    for word in words:
        freq[word] += 1
    for word in freq:
        if freq[word] == 1:
            print(word)


hapax(file)
file.close