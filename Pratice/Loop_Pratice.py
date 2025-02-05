# Give me Positive numbers
my_num = [1,2,3,4,-2,-1,]
Positive_Num= []
Positive_Num_Count = 0
for P_num in my_num:
    if P_num > 0:
        print(P_num)
        Positive_Num.append(P_num)
        Positive_Num_Count +=1
print(Positive_Num)
print("the postive numebrs are ",Positive_Num_Count)

# sum of Even Numbers Upto n
n = 10
Even_Number_Count = 0

for i in range(1,n+1):
    if i%2 == 0:
        Even_Number_Count = Even_Number_Count + 1

print(Even_Number_Count)

# Table Priter to 10 but reomv 5 iterarion
num = 5
remove_iteration = 5
for number in range(1,11):
    if remove_iteration == number:
        continue
    else:
        print(number,"X",num,"=",num*number)

# Reverse a string using loops
name = "saim"
reverse_Name =''
for i in name:
    reverse_Name = i + reverse_Name

print(reverse_Name)

# Print First None Repeating Character in sring 
string = "yahyaoo"

for car in string:
    if string.count(car) == 1:
        print("the fist none repertaing charater is :" , car)
        break
      

# Calculating Factrorial of a number using while loop

number  = 5
facorial = 1

while number > 0:
    facorial = facorial * 5
    number = number - 1 
print(facorial)

# take input from user until he enters a number between 1 or 10
UserInput = int(input("Enter a number btw 1/10 : "))

while True:
    if(UserInput >= 1 and UserInput <= 10):
        print("DONE")
        break
    else:
        UserInput = int(input("Enter a number btw 1/10 : "))



# Calculate Prime Number
number = 17
is_Prime = True

if number >= 1:
    for i in range(2,number):
        if number % i == 0:
            is_Prime = False
            break
print(is_Prime)