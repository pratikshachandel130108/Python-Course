# tuple basics

myTuple=(78,90,75)
StudentTuple=("Khushi","Divya","Ishank","Ayush","Ayush")

#StudentTupletudentTuple[1]="Pratiksha"   #Assignment error tuples are imutable.

print(StudentTuple[2])

# Empty Tuples
emptyTuple=()
singleTuple=(1)
print(type(emptyTuple))
print(type(singleTuple))
print(type(StudentTuple))

# Tuple Methods:-
print(StudentTuple.index("Khushi"))
print(StudentTuple.count("Ayush"))
print(StudentTuple.count("Divya"))
print(StudentTuple.count("Aditya"))