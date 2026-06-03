# take 3 food from the user and store in a list print list and its length.

food1=input("Enter the name of food 1:")
food2=input("Enter the name of food 2:")
food3=input("Enter the name of food 3:")
foodList=[food1,food2,food3]
print(foodList)
print(len(foodList))

# Another Method
food1=input("Enter food 1:")
food2=input("Enter food 2:")
food3=input("Enter food 3:")
foodList=[]
foodList.append(food1)
foodList.append(food2)
foodList.append(food3)
print(foodList)
print(len(foodList))