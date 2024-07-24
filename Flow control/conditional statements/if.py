'''
1.Conditional statements:
=======================
1).if:
		if condition:statement
or
		if condition:
			stmt-1
			stmt-2
			stmt-3

-->If condition is True then statements will be executed.

name = input('Enter Name:')
if name == 'sunny':
	print('Hello sunny good evening')
print('How r u?')

'''

# Ex

name = input("Enter a name: ")
if name == 'sunny':
    print('Hello sunny good evening')
print('How r u?')

age = eval(input("Enter your age: "))
if age>=18:
    print("your can vote now")
    print("you are adult")
print("sorry boss you are not eligible anything")