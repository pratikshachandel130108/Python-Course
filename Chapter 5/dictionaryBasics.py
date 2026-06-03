# Dictionary Basics
student={
    "name": "Pratiksha",
    "city": "New Delhi",
    "age": 18,
    "rollNumber": 29,
    "name":"Aakash",
    "rollNumber": 12
} 
print(type(student))   
print(student["name"])   # last occurence occurs i.e.Aakash
print(student["rollNumber"])
print(student)

# Accessing Values
print(student["city"])

# Adding Or Updating Values
student["city"]="Bangalore"
print(student)
student["favSubject"]="English"
print(student)

#Removing Items
student.pop("favSubject")
print(student)