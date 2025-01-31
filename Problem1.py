# Q1: we have to make a program that sperate the age group

# age = int(input("Enter you age"))

# if  age <13:
#     print("Child:")
# elif age < 20:
#     print("Teenager:")
# elif age < 60:
#     print("Adult")
# elif age > 60:
#     print("Senior")
# else:
#     print("Please Enter a vaild age")
    
# Ticket Discount Provider
age = 20
wednesday = False
price = 12 if age>=18 else 8
if wednesday:
    price += 2
    
print(f'Ticket Price is ${price}')

# Grade Assiging Problem
Marks = 0
Grade = ""
if Marks >=90 and Marks <=100:
    Grade="A++"
elif Marks >=80 and Marks< 90:
    Grade= "A+"
elif Marks >=70 and Marks <80:
    Grade= "A"
elif Marks >=60 and Marks <70:
    Grade= "B"
elif Marks >=50 and Marks <60:
    Grade= "C"
else:
    Grade="FAIL"
    
print(f"your Grade is {Grade}")