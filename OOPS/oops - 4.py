# '''
# AGENDA:
# -------

# 1. ABSTRACT METHOD
# 2. ABSTRACT CLASS
# 3. INTERFACE
# 4. PUBLIC , PRIVATE AND PROTECTED MEMBERS
# 5. __str()__ method
# 6. DIFFERENCE BETWEEN str() AND repr() FUNCTIONS?

# '''

# # 1. ABSTRACT METHOD:
# # -------------------------

# # * Sometimes we dont know about implementation, still we can declare a method. Such type of methods are called as abstract methods. i.e abstract method has only declaration but not implementation.
# # * In Python we can declare abstract method by using @abstractmethod decorator as 
# #              @abstractmethod
# #              def m1(self):pass
# # @abstractmethod decorator present in abc module. We should import abc module. 

# # abc ===> Abstract Base Class 

# # Example - 1:
# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass

# # Example - 2:
# from abc import *
# class Fruit:
#     @abstractmethod
#     def taste(self):
#         pass

# # Child classes are responsible to provide implementation for parent class abstract methods.

# # Abstract class:
# # ----------------------
# # -->Some times implementation of a class not complete, such type of partially implemented classes are called as abstract classes.
# # -->Every abstract class in python should be derived from ABC class which is present in abc module.

# # Case-1:
# # -----------
# from abc import *
# class Test:
# 	pass
# t = Test()

# # -->In the above code we can create object for Test class bcoz it is concrete class and it does not contains any abstract method.

# # Case-2:
# # ----------
# from abc import *
# class Test(ABC):
# 	pass
# t = Test()

# # -->We can create object, even it is derived from ABC class, bcoz it does not contain any abstract method.

# # Case-3:
# # -----------
# from abc import *
# class Test(ABC):
# 	@abstractmethod
# 	def m1(self):
# 		pass
# t = Test()

# # TypeError: Can't instantiate abstract class Test with abstract method m1

# # Case-4:
# # -----------
# from abc import *
# class Test:
# 	@abstractmethod
# 	def m1(self):
# 		pass
# t = Test()

# # -->We can create object even class contains abstract method bcoz we are not extending ABC class.

# # Case-5:
# # -----------
# from abc import *
# class Test:
# 	@abstractmethod
# 	def m1(self):
# 		print('Hi')
# t = Test()
# t.m1()

# # Conclusion:
# # ------------------
# # If a class contains atleast one abstract method and if we are extending ABC class then instantiation is not possible.

# # 		'abstract class with abstract method instantiation is not possible'

# # -->Parent class abstract methods should be implemented in the child classes. Otherwise we cannot instantiate child class. If we are not creating child class object then we wont get any error.

# # Ex:
# from abc import *
# class Vehicle(ABC):
# 	@abstractmethod
# 	def no_of_wheels(self):
# 		pass
# class Bus(Vehicle):
# 	pass

# # -->It is valid bcoz we are not creating child class object.

# # b = Bus()
# # TypeError: Can't instantiate abstract class Bus with abstract method no_of_wheels

# # Note:
# # 	If we are extending abstract class and does not override its abstract method then child class is also abstract and instantiation is not possible.

# # Example : 

# from abc import *
# class Vehicle(ABC):
# 	@abstractmethod
# 	def no_of_wheels(self):
# 		pass

# class Bus(Vehicle):
# 	def no_of_wheels(self):
# 		return 7

# class Auto(Vehicle):
# 	def no_of_wheels(self):
# 		return 3

# b = Bus()
# print(b.no_of_wheels())
# a = Auto()
# print(a.no_of_wheels())
	
# # Note:	Abstract class can contain both abstract and non-abstract methods also

# # Interface vs Abstract class vs Concrete class
# # -------------------------------------------------------------------
# # 1.If we dont know anything about implementation just we have requirement specification then we should go for interface.

# # 2.If we are talking about implementation bit not completely then we should go for abstract class.(Partially implemented class)

# # 3.If we are talking about implementation completely and ready to provide service then we should go for concrete class.

# # 				Interface			:No Implementation
# # 				Abstract class		:Partial Implementation
# # 				Concrete class		:Full Implementation


# # EX : 

# from abc import *
# class CollegeAutomation(ABC):
# 	@abstractmethod
# 	def m1():pass
# 	@abstractmethod
# 	def m2():pass
# 	@abstractmethod
# 	def m3():pass

# class AbsClass(CollegeAutomation):
# 	def m1(self):
# 		print('M1 method implemetation')
	
# 	def m2(self):
# 		print('M2 method implemetation')

# class ConcreteClass(AbsClass):
# 	def m3(self):
# 		print('M3 method implemetation')

# c = ConcreteClass()
# c.m1()
# c.m2()
# c.m3()

# # In general if an abstract class contains only abstract methods such type of abstract class is considered as interface.

