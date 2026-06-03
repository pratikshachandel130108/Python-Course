# Question on Slicing
# take input and print the middle 3 characters and the last 2 characters.

str=input("Enter the Value:")
mid=len(str)//2
output1=str[mid-1:mid+2]
print(output1)

output2=str[-2:]
print(output2)