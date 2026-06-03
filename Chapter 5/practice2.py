# You are  given a list of programing languages:-
#["Python","java","C++","Python","java","C"]
#Covert it into a set and print how many unique languages Divya knows.

programmingList=["Python","Java","C++","Python","Java","C"]
print(type(programmingList))

# How to convert a list into set

programmingSet=set(programmingList)
print(type(programmingSet))

print("Divya knows these 4 languages",len(programmingSet))
