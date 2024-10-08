'''
What is a class?
-----------------
* In python everything is an object. To create objects we required some model or plan or blue print, which is nothing but a class.
* We can write a class to represent properties (attributes) and actions(behaviours) of an object.
* Properties can be represented by variables and actions can be represented by methods.
* Hence class contains both variables and methods.

How to define a class?
-----------------------
We can define by using class keyword.
Syn:
	class ClassName:
		"""documentation string"""
		variables:Instance, static and local variables
		methods:Instance,static and class methods

* Documentation string represents description of the class. within the class doc string is always optional. We can get doc string in 2-ways.

1.print(ClassName.__doc__)
							2.help(ClassName)
Ex:
class Student:
	"""This is student class with required data"""
print(Student.__doc__)
help(Student)


What is object?
----------------
* Physical existence of a class is nothing but object.
* We can create any number of objects for a class.
Syn:
			refvariable = Classname()
Ex:
			s = Student()

What is a Reference Variable?
------------------------------
* The variable which can be used to refer object is called reference variable.
* By using reference variable, we can access properties and methods of object.

'''

# Q : W.A.P to create a student class and creates an objects to it. Call the method display() to display the student details.

class Student:
    def __init__(self, name, rollno, marks):  
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Hello My Name Is:", self.name)
        print("My Roll No Is:", self.rollno)
        print("My Marks Are:", self.marks)


s = Student('sunny', 101, 98)
s.display()

# Self Variable : 
# -----------------

# self is a default variable which is always pointing to current object(like this keyword in java)
# By using self we can access instance variables and instance methods of objects.

# NOTE : 1).self should be first parameter inside constructor.
#           def __init__(self):
# 2) .self should be first parameter inside instance method.        def display(self):

'''
Constructor concept:
---------------------
* Constructor is a special method in python.
* The name of the constructor should be __init__(self).
* Constructor will be executed automatically at the time of object creation.
* The main purpose of constructor is to declare and initialize instance variable.
* Per object constructor will be executed only once.
* Constructor can take atleast one argument(atleast self).
* Constructor is optional and if we are not providing any constructor then python will provide default constructor.
'''

# EX : Program to demonstrate constructor will be executed only once per object
# ------------------------------------------------------------------------------------

class Test:
    def __init__(self):
        print("Constructor Execution...")
    def m1(self):
        print("Method Execution...")

t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()

# How to create list of objects in construcor
# ----------------------------------------------------------

class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

    def info(self):
        print("Movie Name:", self.name)
        print("Hero Name:", self.hero)
        print("Heroine Name:", self.heroine)
        print("Rating:", self.rating)
        print()

movies = [
    Movie('OG', 'Pawan Kalyan', 'Priyanka', 4.5),
    Movie('Kalki', 'Prabhas', 'Deepika', 4.2),
    Movie('Devara', 'JR. NTR', 'Janhavi Kapoor', 5.0)
]

for movie in movies:
    movie.info()

# without constructor:
# -------------------------------

class Movie:
	def info(self):
		print('Movie Name:',self.name)
		print('Hero Name:',self.hero)
m = Movie()
m.name = 'Devara'
m.hero = 'Jr NTR'
m.info()

# with normal method
# ------------------------------

class Movie:
	def vd(self,name,hero):
		self.name = name
		self.hero = hero
	def info(self):
		print('Movie Name:',self.name)
		print('Hero Name:',self.hero)
m = Movie()
m.vd('Maharaja','Vijay')
m.info()

'''
Difference between Method and Constructor?

Method:
-------
* Name of the method can be any name.
* Method will be executed, if we call that method.
* Per object, method can be called any number of times.
* Inside method we have to declare business logic.

Constructor:
-------------
* Constructor name should be __init__().
* constructor will be executed automatically at the time of objects creation.
* Per object, constructor will be executed only once.
* Inside constructor we can write and initilize instance variable.

Types of variables:
---------------------
1.Instance Variable (Object Level Variable)
2.Static Variable (Class Level Variable)
3.Local Variable (Method Level Variable)

1.Instance Variable:
---------------------
* If the value of a variable is varied from object to object then such type of variable are called as instance variables.
* For every object a separate copy of instance variables will be created.

Where we can declare instance variables:
------------------------------------------

1. Inside Constructor:
-----------------------
* We can declare instance variable inside constructor by using self.
* Once we create the object, automatically these variables will be added to the object.

2. Inside Instance Method:
---------------------------
* We can also declare instance variable inside method by using self.
* If any instance variable declared inside instance method, that instance variables will be added once we call that method.

3. Outside of the class:
-------------------------
* We can also add instance variables outside of the class to a particular object.
'''

