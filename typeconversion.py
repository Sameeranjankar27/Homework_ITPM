# type conversion


a = 5 + 3j
b= 5.7
c= 5

x= float(c)
y= complex(c)
z= int(b)

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))


a1=str('strrrr')
a2= str(3.0)
a3= str(5)

print(a1  , '\n',a2,'\n',a3)   # how it supposed to modify



my_set = {1, 2, 3}  # Set: Unordered and unique values
my_tuple = (1, 2, 3)  # Tuple: Ordered and immutable
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Dictionary: Key-value pairs
my_list = [1, 2, 3]  # List: Ordered and mutable

# Printing all
print("Set:", my_set)
print("Tuple:", my_tuple)
print("Dictionary:", my_dict)
print("List:", my_list)