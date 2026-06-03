# Write a program to read a text from a given file certificate.txt and find whether it contains the word live.

file = open("certificate.txt", "r")
dataOfFile = file.read()
file.close()

dataOfFile = dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes, the word 'live' is present in the file.")
else:
    print("No, the word 'live' is not present in the file.")
    
    file.close()
    
    
