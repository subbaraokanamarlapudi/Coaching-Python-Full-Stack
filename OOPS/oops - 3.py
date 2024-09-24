'''
POLYMORPHISM :
--------------
* Poly means Many
* Morphs means Forms
* Polymorphism means 'Many Forms'

Ex:
	Yourself is best example for polymorphism
	Vikram-->Aparichithudu

    
1).Duck Typing philosophy of python
2).Overloading:
		-->Operator overloading
		-->Method overloading
		-->Constructor overloading
3).Overriding:
		-->Method overriding
		-->Constructor overriding
'''

'''
1).Duck Typing philosophy of python
--------------------------------------
* In python we cannot specify the type explicitly.
* Based on provides value at runtime the type will be considerd automatically.
* Hence python is considered as dynamically typed programming language.

        def f1(obj):
            obj.talk()

What is the type of obj?
-------------------------
* We cannot decide at the beginning. At runtime we can pass any type. Then how we can decide the type.
* At runtime if 'it walks like a duck and talks like a duck,it must be duck'.
* Python follows this principle. This is called as Duck Typing philosophy of python

'''

# Examople

# class Duck:
#     def talk(self):
#         print('Quack...... Quack.......')

# class Dog:
#     def bark(self):
#         print('Bow........... Bow........')

# class Cat:
#     def talk(self):
#         print('Meow........ Meow........')

# class Goat:
#     def talk(self):
#         print('Myaahh........ Myaahh........')

# def f1(obj):
#     obj.talk()

# l=[Duck(),Dog(),Cat(),Goat()]
# for obj in l:
#     f1(obj)

# -->The problem in this approach is if obj does not contain talk() method then we will get AttributeError.
# 			AttributeError: 'Dog' object has no attribute 'talk'
# -->We can solve this problem by using hasattr() function.
# 					hasattr(obj,'attributename')
# -->attributename can be method name or variable name.

# Example

# class Dog:
# 	def bark(self):
# 		print('Bow...Bow...')
# class Human:
# 	def talk(self):
# 		print('Hello...Hi.....')

# def f1(obj):
# 	if hasattr(obj,'talk'):
# 		obj.talk()
# 	elif hasattr(obj,'bark'):
# 		obj.bark()

# l = [Dog(),Human()]
# for obj in l:
# 	f1(obj)

# Overloading:
# ===========
# 	We can use same operator or methods for different purposes.

# 1).Operator Overloading:
# 	We can use same operator for multiple purposes, which is nothing but operator overloading.

# Ex:
	# 10 + 20 #30
	# '10' + '20' #'1020'

# Ex:To use + operator for our class objects
# ---------------------------------------------------------------
class Book:
	def __init__(self,pages):
		self.pages = pages
b1 = Book(100)
b2 = Book(200)
print(b1 + b2)

# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

# -->We can overload + operator to work with Book objects also.
# -->For every operator magic methods are available. To overload any operator we have to override that method in our class.
# -->Internally + operator is implemented by using __add__() method. We have to override this method in our class.

# Ex:To overload + operator for our Book class objects
# -------------------------------------------------------------------------------
class Book:
	def __init__(self,pages):
		self.pages = pages
	def __add__(self,other):
		return self.pages + other.pages
b1 = Book(100)
b2 = Book(200)
print('The total number of pages:',b1 + b2)

# How to add multiple objects
# ------------------------------------------
class Book:
	def __init__(self,pages):
		self.pages = pages
	def __add__(self,other):
		print('add method calling')
		total = self.pages + other.pages
		return Book(total)
	def __str__(self):
		return str(self.pages)
b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
bx = b1 + b2 + b3
#print(bx.pages)
print(bx)

# Ex:To overload multiplication operator to work on Employee objects
# ------------------------------------------------------------------------------------------------------
class Employee:
	def __init__(self,name,sal):
		self.name = name
		self.sal = sal
	def __mul__(self,other):
		return self.sal * other.days
class TimeSheet:
	def __init__(self,name,days):
		self.name = name
		self.days = days
	def __mul__(self,other):
		return self.days * other.sal
e = Employee('Sunny',800)
t = TimeSheet('Sunny',25)
print('This month salary:',e * t)
print('This month salary:',t * e)


# 2. Method Overloading:
# --------------------------
# * If the 2-methods having same name but different type of args then those methods are said to be overloaded methods.

# Ex:
# 		m1(int a)
# 		m1(float a)

# * But in python method overloading is not possible.
# * If we are trying to declare multiple methods with same name and different type of args then python will always consider only last method.

# Ex:

class Test:
    def m1(self):
        print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')

t = Test()
t.m1() #Test.m1() missing 2 required positional arguments: 'a' and 'b'
t.m1(10) #Test.m1() missing 1 required positional argument: 'b'
t.m1(10,20) #two-args method

# How we can handle overloaded method requirement in python:
# ------------------------------------------------------------
# * Most of the times, if method with number of args required then we can handle with default args or with variable number of args methods. 

class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('The sum of 3 numbers:',a+b+c)
        elif a!=None and b!=None:
            print('The sum of 2 numbers:',a+b)
        else:
            print('Please provide 2 or 3 arguments')

t = Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)
t.sum()

# Ex:with variable number of args
# ------------------------------------------------
class Test:
	def sum(self,*a):
		total = 0
		for x in a:
			total += x
		print('The sum is:',total)
t = Test()
t.sum(10,20,30)
t.sum()
t.sum(10)
t.sum(1,2,3,4,5,6,7,8,9)

# 3).Constructor Overloading:
# -----------------------------------------
# -->Constructor overloading is not possible in python.
# -->If we define multiple constructor then the last condtructor will be considered.

class Test:
	def __init__(self):
		print('No-Arg constructor')
	def __init__(self,a):
		print('One-Args constructor')
	def __init__(self,a,b):
		print('Two-Args constructor')
t = Test()#Invalid
t = Test(10)#Invalid
t = Test(10,20)#Valid

# -->But based on our requirement we can declare constructor with default args and variable number of args.

# Ex:Constructor with default args
# -------------------------------------------------
class Test:
	def __init__(self,a=None,b=None,c=None):
		print('Constructor with 0|1|2|3 number of args')
t1 = Test(10,20,30)
t2 = Test()
t3 = Test(10,20)
t4 = Test(10)

# Ex:Constructor with variable number of args
# ------------------------------------------------------------------
class Test:
	def __init__(self,*a):
		print('Constructor with variable number of args')
t1 = Test(10,20,30,40,50,60)
t2 = Test()
t3 = Test(10,20)
t4 = Test(10)


# OVERRIDING:
# 1.Method overriding 
# 2.Constructor overriding


# 1).Method Overriding:
# ------------------------
# * Whatever members available in the parent class are by default available to the child class through inheritance. 
# * If the child class not satisifed with parent class implementation then child class is allowed to re-define that method in the child class based on its requirement.
# * This concept is called as overriding.
# * Overriding applicable for both method and constructor.

# Ex:

class P:
	def property(self):
		print('Gold+Land+Cash+Power')
	def marry(self):
		print('Appalamma')

class C(P):
	def marry(self):
		super().marry()
		print('Katrina Kaif')

c = C()
c.property()
c.marry()

# From overriding method of child class, we can call parent class method also by using super() method.

# Ex:Constructor overriding
# ----------------------------------------
class P:
	def __init__(self):
		print('Parent Constructor')
class C(P):
	def __init__(self):
		print('Child Constructor')
c = C()

# -->In the above example, if child class does not contain constructor then parent class constructor will be executed.

# -->From child class constructor we can call parent class constructor by using super() method.