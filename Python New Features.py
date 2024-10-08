# The walrus operator:
# -------------------------

# * :=  ---> It is avaliable in plsql also.

# Python 3.8 version
# This operator released as the part of PEP 572.
# 		PEP-->Python Enhancement Proposals
# To assign values to the variables as the part of expression itself.

# Other meaning is:
# 	Assignment Expressions

# Ex : 1

l = [10,20,30,40,50]
if (n := len(l)) > 3:
    print('List contains more than 3 elements')
    print('The length of the list:',n)
print(n)

# Ex : 2

heroines = []
while (heroine := input('Enter your favourite heroine:')) != 'radhika':
    heroines.append(heroine)
print(heroines)

#Read data line by line from abc.txt file and print to the console
f = open('abc.txt')
while (line := f.readline()) != '':
	print(line,end='')
f.close()

# The main advantage of the walrus operator:
# -----------------------------------------------------------------
# It won't do any new thing.
# It just reduces length of the code and readability will be improved.


# Functions:
# 	-->positional
# 	-->keyword
# 	-->default
# 	-->variable length

def f1(*n):tuple
def f1(**n):dict

# keyword-only parameters:
# ---------------------------------------
# After *, all parameters become keyword-only parameters.
# At the time of calling we should pass values by keyword-only.

# Ex:
def f1(*,a,b):
	print(a,b)
f1(10,20)#Invalid
f1(10,b=20)#Invalid
f1(a=10,b=20)#Valid

# Python 3.0 version only

# Ex:def f1(a,*,b,c)
# --------------------------
# for a we can pass either by positional or keyword
# But b and c compulsory we should use keyword-only

def f1(a,*,b,c):
	print(a,b,c)
f1(50,b=30,c=40)#valid
f1(a=50,b=30,c=40)#valid
f1(50,30,c=40)#invalid

# Ex:
def f1(*,a=10,b=20):
	print(a,b)
f1()#Valid
f1(30)#Invalid
f1(a=30)#Valid

# Ex:
# def f1(a,b,*):
# 	pass
# SyntaxError

# positional-only args:
# -------------------------------
# All parameters before /, will become positional-only parameters.

def f1(a,b,/):
	print(a,b)
f1(10,20)#Valid
f1(a=10,b=20)#Invalid

# Python 3.8 version as the part of PEP 570

# Ex:
def f1(a,b,/,c,d,*,e,f):
	print(a,b,c,d,e,f)

#a and b are positional-only parameters
#c and d positional-or-keyword parameters
#e and f are keyword-only parameters.

f1(10,20,30,d=40,e=50,f=60)
f1(10,20,30,40,e=50,f=60)
f1(10,20,c=30,d=40,e=50,f=60)
f1(10,b=20,c=30,d=40,e=50,f=60)#Invalid
f1(10,20,30,40,50,f=60)#Invalid

# Ex:
# def f1(*,a,b,c,/):
# 	print(a,b,c)
# SyntaxError: invalid syntax

# Note:
# 	f1(positional-only args,positional-or-keyword args,keyword-only args)

# positional-only vs keyword-only:
# ------------------------------------------------
# 1.If the paremeter names are not important and not having any meaning and there are only few parameters===>positional-only args

# 2.If parameter names having meaning and function implementation is more understandable with these names===>keyword-only args.

# f-strings or formatted string or Literal String Interpolation
# ---------------------------------------------------------------------------------------
# String formatting means inserting values and expressions in string literal

# 3-types of techniques
# --------------------------------
# 1. %-formatting
# 2. str.format() method
# 3. f-strings

# It is introduced in Python 3.6 version
# As the part of PEP 498
# The syntax is similar to str.format()
# It is more concise and more readable.
# Performace is more when compared with other 2-techniques.

# Ex:

name = 'Durga'
print('Hello %s good evening'%name)
print('Hello {} good evening'.format(name))
print(f'Hello {name} good evening')

# Note:
# 	We can use either f or F, we can use single quotes or double quotes or triple quotes also.

# Handling Quotes in f-string:
# -----------------------------------------
# o/p:the symbol ' is good

print(f"The symbol ' is good")
print(f'The symbol " is good')
print(f"The symbol \'  and \" are good")
print(f'''The symbol '  and " are good''')

