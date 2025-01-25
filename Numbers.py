# Python is a powerful number crunching tool that can be used to perform complex calculations with ease.

# simple math
print(2 + 2)
print(2 - 2)

# operations
print('cup'+'cake') # cupcake
print('cup'*3) # cupcupcup

# python system
x= 2
y= 3
z=4
x,y,z # (2, 3, 4) # tuple # why 
# because of the comma (,) operator. The comma operator is used to create a tuple of multiple values. In this case, the values are 2, 3, and 4. The values are then assigned to the variables x, y, and z, respectively.

print(2**3) # 8
print(2 ** 100) # 1267650600228229401496703205376
print(10 % 3) # 1

# ===================  floor division operator ==========================
print(10 // 3) # 3
# The floor division operator (//) in Python performs division but instead of giving the exact result (which can be a floating-point number), it gives the largest whole number that is less than or equal to the result. This is called "flooring" the result.

# Example: 10 // 3
# Regular Division (/):
# If you do 10 / 3, you get 3.3333.... This is the exact result of the division.

# Floor Division (//):
# When you use 10 // 3, it takes the result of the division (3.3333...) and rounds it down to the nearest whole number. The result is 3




# sepical typenumber handeling 
complexNum = 1 + 2j #  complx Number
print(type(complexNum)) # <class 'complex'>

# Decimal
from decimal import Decimal
print(0.1 + 0.2) # 0.30000000000000004
print(Decimal('0.1') + Decimal('0.2')) # 0.3

(0.1 + 0.1 + 0.1) -3 # 5.551115123125783e-17
# SOlution
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # 0

# float
print(float(2.5) + float(5)) #  7.5
print(float(40)) # 40.0 

# round
print(round(6.6)) # 7
print(round(6.4)) # 6

#  =================== random ========================== 
import random
# random number
print(random.random()) # 0 to 1
print(random.randint(1, 10)) # 1 to 10

# random choice
li= ['apple', 'banana', 'cherry']
print(random.choice(li)) # gives random choice from list

#random shuffle (shuffle the list randomly)
l2=[1,2,3]
random.shuffle(l2) # [3, 1, 2] 

##################################################################
# =================== math module ==========================
import math

print(math.floor(2.9)) # 2
print(math.floor(-2.9)) # -3
#truncate
print(math.trunc(2.9)) # 2
print(math.trunc(-2.9)) # -2 
 # ceil (round a number up to the nearest whole number)
print(math.ceil(2.1)) # 3
print(math.ceil(-2.1)) # -2
 # square root
print(math.sqrt(16)) # 4.0
# power
print(math.pow(2, 3)) # 8.0
# pi
print(round(math.pi)) # 3.141592653589793
print(round(math.pi,2)) # 3.14



# sets
my_set = {1,2,3}
# operatoins
# ===> union
my_set & {3,4,5} # {3}
# ===> intersection
my_set | {3,4,5} # {1, 2, 3, 4, 5}
# ===> difference
my_set - {3,4,5} # {1, 2}
my_set - {1,2,3} # set()

#the result is set() not {} (empty set) because type of {} id dictory 



True == 1 # True
False == 0 # True

True + True # 2
False + False # 0

True +1 # 2
False + 1 #