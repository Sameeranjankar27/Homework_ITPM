#       Date : 21/11/2024

# 1. positive , negative or zero
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. even and odd
num =3
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Grade cheaker
percent = 70
if 90 <= percent <= 100:
    print("Grade: A")
elif 70 <= percent < 90:
    print("Grade: B")
elif 50 <= percent < 70:
    print("Grade: C")
else:
    print("Grade: F")


# 4. cheak divisibility 
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")


# 5. Min number between two
a = 30
b = 12
print("Smaller number is:", a if a < b else b)



# 6. Max in 3 digits
a = 30
b = 15
c = 40

if a > b:
    if a > c:
        print("Largest:")
    else:
        print("Largest:")
else:
    if b > c:
        print("Largest:")
    else:
        print("Largest:")





# 7. cheak leap year
year = 2014
if (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")



# 8. Nested temp cheak
t1 = 32
if t1 < 15:
    print("Cold")
elif 15 <= t1 <= 30:
    print("Warm")
else:
    print("Hot")




# 9 . vowels and consolents
b1 = "a"
if b1 in 'aeiou':
    print("Vowel")
else:
    print("Consonant")




# 10 . Driving eligibility
age = 42
license = "yes"
if age >= 18:
    if license == "yes":
        print("Eligible to drive")
    else:
        print("Not eligible to drive (no license)")
else:
    print("Not eligible to drive (underage)")






# 11. Traingle validation
a = 32
b = 33
c = 34
if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")



# 12.  Calculate tax based on salary
salary = 23400
if salary <= 500000:
    print("Tax: ", salary * 0.05)
elif salary <= 1000000:
    print("Tax: ", salary * 0.10)
else:
    print("Tax: ", salary * 0.20)






# 13. Categorize age
age = 32
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")







# 14 . logical and cheak
num = 34
if num > 10 and num % 2 == 0:
    print("Condition satisfied")
else:
    print("Condition not satisfied")





# 15 .  Logical OR check
num = 35
if num < 5 or num > 20:
    print("Condition satisfied")
else:
    print("Condition not satisfied")





#16. Electricity bill
units = 67
if units <= 100:
    print("5 rs unit") 
elif units <= 200:
    print("10 rs unit") 
else:
    print("15 rs unit") 





# 17. Season finder
month = "jan"
if month in ['dec', 'jan', 'feb']:
    print("Season: Winter")
elif month in ['march', 'april', 'may']:
    print("Season: Spring")
elif month in ['june', 'july', 'august']:
    print("Season: Summer")
elif month in ['september', 'october', 'november']:
    print("Season: Autumn")
else:
    print("Invalid month")






# 18. Password validation
password = "234682771@"
if len(password) >= 8 and '@' in password:
    print("Valid password")
else:
    print("Invalid password")





# 19. Categorize BMI
bmi = 32
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")






#20. Character type checker
char = "67"
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")