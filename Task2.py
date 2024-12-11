# deep copy and shallo copy

import copy
a= [1, "staring"]
deep= copy.deepcopy(a)
shallow= copy.copy(a)

#deep[0]= 2
#print(deep)
#print(a)

# shallow copy now change the orignal one
shallow[0]=4
#print(shallow)
print(a) 


original = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

shallow_copy[0][0] = 99
print(original)  # Output: [[99, 2], [3, 4]]
print(deep_copy)  # Output: [[1, 2], [3, 4]]


def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the original function.")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Original function executed.")

display()


def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example_function(1, 2, 3, name="Alice", age=30)