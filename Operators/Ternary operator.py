'''
In java we can use:
	x = (condition)?first value:second value

Ex:
	x = (10<20)?30:40
	print(x)

-->In python we can use:
			x = first value if condition else second value.
Ex:
	x = 30 if 10<20 else 40
	x #30
	x = 30 if 10>20 else 40
	x #40

-->first value if condition-1 else second value if condition-2 else third value

x = 10 if 20<30 else 40 if 50<60 else 70
x #10
x = 10 if 20>30 else 40 if 50<60 else 70
x #40
x = 10 if 20>30 else 40 if 50>60 else 70
x #70

'''

x = 10 if 20<30 else 40
print(x)

y = 10 if 20>30 else 50
print(y)

z = 10 if 20>30 else 40 if 50<60 else 70
print(z)

a = 10 if 20>30 else 40 if 50>60 else 70
print(a)

b = 10 if 20<30 else 40 if 50>60 else 70
print(b)

c = 10 if 20>30 else 40 if 50>60 else 70
print(c)