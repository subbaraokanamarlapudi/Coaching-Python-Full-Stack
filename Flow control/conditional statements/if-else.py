'''
----> if -else:
----------------
	if condition:
		Action-1
	else:
		Action-2

-->If condition is True Action-1 will be executed otherwise Action-2 will be executed.

name = input('Enter Name:')
if name == 'sunny':
	print('Hello sunny good evening')
else:
	print('Hello guest good evening')
print('How r u?')

'''
# Ex-1

name = input("Enter a name: ")
if name == 'sunny':
    print('Hello sunny good evening')
else:
    print('Hello guest good evening')

# ex-2
age = eval(input("Enter your age: "))
if age>18 or age == 18:
    print("your can vote now")
    print("you are adult")
else:
    print("sorry boss you are not eligible anything")

# ex-3

username = eval(input("Enter username: "))
password = eval(input("Enter password: "))

if username == 'laptop' and password == 1230:
    print("Welcome boss")
else:
    print("Invalid username or password")