# With KeyWord

with open("report.txt","r") as f:
    data=f.read()
    print("File Data:",data)
    
# Read line by line.

with open("newTextfile.txt","r") as f:
    line1=f.readline()    
    line2=f.readline()
    line3=f.readline()
    print(line1)
    print(line2)
    print(line3)
    