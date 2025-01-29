# Dictonary

#declaration
my_dictonary = {
    'name':'saim',
    'age':20,
    'status':'unmaried',
    'street':606
}
print(my_dictonary)
# Access and Value
print(my_dictonary['name']) # saim
print(my_dictonary['age']) # 20
print(my_dictonary['status']) #unmaried

print(my_dictonary.get('name')) # saim
print(my_dictonary.get('age')) # 20
print(my_dictonary.get('status')) #unmaried

# Difference Between [] and .

# print(my_dictonary.get('a')) #None
# print(my_dictonary['a']) # Gives Error
  
# Adding a value
my_dictonary['gender'] = "male" 
print(my_dictonary) # {'name': 'saim', 'age': 20, 'status': 'unmaried', 'gender': 'male'}

#================================= METHOD  =============================
keys = my_dictonary.keys()  # Get all keys
values = my_dictonary.values()  # Get all values
items = my_dictonary.items()  # Get key-value pairs
print(keys)
print(values)
print(items)

#Removing items:
my_dictonary.pop('status')  # Remove by key
# print(my_dictonary)
my_dictonary["live"] = True
my_dictonary.popitem() # it will delte this live:Ture
print(my_dictonary)
del my_dictonary["age"]  # Delete by key
# print(my_dictonary)
my_dictonary.clear()  # Remove all items



#Looping
new_Dict = {'username':'Ali','Role':'WEb developer', "postion":'Entery Level'}
for val in new_Dict:
    # print(val) # to print key only
    print(f'{val} : {new_Dict[val]}') # to print keys and values
    
# Both are same
for key,val in new_Dict.items():
    print(key,val)
    

# Advance
list  = ["car","bike","laptop"]
owner = "saim"

# Now make a dictonary 
#solutoin
new_Dict_onwer = dict.fromkeys(list,owner)
print(new_Dict_onwer) #{'car': 'saim', 'bike': 'saim', 'laptop': 'saim'}

#conditonal 
if "car" in new_Dict_onwer:
    print("saim  is the owner of all the prodcuts")