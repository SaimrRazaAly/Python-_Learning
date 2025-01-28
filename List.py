# List 
# sytax

list = [1,2,3,4]
print(list) # [1, 2, 3, 4]

# Slicing And indexing 
print(list[:])
print(list[0:3]) #[1, 2, 3]
print(list[-1]) 

# methods
list.append(5) # add 5 to end
list.insert(1, 10)  # Add at index 1
print(list)
list.pop()#remomves the last element
values = ["mobile","car","laptop"]
values.remove("car")
print(values,len(values))
for val in values:
    print("this is my " + val)
    # print("this is my " + val ,end="-")
    
# List comprehension:
square_nums = [x**2 for x in range(6)]
print(square_nums) # [0, 1, 4, 9, 16, 25]
# range(6)
# [0,1,2,3,4,5]
zero_nums = [x-x for x in range(10)]
print(zero_nums) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Sorting:
whole = [1,2,3,20,100]
print(whole.sort()) # Ascending
print(whole.sort(reverse=True))  # Descending

print(whole.index(3))  # element at index 3 


my_list = [3, 1, 4, 2]

# Ascending
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

# Descending
my_list.sort(reverse=True)
print(my_list)  # Output: [4, 3, 2, 1]