# Inside constructor:

class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Durga'
        self.esal = 10000

e = Employee()
print(e.__dict__)

# Inside instance method:

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30

t = Test()
t.m1()
print(t.__dict__)


# Outside of the class:

class Test:
    pass
t = Test()
t.a = 10
t.b = 20
print(t.__dict__)

# How to access instance variables?
# ----------------------------------

#  We can access instance variable within the class by using 
# self variable and outside of the class by using object references

# Example : 

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def display(self):
        print(self.a)
        print(self.b)

t = Test()
t.display()
print(t.a)
print(t.b)

# How to delete instance variables from the object?
# --------------------------------------------------

# 1.Within a class we can delete instance variable by using self.
# 						del self.variable_name

# 2.From outside of a class we can delete instance variable as:
# 						def objectreference.variable_name

# Example:

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def m1(self):
        del self.c

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.b
print(t.__dict__)


# Note:
# 	The instance variables which are deleted from one object, will not be deleted from other object.

class Test:
	def __init__(self):
		self.a = 10
		self.b = 20
		self.c = 30
t1 = Test()
t2 = Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)

# -->If we change the values of instance variables of one object then those changes wont be reflected to the remaining objects, because for every object we have separate copy of instance variables are available.

class Test:
	def __init__(self):
		self.a = 10
		self.b = 20
t1 = Test()
t1.a = 333
t1.b = 999
t2 = Test()
print('t1:',t1.a,t1.b)
print('t2:',t2.a,t2.b)

'''
2. Static Variable:
--------------------
* If the value of a variable is not varied from object to object, such type of variable we have to declare within the class directly but outside of the methods.
  such type of variables are called as static variables.
* For total class only one copy of static variables will be created and shared by all the objects of that class.
* We can access static variables whether by className or by object reference. But recommended to use className.

Ex:
class Test:
	x = 10
	def __init__(self):
		self.y  = 20
print(Test.__dict__)

Types of variables:
---------------------
1.Instance Variable (Object Level Variable)
2.Static Variable (Class Level Variable)
3.Local Variable (Method Level Variable)

Instance variable vs static variable:
--------------------------------------
* In the case of instance variables for every object a separate copy will be created, but in the case of static variables for
  total class only one copy will be created and shared by every object of that class.

Example:
---------

class Test:
	x = 10
	def __init__(self):
		self.y = 20
t1 = Test()
t2 = Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x = 333
t1.y = 999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

Various places to declare static variables:
---------------------------------------------
* In general we can declare within the class directly but from outside of any method.
* Inside constructor by using class name.
* Inside instance method by using class name.
* Inside class method by using cls variable or class name.
* Inside static method by using class name.
* From outside of the class by using class name.

How to access static variables:
--------------------------------
* Inside constructor: By using either self or className.
* Inside instance method: By using either self or className.
* Inside class method: By using cls variable or className.
* Inside static method: By using className.
* From outside of the class: By using either className of object reference.
'''

class Test:
    x = 10
    def __init__(self):
        self.y = 20

print(Test.__dict__)

class Test:
	x = 10
	def __init__(self):
		self.y = 20
t1 = Test()
t2 = Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x = 333
t1.y = 999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# Various places to declare static variables
# Example :

class Test:
    a = 10
    def __init__(self):
        Test.b = 20
    def m1(self):
        Test.c = 30
    @classmethod
    def m2(cls):
        cls.d1 = 40
        Test.d2 = 50
    @staticmethod
    def m3():
        Test.e = 60

t = Test()
t.m1()
Test.m2()
Test.m3()
Test.f = 70
print(Test.__dict__)

# Accessing the static variables:
# Example :

