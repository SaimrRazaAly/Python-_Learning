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


# Food Ripness Checker 
banana = "green"

if banana == "green":
    print("UnRipe ")
elif banana == "yellow":
    print("Ripe")
else:
    print("OverRipe ")

# Activity Sugesstion using Weather

Weather = "sunny"

if Weather == "sunny":
    print("Go for a walk")
elif Weather == "rainy":
    print("Read a book")
else:
    print("Build a snowMan")
    
# Taxi Provider
distance = "4"

if distance != int:
    print("Please Enter a distacne in the form of integer not need to give KM with it ")
    exit()
    
action = ""
if distance <=3 and distance > 0:
    action = "Walk"
elif distance >3 and distance < 15:
    action="BiceCycle"
elif distance >= 15:
    action = "Car"
else:
    action = "Dont go any where stay at home "

if distance < 0 :
    print(action)
else:
    print(f"go with {action}")
    
# Password stength checker
password= "Asdfiuoi"
Strength = ""
length = len(password)

if length < 6 and length >0 :
    Strength = "Weak"
elif length >=6 and length <10 :
    Strength = "Medium"
else:
    Strength = "Strong"
    
print("Your password is",Strength,"with",length,"Characters")