# How to define multi line f-strings
# --------------------------------------------------
name = 'Mahesh'
age = 50
subject = 'Python'
msg = f'''
Name:{name}
Age:{age}
Subject:{subject}
'''
print(msg)

# f-string calling a function
# --------------------------------------
# We can call function directly from f-string

name = 'Mahesh'
print(f'Faculty Name:{name.upper()}')

# Ex:
def mymax(a,b,c):
	max = a if a>b and a>c else b if b>c else c
	return max
a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))
c = int(input('Enter 3rd number:'))
print(f'The maximum of {a},{b} and {c} is {mymax(a,b,c)}')

# f-strings for objects
# -----------------------------
# str.format() method will always call str() method only.
# But in f-string, we can call either str() and repr() based on our requirement.

class Student:
	def __init__(self,name,rollno,marks):
		self.name = name
		self.rollno = rollno
		self.marks = marks
	def __str__(self):
		return f'Name:{self.name},RollNo:{self.rollno},Marks:{self.marks}'
	def __repr__(self):
		return f'Student Name:{self.name},Student RollNo:{self.rollno},Student Marks:{self.marks}'
s = Student('Radhika',101,90)
print('Information--->{}'.format(s))
print(f'Information--->{s}')
print(f'Information--->{s!r}')

# Expressions inside f-string
# ----------------------------------------
a = 10
b = 20
c = 30
print(f'The Result:{10*20/3}')
print(f'The Result:{10*20/3:.2f}')
print(f'The Result:{a+b*c}')

# How to use crlry braces inside f-strings
# ------------------------------------------------------------
# o/p:  { is a special symbol

# print(f'{ is a special symbol')#SyntaxError: f-string: expecting '}'
# print(f'{{ is a special symbol')# { is a special symbol
# print(f'{{{ is a special symbol')#SyntaxError: f-string: expecting '}'
# print(f'{{{{ is a special symbol')# {{ is a special symbol

# o/p: } is a symbol

# print(f'} is a special symbol')#Invalid
# print(f'}} is a special symbol')#Valid
# print(f'}}} is a special symbol')#Invalid
# print(f'}}}} is a special symbol')#Valid

# Ex:
name = 'Sunny'
print(f'Name:{name}')#Name:Sunny
print(f'Name:{{name}}')#Name:{name}
print(f'Name:{{{name}}}')#Name:{Sunny}
print(f'Name:{{{{name}}}}')#Name:{{name}}

# 3.8 version
# ==========
# We can use = symbol inside f-string for self documenting expressions and it is very useful for debugging purpose.

x = 10
y = 20
#print(f'x = {x}')
#print(f'y = {y}')
print(f'{x=}')
print(f'{y=}')

# Aliasing & cloning
# ---------------------------
# Aliasing
# ------------
l1 = [10,20,30,40]
l2 = l1 #Aliasing
l1[0] = 100
print(f'l1:{l1}')
print(f'l2:{l2}')

# cloning
# -----------
l1 = [10,20,30,40]
#l2 = l1.copy()
l2 = l1[:]
l1[0] = 100
print(f'l1:{l1}')
print(f'l2:{l2}')

# Shallow cloning and Deep cloning
# --------------------------------------------------
# Aliasing---->Shallow Cloning
# Cloning--->Deep Cloning

# Shallow Cloning:
# -------------------------
import copy
l1 = [10,20,[30,40],50]
l2 = copy.copy(l1)
l2[2][0] = 333
print(f'l1:{l1}')#[10, 20, [333, 40], 50]
print(f'l2:{l2}')#[10, 20, [333, 40], 50]

# Deep Cloning:
# --------------------
import copy
l1 = [10,20,[30,40],50]
l2 = copy.deepcopy(l1)
l1[2][0] = 333
l2[2][1] = 999
print(f'l1:{l1}')#[10, 20, [333, 40], 50]
print(f'l2:{l2}')#[10, 20, [30, 999], 50]

# Shallow Cloning vs Deep Cloning:
# --------------------------------------------------
# If original object does not contain any nested objects then it is highly recommended to go for===>Shallow cloning.

# If original object contains any nested objects then we should go for==>deep cloning.