class Test:
    a = 10  # Class variable

    def __init__(self):
        print(Test.a)  # Accessing class variable using class name
        print(self.a)   # Accessing class variable using 'self'

    def m1(self):
        print(Test.a)  # Accessing class variable using class name
        print(self.a)  # Accessing class variable using 'self'

    @classmethod
    def m2(cls):
        print(Test.a)  # Accessing class variable using class name
        print(cls.a)   # Accessing class variable using 'cls'

    @staticmethod
    def m3():
        print(Test.a)  # Accessing class variable using class name


# Creating an instance of the Test class
t = Test()

# Calling instance method
t.m1()

# Calling class method
t.m2()

# Calling static method
t.m3()

# Accessing class variable directly from the class
print(Test.a)


# Where we can modify the value of static variable:
# -------------------------------------------------------------------------
# Anywhere either within the class or outside of class we can modify by using ClassName. But inside classmethod by using cls variable.

class Test:
	a = 333
	@classmethod
	def m1(cls):
		cls.a = 666
	@staticmethod
	def m2():
		Test.a = 999
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)

# Note:
#  	If we change the value of static variable by using either self or object reference variable, then the value of static variable wont be changed, just a new instance variable with that name will be added to that particular object.

class Test:
	a = 10
	def m1(self):
		self.a = 333
t = Test()
t.m1()
print(Test.a)#10	
print(t.a)#333

# EX : 1

class Test:
	a = 10

	def __init__(self):
		self.b = 20
	def m1(self):
		self.a = 333
		self.b = 999

t1 = Test()
t2 = Test()
t1.m1()
print('t1:',t1.a,t1.b)#333 999
print('t2:',t2.a,t2.b)#10 20

# Ex:
class Test:
	a = 10
	def __init__(self):
		self.b = 20
	@classmethod
	def m1(cls):
		cls.a = 333
		cls.b = 999
t1 = Test()
t2 = Test()
t1.m1()
print('t1:',t1.a,t1.b)#333 20
print('t2:',t2.a,t2.b)#333 20
print(Test.a,Test.b)#333 999

# How to delete static variables of a class?
# ------------------------------------------------------------
# We can delete static variables from anywhere by using ClassName.
# 				del ClassName.variablename

# But inside classmethod we can also use cls variable.
# 				del cls.variablename
# Ex:

class Test:
	a = 10
	@classmethod
	def m1(cls):
		del cls.a
Test.m1()
print(Test.__dict__)

# Ex:
class Test:
	a = 10
	def __init__(self):
		Test.b = 20
		del Test.a
	def m1(self):
		Test.c = 30
		del Test.b
	@classmethod
	def m2(cls):
		Test.d = 40
		del Test.c
	@staticmethod
	def m3():
		Test.e = 50
		del Test.d
t = Test()
t.m1()
t.m2()
t.m3()
del Test.e
print(Test.__dict__)

# Note:
# 	By using object reference variable or self we can read static variables, but we cannot modify or delete.
	
# 	If we are trying to modify, then a new instance variable will be added to that particular object.
	
# 	If we are trying to delete then we will get an error.

# Ex:
class Test:
	a = 10
t = Test()
del t.a #AttributeError: a

# -->We can modify or delete static variables only by using ClassName od cls variable.

# Ex:
import sys
class Customer:
	'''Customer class with bank operations.....'''
	bank_name = 'SunnyBank'
	def __init__(self,name,balance=0.0):
		self.name = name
		self.balance = balance
	def deposit(self,amt):
		self.balance += amt
	def withdraw(self,amt):
		if amt > self.balance:
			print("Insufficient funds...can't perform this operation")
			sys.exit()
		self.balance -= amt
		print('Balance after withdraw:',self.balance)
print('Welcome to',Customer.bank_name)
name = input('Enter Your Name:')
c = Customer(name)
while True:
	print('d-Deposit\nw-Withdraw\ne-Exit')
	option = input('Enter your option:')
	if option == 'd' or option == 'D':
		amt = float(input('Enter amount:'))
		c.deposit(amt)
	elif option == 'w' or option == 'W':
		amt = float(input('Enter amount:'))
		c.withdraw(amt)
	elif option == 'e' or option == 'E':
		print('Thanks for Banking!!!!!!!!!!!')
		sys.exit()
	else:
		print('Invalid option.....Pls choose valid option')

