'''
Output Streams:
-------------------------
We can use print() function to display output

Form-1:print() without arg
-----------------------------------------
Just it prints new line character

Form-2:print(string)
------------------------------
print('Hello World')
print('Hello\nWorld')
print('Hello\tWorld')
print(5*'Hi ')
print('Hi '*5)
print('Hello'+'World')
print('Hello','World')

Form-3:print() with variable number of args
------------------------------------------------------------------
a,b,c = 10,20,30
print('The values are:',a,b,c)
	
-->Bydefault output values are separated by space. If we want we can specify separator by using 'sep' attribute.

a,b,c = 10,20,30
print(a,b,c,sep=':')
print(a,b,c,sep='-')

Form-4:print() with end attribute
--------------------------------------------------
print('Hello')
print('Radhika')
print('How r u?')

-->If we want output in the same line with space.

print('Hello',end=' ')
print('Radhika',end=' ')
print('How r u?')

Form-5:print(object) statement
-----------------------------------------------
We can pass any object(like list,tuple,set.....) as arg to the print.

Ex:
	l = [10,20,30]
	t = (10,20,30)
	print(l)
	print(t)

Form-6:print(string,variable list)
-------------------------------------------------
s = 'Mahesh'
a = 50
s1 = 'Python'
s2 = 'Django'
print('Hello',s,'your age is:',a)
print('You are teaching',s1,'and',s2)

Form-7:print(formatted string)
----------------------------------------------
%d-->int
%f-->float
%s-->string type

Syn:
		print('formatted string'%(variablelist))

a,b,c = 10,20,30
print('a value is %d'%a)
print('b value is %d and c value is %d'%(b,c))

Form-8:print() with replacement operator {}
------------------------------------------------------------------
name = 'Mahesh'
sal = 10000
gf = 'Sunny'
print('Hello {} your salary {} and your GF {} is waiting'.format(name,sal,gf))
print('Hello {0} your salary {1} and your GF {2} is waiting'.format(name,sal,gf))
print('Hello {n} your salary {s} and your GF {g} is waiting'.format(s=sal,g=gf,n=name))
'''

# Form-1

print("-----------FORM-1-----------")
print("Hello world")
print("vijay")
print("srikhar")

# Form-2

print("-----------FORM-2-----------")
print('Hello World')
print('Hello\nWorld')
print('Hello\tWorld')
print(5*'Hi ')
print('Hi '*5)
print('Hello'+'World')
print('Hello','World')

# Form-3
print("-----------FORM-3-----------")

a,b,c = 10,20,30
print('The values are:',a,b,c)

a,b,c = 10,20,30
print(a,b,c,sep=':')
print(a,b,c,sep='-')

# Form-4
print("-----------FORM-4-----------")

print('Hello')
print('Radhika')
print('How r u?')

# -->If we want output in the same line with space.

print('Hello',end=' ')
print('Radhika',end=' ')
print('How r u?')

# Form-5
print("-----------FORM-5-----------")

l = [10,20,30]
t = (10,20,30)
print(l)
print(t)

# Form-6
print("-----------FORM-6-----------")

s = 'Mahesh'
a = 50
s1 = 'Python'
s2 = 'Django'
print('Hello',s,'your age is:',a)
print('You are teaching',s1,'and',s2)

# Form-7
print("-----------FORM-7-----------")

a,b,c = 10,20,30
print('a value is %d'%a)
print('b value is %d and c value is %d'%(b,c))

# Form-8
print("-----------FORM-8-----------")

name = 'Mahesh'
sal = 10000
gf = 'Sunny'
print('Hello {} your salary {} and your GF {} is waiting'.format(name,sal,gf))
print('Hello {0} your salary {1} and your GF {2} is waiting'.format(name,sal,gf))
print('Hello {n} your salary {s} and your GF {g} is waiting'.format(s=sal,g=gf,n=name))