# # EX:

# from abc import *
# class DBinterface(ABC):
# 	@abstractmethod
# 	def connect(self):pass
# 	@abstractmethod
# 	def disconnect(self):pass

# class Oracle(DBinterface):
# 	def connect(self):
# 		print('Connecting to Oracle DB')
# 	def disconnect(self):
# 		print('Disconnecting from Oracle DB')

# class MongoDB(DBinterface):
# 	def connect(self):
# 		print('Connecting to MongoDB')
# 	def disconnect(self):
# 		print('Disconnecting from MongoDB')

# dname = eval(input("Enter Database: "))
# className = globals()[dname]
# print(globals()[dname])
# d = className()
# d.connect()
# d.disconnect()

# # Note : The inbuilt function globals()[str] converts the string 'str' into a className and returns the className.

# from abc import *
# class Printer(ABC):
# 	@abstractmethod
# 	def print_it(self,text):pass
# 	@abstractmethod
# 	def disconnect(self):pass

# class Epson(Printer):
# 	def print_it(self,text):
# 		print('Printing from Epson Printer')
# 	def disconnect(self):
# 		print('Disconnecting from Epson Printer')


# class HP(Printer):
# 	def print_it(self,text):
# 		print('Printing from HP Printer')
# 	def disconnect(self):
# 		print('Disconnecting from HP Printer')

# with open('config.txt','r') as f:
# 	pname=f.readline()

# className = globals()[pname]
# c = className
# c.print_it('This data has to print....')
# c.disconnect()


# # public, private and protected attributes
# # ----------------------------------------------------------
# # -->Bydefault every attribute is public. We can access from anywhere either within the class or from outside of the class.
# # Syn:	variablename = value
# # Ex:	name = 'sunny'

# # test.py
# # ----------
# class Test:
# 	x = 10
# 	def __init__(self):
# 		self.y = 20

# # test1.py
# # ------------
# from test import Test
# class Test1:
# 	t = Test()
# 	print(t.x)
# 	print(t.y)

# # -->Protected variables can be accessed with in the class anywhere but from outside of the class only in child class. We can specify an attribute as protected by prefixing with _ symbol.

# # Syn: _variablename = value
# # Ex:	_name = 'sunny'

# # test.py
# # ----------
# class Test:
# 	_x = 10
# 	def __init__(self):
# 		self._y = 20
# t = Test()
# print(t._x)
# print(t._y)

# # -->But it is just convention and in reality does not exist protected attributes.

# # -->Private attributes can be accessed only within the class. i.e from outside of the class we cannot access. We can declare a variable as private explicitly by prefixing with 2 underscore symbols.

# # Syn:	__variablename = value
# # Ex:	__name = 'sunny'

# class Test:
# 	x = 10
# 	_y = 20
# 	__z = 30
# 	def m1(self):
# 		print(Test.x)
# 		print(Test._y)
# 		print(Test.__z)
# t = Test()
# t.m1()
# print(Test.x)
# print(Test._y)
# print(Test.__z)

# # How to access private variables from outside of the class?
# # ---------------------------------------------------------------------------------------
# # We cannot access private variables directly from outside of the class.
# # But we can access indirectly as:
# # 				objreference._ClassName__variablename
# # Ex:
# class Test:
# 	__x = 10
# 	def __init__(self):
# 		self.__y = 20
# t = Test()
# #print(t.__dict__)
# print(t._Test__y)
# print(Test._Test__x)

# # __str__() method:
# # -------------------------
# # -->Whenever we are printing any object reference internally __str__() method will be called which returns string in the following format.
# # 				<__main__.Student object at 0x000001B36242BB20>
# # -->To return meaningful string representation we have to override __str__() method
# # Ex:
# class Student:
# 	def __init__(self,name,rollno):
# 		self.name = name
# 		self.rollno = rollno
# 	def __str__(self):
# 		return 'This is Student with Name:{} and RollNo:{}'.format(self.name,self.rollno)
# s1 = Student('Radhika',101)
# s2 = Student('Lilly',102)
# print(s1)
# print(s2)

# Q : Difference between str() and repr()  (or) Difference between __str__() and __repr__() ?
# ----------------------------------------------------------------------------------------------------------

# * str() internally calls __str__() method, hence functionality of both is same.
# * similarly repr() internally calls __repr__() function.
# * str() returns a string containing a nicely printable reprensentation object. 
# * The main purpose of str() is for readability. It may not possible to convert result string to original object. 
# * But by using repr() it is possible.
# * We can convert result string to original object by using eval() function, which may not possible in str() function.

# Ex:

import datetime
today = datetime.date.today()
# print(today)
print(type(today))
s = repr(today) # converting datetime object to str
print(s)
print(type(s))
d = eval(s) # converting str to datetime object
print(d)
print(type(d))

# Note : It is recommended to use repr() instead of str().