# 3).Local Variables:
# ---------------------------
# -->Sometimes to meet temporary requirements of programmer, we can declare variables inside a method directly, such type of variables are called local variables or temporary variables.
# -->Local variables will be created at the time of method execution and destroyed once method completes.
# -->Local variables of a method cannot be accessed from outside of method.

# Ex:
class Test:
	def m1(self):
		a = 1000
		print(a)
	def m2(self):
		b = 2000
		print(b)
		print(a)#NameError: name 'a' is not defined
t = Test()
t.m1()
t.m2()


# Types of methods:
# 	1.Instance methods
# 	2.Class methods
# 	3.Static methods

# 1.Instance methods:
# -------------------------------
# -->Inside method implementation if we are using instance variables then such type of methods are called as instance methods. Inside instance method declaration, we have to pass self variable.
# 							def m1(self):
# -->By using self variable inside method we can able to access instance variables.
# -->Within the class we can call instance methods by using self variable and from outside of the class we can call by using object reference.

# Ex:

class Student:
	def __init__(self,name,marks):
		self.name = name
		self.marks = marks
	def display(self):
		print('Hi',self.name)
		print('Your marks are:',self.marks)
	def grade(self):
		if self.marks >= 60:
			print('You got First Grade')
		elif self.marks >= 50:
			print('You got Second Grade')
		elif self.marks >= 35:
			print('You got Third Grade')
		else:
			print('Congrats you are failed....')
n = int(input('Enter number of students:'))
for i in range(n):
	name = input('Enter Name:')
	marks = int(input('Enter Marks:'))
	s = Student(name,marks)
	s.display()
	s.grade()
	print()

# setter and getter methods:
# -------------------------------
# We can set and get the values of instance variable by using setter and getter methods.

#  setter method:
# ----------------------
# It can be used to set the instance variable, setter method also known as mutator method.
# Syn:
# 		def set_variable(self,variable):
# 			self.variable = variable

# Getter method:
# -----------------------
# 	It can be used to get values of the instance variables. Getter method also known as accessor method.
# Syn:
# 		def get_variable(self):
# 			return self.variable

# Examle on setter and getter method:
# -------------------------------------

class Student:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

l = []
n = int(input("Enter number of students: "))
for i in range(n):
    s = Student()
    name = input("Enter name: ")
    s.set_name(name)
    marks = int(input("Enter marks: "))
    s.set_marks(marks)
    l.append(s)

# Display details of all students
for s in l:
    print("Name:", s.get_name())
    print("Marks:", s.get_marks())
    print()
    
# 2).Class Methods:
# --------------------------
# -->Inside method implementation if we are using only class variables(static variables) then such type of methods we should declare as classmethod.
# -->We can declare classmethod explicitly by using @classmethod decorator. For classmethod we should provide cls variable at the time of declaration.
# -->We can call classmethod by using ClassName or object reference variable.

