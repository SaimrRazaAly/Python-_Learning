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