# Create class Student that takes 3 marks and has a method average().

class Student:

    def __init__(self, name, listOfmarks):
        self.name = name
        self.listOfmarks = listOfmarks

    def average(self):      # Same indentation level as __init__
        total = 0

        for value in self.listOfmarks:
            total += value

        average = total / len(self.listOfmarks)
        print("Average is:", average)


student1 = Student("Aditya", [90, 98, 99])
student1.average()







        
        