# Ex:
class Animal:
	legs = 4
	@classmethod
	def walk(cls,name):
		print('{} walks with {} legs'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')

# w.a.p to track the number of objects created for a class
# -----------------------------------------------------------------------------------
class Test:
	count = 0
	def __init__(self):
		Test.count += 1
	@classmethod
	def no_of_objects(cls):
		print('The number of objects created for Test class:',cls.count)
t1 = Test()
t2 = Test()
Test.no_of_objects()
t3 = Test()
t4 = Test()
Test.no_of_objects()

# 3).Static Methods:
# ---------------------------
# -->These methods are general utility methods. Inside these methods we wont use any instance or class variables. Here we wont provide self or cls args at the time of declaration.
# -->We can declare static method explicitly by using @staticmethod decorator. We can access static methods by using ClassName or object reference.

# Note:
	# In general we can use only instance and static methods. Inside static method we can access class level variables by using ClassName.
	# class methods are rarely used methods in python.

# Ex:
class MaheshMath:
	@staticmethod
	def add(x,y):
		print('The sum is:',x+y)
	
	@staticmethod
	def product(x,y):
		print('The product is:',x*y)

MaheshMath.add(10,20)
MaheshMath.product(10,2)

# Passing members of one class to another class:
# ----------------------------------------------------------------------
# We can access members of one class inside another class.

class Employee:
	def __init__(self,eno,ename,esal):
		self.eno = eno
		self.ename = ename
		self.esal = esal
	def display(self):
		print('Employee Number:',self.eno)
		print('Employee Name:',self.ename)
		print('Employee Salary:',self.esal)
class Test:
	def modify(emp):
		emp.esal += 8000
		emp.display()
e = Employee(101,'Sunny',12000)
Test.modify(e)

'''
Inner Classes:
----------------
* Sometimes we can declare a class inside another class, such type of classes are called inner classes.
* without exisiting one type of object if there is no chance of exisiting another type of object, then we should go for inner classes.

Ex-1:Without existing Car object there is no chance of existing Engine object. Hence Engine class should be part of Car class.
			class Car:
				class Engine:

Ex-2:Without existing University object there is no chance of existing Department object.
			class University:
				class Department:

Ex-3:Without existing Human there is no chance of existing Head. Without Head no chance of Brain.
			class Human:
				class Head:
					class Brain:

Note:
-----
* without existing outer class object there is no chance of exisiting inner class object. Hence Inner class object is always associated with outer class object.
'''

# Example:

class Outer:
    def __init__(self):
        print("Outer class object creation...")
    
    class Inner:
        def __init__(self):
            print('Inner class object creation...')
        
        def m1(self):
            print('Inner class m1() method')

o = Outer()
i = o.Inner()
i.m1()

i = Outer().Inner()
i.m1()

Outer().Inner().m1()

# Example - 1

class Human:
    def __init__(self):
        self.name = 'sunny'
        self.head = self.Head()
        self.brain = self.Head().Brain()
    
    def display(self):
        print('Hello, my name is', self.name)
        self.head.talk()
        self.brain.think()
    class Head:
        def talk(self):
            print('Talking...')
        class Brain:
            def think(self):
                print('Thinking...')

h = Human()
h.display()

# Nested methods:
# ----------------
# * Nested Method : A method inside the method.
# * Purpose : To define method specific repeatedly required functionality.

# Example : 

class Test:
    def m1(self):
        def calc(a,b):
            print('The sum is:',a+b)
            print('The product is:',a*b)
            print()
        calc(10,20)
        calc(100,200)

t = Test()
t.m1()

'''
Garbage Collections:
----------------------
-->In old langauges like C++ programmer is responsible for both creation and destruction of objects. Usually programmer is taking very much care while creating object, but neglecting destruction of useless objects. 
Because of this total memory can be filled with useless objects which creates memory problems and total performance will be down with 'out of memory' error

-->But in python we have some assiatant which is always running in the background to destroy useless objects. Because of this assistant the chance of failing python program with memory problems is very less. This is assistant is nothing but 
Garbage Collector(GC).

-->The main objective of GC is destroy useless objects.

-->If an object does not have any reference variable then that object is eligible for GC.

How to enable and disable GC in our program?
---------------------------------------------------------------------
Bydefault GC is enabled, but we can disable based on our requirement. In this context we can use the functions of gc module.

import gc
class Test:
	print(gc.isenabled())
	gc.disable()
	print(gc.isenabled())
	gc.enable()
	print(gc.isenabled())


Destructor:
-----------------
-->Destrucor is a special method and the name of should be __del__(). Just before destroying an object GC always calls destructor to perform clean up activities(Resource deallocation activities like close database connection etc).
-->Once destructoe execution completed then GC automatically destroy that object.

Note:
	The job of destructor is not destroy object and it is just to perform clean up activities.
'''

# Example : 1

import time 
class Test:
    def __init__(self):
        print('Object Initialization...')
    def __del__(self):
        print('Fulfilling last wish and performing clean up activities')

t = Test()
t = None
time.sleep(10)
print('End of application')

# Example : 2

import time
class Test:
	def __init__(self):
		print('Constructor Exection......')
	def __del__(self):
		print('Destructor Execution.......')
l = [Test(),Test(),Test()]
time.sleep(5)
print('End of application...')


# How to find number references of an object:
# --------------------------------------------------
# sys module contains getrefcount() function

# Example : 

import sys
class Test:
    pass
t1 = Test()
t2 = t1
t3 = t1
t4 = t1
print(sys.getrefcount(t1))

# Note : For every object, pytho internally maintains one default reference variable self.