# STRINGS 
# strings are immutable in python
n = 'good'
n[0] = 'b' # TypeError: 'str' object does not support item assignment

print("Hello, World!") # Hello, World!
print('Hello, World!') # Hello, World!
print('''Hello, World!''') # Hello, World!
print("""Hello, World!""") #  Hello, World!

name = "Ali"
age= 12
userinfo = f'user name is {name} and {age} years old' 

length = len(name) # 3

# qoute = "he said that "hard work is the key to success"" # SyntaxError: invalid syntax
qoute = 'he said that "hard work is the key to success"' 
qoute = "he said that \"hard work is the key to success\""

# Windows path
path = "C:\\Users\\Ali\\Desktop\\Python\\Strings.py"
path  = r"C:\Users\Ali\Desktop\Python\Strings.py" # r is used to make the string raw 

# string operations
# concatenation
print('cup'+'cake') # cupcake
print('cup'*3) # cupcupcup

# Methods
val = "Hello"
print(val.upper()) # HELLO
print(val.lower()) # hello
print(val.capitalize()) # Hello

# strip
val = "   Hello   "
print(val.strip()) # Hello

# replace
val = "Hello, World!"
print(val.replace('Hello', 'Python')) # Python, World!
print(val.replace('heli','pu')) # Hello, World!

# split
catagories = "Books, Movies, Music"
print(catagories.split(", ")) # ['Books', 'Movies', 'Music']

#find
val = "Hello, World!"
print(val.find('World')) # 7

#in
val = "Hello, World!"
print('World' in val) # True

# not in
val = "Hello, World!"
print('World' not in val) # False

# count
val = "Saim Raza Saim Ali"
print(val.count('Saim')) # 2

# string formatting
name = "Saim"
age = 50
result ="My name is {} and i am {} years old"
print(result.format(name,age)) # My name is Saim and i am 50 years old

# list to sring
li = ['apple', 'banana', 'cherry']
print("".join(li))
  

