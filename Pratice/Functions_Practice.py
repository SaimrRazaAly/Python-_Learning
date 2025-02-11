# Function Syntax and its use
# def name(parametes):

#Programs

#  Q1:(Write a program to calculate the cube of it)

def Square(number):
    return number **3

Squared_Number = Square(2)
print(Squared_Number)


# Q2 Write a program that gives sum of two numbers

def Add_Two_Num(a,b):
    return a+b
print(Add_Two_Num(5,6)) # 11
print(Add_Two_Num("5","6")) #56

# Q3 Make a program that gives Circumfarece and area of cirlce when radius is given
import math 

def Circle_opeation(radius):
    area = math.pi * (radius ** 2)
    circumference = (2 * math.pi) * radius
    return area ,circumference

a,c = Circle_opeation(41)

print("the area is,",round(a,1),"\nthe cercomferece is ,", round(c,1),)


# make a funciton with default parameter 

def Greeting (name="saim"):
    print(f"hi {name} !")
    
Greeting()    
Greeting("ali")    


# functiion with *args

def Give_Me_Numbers(*args):
    # return sum(args)
    # or
     print(args)
     for i in args:
         print(i * 2)
     return sum(args)

    
print(Give_Me_Numbers(1,2,3))   
# print(Give_Me_Numbers(1,2,3,6,7,8,8))   


# functoin with keyword arguments

def Greeting(name,age):
    print(f"Name:",name,"Age:",age)

print(Greeting(name="saim",age=23))
print(Greeting(age=23,name="saim"))
# print(Greeting(age=23,name="saim",gender="male")) # error

# so inorder to fix it we use keyword arguments

def Greeting(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

print(Greeting(age=23,name="saim",gender="male")) # 