'''
Agenda : 
    * Inheritance
    * Has-A Relationship
    * IS-A Relationship
    * IS-A VS HAS-A Relationship
    * Composition VS Aggregation
    
    * Types of inheritances:
        * Single Inheritance
        * Multi-level Inheritance
        * Multiple Inheritance
        * Hierarchical Inheritance
        * Hybrid Inheritance
        * Cyclic Inheritance    
    
    * MRO(Method Resolution Order)
    * Super() function
'''

# Using members of one class inside another class:
# ---------------------------------------------------

# 1. By composition (Has-A Relationship)
# 2. By inheritance (IS-A Relationship)

# 1.Has-A Relationship : 
# -----------------------

# * By using ClassName of by creating object we can access members of one class inside another class is nothing but composition(HAS-A Relationship).
# The main advantage of Has-A relationship is code re-usablity.

# Example 1:
class X:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('m1 method of X-class')

class Y:
    c = 30
    def __init__(self):
        self.d = 40
    def m2(self):
        print('m2 method of Y-class')
        
    def m3(self):
        x1 = X()
        print(x1.a)
        print(x1.b)
        x1.m1()
        print(Y.c)
        print(self.d)
        self.m2()
        print('m3 method of Y-class')

y1 = Y()
y1.m3()

# Example 2:

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    
    def get_info(self):
        print('Car Name:{},Model:{},Color:{}'.format(self.name, self.model, self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.name = ename
        self.eno = eno
        self.car = car

    def emp_info(self):
        print('Employee Name:',self.name)
        print('Employee Number:',self.eno)
        print('Employee Car Info:')
        self.car.get_info()

c1 = Car('Innova','2.5V','Grey')
e1 = Employee('Durga',100,c1)
e1.emp_info()

# In the above example Emplyee Has-A Car reference, hence Employee class can access all members of Car class.


# 2. By Inheritance(IS-A Relationship):
# ---------------------------------------
# * Whatever variables, methods and constructors available in the parent class by default available to the child classes and we are not required to re-write.
# * Hence the main advantage of inheritance is code re-usability and we can extend exisiting functionality with some more extra functionality.

# Syntax :      class ChildClass(ParentClass)

# Example 1:

class P:
    a = 10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Parent instance method')
    
    @classmethod
    def m2(cls):
        print('Parent class method')
    
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    pass

c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()