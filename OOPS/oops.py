# '''
# What is a class?
# -----------------
# * In python everything is an object. To create objects we required some model or plan or blue print, which is nothing but a class.
# * We can write a class to represent properties (attributes) and actions(behaviours) of an object.
# * Properties can be represented by variables and actions can be represented by methods.
# * Hence class contains both variables and methods.

# How to define a class?
# -----------------------
# We can define by using class keyword.
# Syn:
# 	class ClassName:
# 		"""documentation string"""
# 		variables:Instance, static and local variables
# 		methods:Instance,static and class methods

# * Documentation string represents description of the class. within the class doc string is always optional. We can get doc string in 2-ways.

# 1.print(ClassName.__doc__)
# 							2.help(ClassName)
# Ex:
# class Student:
# 	"""This is student class with required data"""
# print(Student.__doc__)
# help(Student)


# What is object?
# ----------------
# * Physical existence of a class is nothing but object.
# * We can create any number of objects for a class.
# Syn:
# 			refvariable = Classname()
# Ex:
# 			s = Student()

# What is a Reference Variable?
# ------------------------------
# * The variable which can be used to refer object is called reference variable.
# * By using reference variable, we can access properties and methods of object.

# '''

# # Q : W.A.P to create a student class and creates an objects to it. Call the method display() to display the student details.

# class Student:
#     def __init__(self, name, rollno, marks):  
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

#     def display(self):
#         print("Hello My Name Is:", self.name)
#         print("My Roll No Is:", self.rollno)
#         print("My Marks Are:", self.marks)


# s = Student('sunny', 101, 98)
# s.display()

# # Self Variable : 
# # -----------------

# # self is a default variable which is always pointing to current object(like this keyword in java)
# # By using self we can access instance variables and instance methods of objects.

# # NOTE : 1).self should be first parameter inside constructor.
# #           def __init__(self):
# # 2) .self should be first parameter inside instance method.        def display(self):

# '''
# Constructor concept:
# ---------------------
# * Constructor is a special method in python.
# * The name of the constructor should be __init__(self).
# * Constructor will be executed automatically at the time of object creation.
# * The main purpose of constructor is to declare and initialize instance variable.
# * Per object constructor will be executed only once.
# * Constructor can take atleast one argument(atleast self).
# * Constructor is optional and if we are not providing any constructor then python will provide default constructor.
# '''

# # EX : Program to demonstrate constructor will be executed only once per object
# # ------------------------------------------------------------------------------------

# class Test:
#     def __init__(self):
#         print("Constructor Execution...")
#     def m1(self):
#         print("Method Execution...")

# t1 = Test()
# t2 = Test()
# t3 = Test()
# t1.m1()

# # How to create list of objects in construcor
# # ----------------------------------------------------------

# class Movie:
#     def __init__(self, name, hero, heroine, rating):
#         self.name = name
#         self.hero = hero
#         self.heroine = heroine
#         self.rating = rating

#     def info(self):
#         print("Movie Name:", self.name)
#         print("Hero Name:", self.hero)
#         print("Heroine Name:", self.heroine)
#         print("Rating:", self.rating)
#         print()

# movies = [
#     Movie('OG', 'Pawan Kalyan', 'Priyanka', 4.5),
#     Movie('Kalki', 'Prabhas', 'Deepika', 4.2),
#     Movie('Devara', 'JR. NTR', 'Janhavi Kapoor', 5.0)
# ]

# for movie in movies:
#     movie.info()

# # without constructor:
# # -------------------------------

# class Movie:
# 	def info(self):
# 		print('Movie Name:',self.name)
# 		print('Hero Name:',self.hero)
# m = Movie()
# m.name = 'Devara'
# m.hero = 'Jr NTR'
# m.info()

# # with normal method
# # ------------------------------

# class Movie:
# 	def vd(self,name,hero):
# 		self.name = name
# 		self.hero = hero
# 	def info(self):
# 		print('Movie Name:',self.name)
# 		print('Hero Name:',self.hero)
# m = Movie()
# m.vd('Maharaja','Vijay')
# m.info()

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