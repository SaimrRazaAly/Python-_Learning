# Tuples
# tuples are used becuase tuples are immatuable and list are mutable (can be change)

#syntax
my_Tuple = (1,2,3,4)
print(my_Tuple)
print(type(my_Tuple))

print(my_Tuple[0]) #1
# my_Tuple[0] = "56" 
# print(my_Tuple) # gives error

len(my_Tuple) # 4
my_Tuple = (1,2,3,4,4,4,4,4)
print(my_Tuple.count(4)) # 5 times

# loop
tple = ("125","CD","honda","Civic")
for num in tple:
    print(num)
    
if 2 in my_Tuple:
    print("i have 2")


#operaition

my_Tp1=("saim","Raza")
my_Tp2=("Pc","gaming")
new_tpl = my_Tp1 + my_Tp2
print(new_tpl)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(f'====================={mytuple} ==============================')

#impoertant
thistuple = ("apple",) #plase add ,
print(type(thistuple)) #Tuple

thistuple = ("apple") #not a tuple
print(type(thistuple))


# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # cherry

# *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
index = fruits.index("banana")
print(f'///////////////////////////////////{index}//////////////////////////')
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #['cherry', 'strawberry', 'raspberry']

