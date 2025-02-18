# how to create a class and object in python

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


Student_1 = Student("saim",16,"A ++")
print(Student_1.grade)

#  ==============================================================================================

# Q1 (Create a CAR class with attributes like name,model)

# its first letter should be Capital 
class Car:
    def __init__(self,brand,model):
        self.barnd = brand
        self.model = model 
        
Car_1 = Car("Toyota","2020")

# ================================================================================================
# Q2 (Create a class with a method that returns the full name of the car including (Brand and model))

class Car:
    def __init__(self,brand,model):
        self.barnd = brand
        self.model = model 
    
    def full_name(self):
        return f"{self.barnd} {self.model}"
    
Tesla = Car("Tesla","Model S")
print(Tesla.full_name())