# Read all lines method

with open("newTextFile.txt","r") as f:
    readLinesmethod=f.readlines()
    print(readLinesmethod)
    
    
# Question:- read only the first line of bio.txt .

with open("bio.txt","r") as f:
    line1=f.readline()
    print("Line 1 is",line1)    
    
# question: Print how many lines are present in notes.txt.

with open("notes.txt","r") as f:
    listOfLines=f.readlines()
    print("Output of readLines Function",listOfLines)
    print("Number of lines in notes.txt:", len(listOfLines))
        