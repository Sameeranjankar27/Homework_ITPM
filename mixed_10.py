# What is the difference between a list and a tuple in Python? Provide examples.

a= [1,2,34,5,6,"str"]      # list
b = (1 ,2 , 3, 45)         # tuple

# cheak no positive , negatie or 0

b1 = 12

if b1 > 0:
    print("The number is positive.")
elif b1 < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# example of if- else and else if


marks = 49

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")




# take str from user and convert into int


user_input = input("Enter a number: ")
num = int(user_input)  # Convert to integer
print(num)