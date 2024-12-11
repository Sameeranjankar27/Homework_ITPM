#Modification of string
s= "I am student"
print(s.replace("student", "Tech"))

adress =  "123 suhana apt, marathali, Bangalore"
print(adress.replace("apt", "main ho don"))

text = "bbt kki lio"
print(text.replace("bbt", "okay hie").replace("kki", "bye").replace("lio","myself you"))


a=text.upper()
b=text.lower()
c=text.title()
print(a,b,c)

p1="Akod OKJsuwdb"
print(p1.swapcase())

print("Akod" in p1)



email = "ajay12345gmail.com"
if "@" in email:
    print("valid email")
else:
    print("Invalid")


a1= "   I    am   sameer"
print(a1.strip())



str1 = "HELLO"
str2 = "hello"

print(str1.lower() == str2.upper())


###
reg_username = ["azad", "azad","azad"]
new_user = "azad1"
if new_user in reg_username:
    print("already in use")
else:
    print("username is available")


###
names = ["KKHH", "Magic", "Hello", "Magic"]
sorted(names)

#
input_str = "       azad        "
print(input_str.strip())
print(input_str.lstrip())
print(len(input_str.lstrip()))
print(input_str.rstrip())
print(len(input_str.rstrip()))


data = "Ajay, data science, teacher"
print(data.split("a"))



address = """123, sanmukha villa, \nmarathali,  \nbangalore """         # new line
print(address)

