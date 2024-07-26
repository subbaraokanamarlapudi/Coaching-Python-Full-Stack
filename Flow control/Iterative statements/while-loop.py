'''
2).while loop:
-------------------
-->If we want to execute a group of statements iteratively until some condition False, then we should go for while loop.

Syn:
		while condition:
			body

Ex:To print numbers from 1 to 10 by using while loop
--------------------------------------------------------------------------------
x = 1
while x <= 10:
	print(x)
	x += 1

'''

# Ex-1 To print numbers from 1 to 10 by using while loop.
# x = 1
# while x <= 10:
# 	print(x)
# 	x += 1
	
# ---> If x+=1 is not there , the program goes into the infinite loop. If we want to stop the infinite loop just apply the "ctrl+c". It gives the keyboard interpution.

# Ex-2 To print the sum of first n numbers by using while loop.

# n = eval(input("Enter a number: "))
# sum = 0
# x = 1

# while x<=n:
# 	sum += x
# 	x += 1
# print("The sum of first",n,"numbers is:",sum)

# Ex-3 To print the multiplication table by using while loop.

# n = eval(input("Enter a number: "))
# x = 1
# while x<=10:
#     print(n,'*',x,'=',n*x)
#     x += 1

# Ex-4 w.a.p to prompt user to enter some name until entering 'sunny'
# name = ""
# while name != 'sunny':
# 	name = input("Enter your name: ")
# 	print("Welcome",name)
# print("Thank you")

# Ex-5: w.a.p to prompt user to enter name & pwd until 'mahesh' & 'sunny'

# name = ''
# pwd = ''
# while name != 'mahesh' or pwd != 'sunny':
# 	name = input('Enter Correct Name:')
# 	pwd = input('Enter Correct Pwd:')
# print('Thanks for confirmation')

# Ex-6
n=6
while n>0:
    print(n)
    n-=2 if n%3==0 else 1