# Week 1.3, Session 2: Word Counter
# List of text files
files = ["story1.txt","story2.txt","glasses.txt"]
#Count the world in each file
for filename in files :
    with open("story1.txt","r",encoding="utf-8")as file:
        text = file.read()
        word = txt.split()
        print(filename,":",len(words),"words")
# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210