import os
os.chdir("/Users/dep50/OneDrive/Documents/Coding Projects/DreemGoat/Week 7")
file = open("Miyagi.txt","r")
infut = file.read()
word = ""
for x in range(0, len(infut)): 
	if(word!="" or infut[x]!=" "): #this loop prints out the letters of the text file one by one
		word=word+infut[x]
	if (infut[x] == "!" or infut[x] == "?" or infut[x] == "."): #this checks for punctuation
		if(infut[x] == "."):
			if x+1>len(infut) or x+2>len(infut): #this checks if the loop has reached the end of the text file or not
				break
			elif (infut[x+1]==" " 
			and infut[x+2].isupper() 
			and word.split(" ")[len(word.split(" "))-1]!="Mr."  
			and word.split(" ")[len(word.split(" "))-1]!="Mrs." 
			and word.split(" ")[len(word.split(" "))-1]!="Dr." #word.split here checks the last word in the sentence, if it is Mr., Mrs or Dr. it is not considered the last word
			):
				print(word)
				word=""
		else:
			print(word) #when the code detects punctuation it will print the sentence 
			word=""
print(word)