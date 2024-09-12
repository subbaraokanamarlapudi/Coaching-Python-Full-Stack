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