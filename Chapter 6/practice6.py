# Write a program to find the multiplication table of any number using while loop.

n=int(input("Enter a number:"))
i=1

while i<=10:
    print(f"{n} x {i} = {n*i}")
    i=i+1