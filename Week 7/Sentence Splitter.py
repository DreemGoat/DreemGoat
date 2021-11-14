import os
import re
os.chdir("/Users/dep50/OneDrive/Documents/Coding Projects/DreemGoat/Week 7")
file = open("Miyagi.txt","r")
a = file.read()
sentence = re.sub(r'\n','', a) 
sentence = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentence)
sentence = re.sub(r'\?\s', '?\n', sentence) 
sentence = re.sub(r'!\s', '!\n', sentence) 
print(sentence)
file.close