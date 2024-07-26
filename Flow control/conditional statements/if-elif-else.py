'''
----->if-elif-else:
--------------------
	if condition-1:
		Action-1
	elif condition-2:
		Action-2
	elif condition-3:
		Action-3
	else:
		Default Action

-->Based on condition the corresponding action will be executed.

'''
# Ex-1

brand = input("Enter brand name: ")
if brand == 'samsung':
    print("I have samsung mobile")
    print("I have all models")
elif brand == 'iphone':
    print("I have iphone mobile")
    print("I am using since 2 years")
elif brand == 'vivo':
    print("I have vivo mobile")
    print("camera quality good")
else:
    print("I dont have that brand")

# Ex-2

marks = eval(input("Enter your marks: "))
if marks >= 90:
    print("You got A grade")
    print("You are very good")
elif marks >= 80:   
    print("You got B grade")
    print("You are good")
elif marks >= 70:
    print("You got C grade")
    print("You are average")
elif marks >= 60:
    print("You got D grade")
    print("You are poor")
else:
    print("You are fail")
    print("You need to work hard")

# Ex-3

n1 = eval(input("Enter first number: "))
n2 = eval(input("Enter second number: "))
n3 = eval(input("Enter third number: "))

if n1 > n2 and n1 > n3:
    print("Biggest number is:" ,n1)
elif n2 > n1 and n2 > n3:
    print("Biggest number: " ,n2)
else:
    print("Biggest number: " ,n3)