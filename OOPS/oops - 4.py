'''
AGENDA:
-------

1. ABSTRACT METHOD
2. ABSTRACT CLASS
3. INTERFACE
4. PUBLIC , PRIVATE AND PROTECTED MEMBERS
5. __str()__ method
6. DIFFERENCE BETWEEN str() AND repr() FUNCTIONS?

'''

# 1. ABSTRACT METHOD:
# -------------------------

# * Sometimes we dont know about implementation, still we can declare a method. Such type of methods are called as abstract methods. i.e abstract method has only declaration but not implementation.
# * In Python we can declare abstract method by using @abstractmethod decorator as 
#              @abstractmethod
#              def m1(self):pass
# @abstractmethod decorator present in abc module. We should import abc module. 

# abc ===> Abstract Base Class 

# Example - 1:
from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass

# Example - 2:
from abc import *
class Fruit:
    @abstractmethod
    def taste(self):
        pass

# Child classes are responsible to provide implementation for parent class abstract methods.

# Abstract class:
# ----------------------
# -->Some times implementation of a class not complete, such type of partially implemented classes are called as abstract classes.
# -->Every abstract class in python should be derived from ABC class which is present in abc module.

# Case-1:
# -----------
from abc import *
class Test:
	pass
t = Test()

# -->In the above code we can create object for Test class bcoz it is concrete class and it does not contains any abstract method.

# Case-2:
# ----------
from abc import *
class Test(ABC):
	pass
t = Test()

# -->We can create object, even it is derived from ABC class, bcoz it does not contain any abstract method.

# Case-3:
# -----------
from abc import *
class Test(ABC):
	@abstractmethod
	def m1(self):
		pass
t = Test()

# TypeError: Can't instantiate abstract class Test with abstract method m1

# Case-4:
# -----------
from abc import *
class Test:
	@abstractmethod
	def m1(self):
		pass
t = Test()

# -->We can create object even class contains abstract method bcoz we are not extending ABC class.

# Case-5:
# -----------
from abc import *
class Test:
	@abstractmethod
	def m1(self):
		print('Hi')
t = Test()
t.m1()

# Conclusion:
# ------------------
# If a class contains atleast one abstract method and if we are extending ABC class then instantiation is not possible.

# 		'abstract class with abstract method instantiation is not possible'

# -->Parent class abstract methods should be implemented in the child classes. Otherwise we cannot instantiate child class. If we are not creating child class object then we wont get any error.

# Ex:
from abc import *
class Vehicle(ABC):
	@abstractmethod
	def no_of_wheels(self):
		pass
class Bus(Vehicle):
	pass

# -->It is valid bcoz we are not creating child class object.

# b = Bus()
# TypeError: Can't instantiate abstract class Bus with abstract method no_of_wheels

# Note:
# 	If we are extending abstract class and does not override its abstract method then child class is also abstract and instantiation is not possible.

# Example : 

from abc import *
class Vehicle(ABC):
	@abstractmethod
	def no_of_wheels(self):
		pass

class Bus(Vehicle):
	def no_of_wheels(self):
		return 7

class Auto(Vehicle):
	def no_of_wheels(self):
		return 3

b = Bus()
print(b.no_of_wheels())
a = Auto()
print(a.no_of_wheels())
	
# Note:	Abstract class can contain both abstract and non-abstract methods also

# Interface vs Abstract class vs Concrete class
# -------------------------------------------------------------------
# 1.If we dont know anything about implementation just we have requirement specification then we should go for interface.

# 2.If we are talking about implementation bit not completely then we should go for abstract class.(Partially implemented class)

# 3.If we are talking about implementation completely and ready to provide service then we should go for concrete class.

# 				Interface			:No Implementation
# 				Abstract class		:Partial Implementation
# 				Concrete class		:Full Implementation
