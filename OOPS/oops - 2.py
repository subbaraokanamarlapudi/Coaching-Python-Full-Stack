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

# * In the above example Parent class contains 10-methods and these methods automatically available to the child class and 
# these methods automatically available to the child class and we are not required to re-write those methods(code re-usability). Hence child class contains 15-methods.

# similarly variables also.

# Example 2:

class P:
    a = 10
    def __init__(self):
        self.b = 20

class C(P):
    c = 30
    def __init__(self):
        super().__init__()
        self.d = 40

c1 = C()
print(c1.a,c1.b,c1.c,c1.d)

# If we comment line-1 then variable 'b' is not available to the child class.


# EX : 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def eat_n_drink(self):
        print('Eat birayani and Drink cool drink')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.sal = esal
    
    def work(self):
        print("Coding is very easy just like chilled cooled water")
    
    def emp_info(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.sal)

e = Employee('Durga',48,872,100000)
e.eat_n_drink()
e.work()
e.emp_info()

# IS-A vs HAS-A Relationship:
# -----------------------------

# * If we want to extend existing functionality with some more extra functionality then we should go for IS-A relationship
# * If we want to extend and just we have to use existing functionality then we should go for HAS-A relationship.
    
# EXAMPLE : 
#     Employee class extends person class functionality.
#     But Employee class just uses car functionality but not extending.

# Ex : 

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    
    def get_info(self):
        print('\tCar Name:{}\n\tModel:{}\n\tColor:{}'.format(self.name,self.model,self.color))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat_n_drink(self):
        print('Eat birayani and Drink cool drink')

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
        self.car = car
    
    def work(self):
        print("Coding is very easy just like chilled cooled water")
    
    def emp_info(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)
        print('Employee Car Info:')
        self.car.get_info()

c = Car('Innova','2.5V','Grey')
e1 = Employee('Durga',48,872,100000,c)
e1.eat_n_drink()
e1.work()
e1.emp_info()

'''
Compositon:
------------
* Without existing container object if there is no chance of existing contained object then the container and contained objects
  are strongly associated and that strong association is nothing but composition.

Ex:
    University contains several Departments and without existing University object there is no chance of existing Department object. 
    Hence University and Department objects are strongly associated and this strong association is nothing but Composition.

    
Aggregation:
-------------
* Without existing container object if there is a chance of existing contained object then the container and contained objects are weakly associated and that weak association is nothing but Aggregation.
Ex:
	Department contains several Professors. Without existing Department still there may be a chance of existion Professor. 
    Hence Department and Professor objects are weakly associated, whcih is nothing but Aggregation.

Ex:
class Student:
	college_name = 'NIT'
	def __init__(self,name):
		self.name = name
print(Student.college_name)
s = Student('Sunny')
print(s.name)	

-->In the above example without existing Student object there is no chance of existing his name. Hence Student object and his name are strongly associated which is nothing but Composition.

-->But without existing Student object there may be a chance of existing college_name. Hence Student object and college_name are weakly assocaited which is nothing but Aggregation.

Conclusion:
	The relation between object and its instance variables is always Composition where as the relation between object and static variable is Aggregation.

Note:
	Whenever we are creating child class object then child class constructor will be executed. If the child class does not contain constructor then parent class constructor will be executed, but parent object won't be created.

'''

# EXAMPLE : 1

class Student:
    college_name = 'NIT'
    def __init__(self,name):
        self.name = name

print(Student.college_name)
s = Student('sunny')
print(s.name)

# Example : 2

class P:
    def __init__(self):
        print(id(self))

class C(P):
    pass

c = C()
print(id(c))

# EXAMPLE : 3

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks
    
    def __str__(self):
        return 'Student Name:{}\nStudent Age:{}\nStudent Rollno:{}\nStudent Marks:{}'.format(self.name,self.age,self.rollno,self.marks)
    
s = Student('sunny',25,101,98)
print(s)

'''
TYPES OF INHERITANCE :
-----------------------

1. Single Inheritance:
------------------------
* The concept of inheriting the properties from one class to another class is known as single inheritance.

2. Multi-level Inheritance:
--------------------------
* The concept of inheriting the properties from multiple classes to single class with the concept of one after another is known as multi-level inheritance.

3. Hierarchical Inheritance:
------------------------------
* The concept of inheriting properties from one class into multiple classes which are present at the same level is know as hierarchical inheritance.

4. Multiple Inheritance:
--------------------------
* The concept of inheriting the properties from multiple classes into single class at a time, is know as multiple inheritance.
* If the same method is inhertied from the both parent classes,then python will always consider the order of parent classes in the declartion of the child class.

                class C(P1,P1):==>P1 method will be considered.
				class C(P2,P1):==>P2 method will be considered.

5. Hybrid Inheritance:
-----------------------
* The combiniation of single, multiple-level, multiple and hierarchical inheritance is known as hybrid inheritance.

6. Cyclic Inheritance:
-----------------------
* The concept of inheriting properties from class to another class in cyclic way, is called as cyclic inheritance.
* Python wont support cyclic inheritance of course it is really not required.

'''

# 1. Single Inheritance :
# ---------------------------

class P:
    def m1(self):
        print('Parent Method')

class C(P):
    def m2(self):
        print('Child Method')

c = C()
c.m1()
c.m2()


# 2. Multi-level Inheritance:
# ------------------------------

class P:
    def m1(self):
        print("Parent Method")

class C(P):
    def m2(self):
        print("Child Method")

class CC(C):
    def m3(self):
        print("Sub Child Method")

c = CC()
c.m1()
c.m2()
c.m3()

# 3. Hierarchical Inheritance:

class P:
    def m1(self):
        print("Parent Method")

class C1(P):
    def m2(self):
        print("Child-1 Method")

class C2(P):
    def m3(self):
        print("Child-2 Method")

c1 = C1()
c1.m1()
c1.m2()
c2 = C2()
c2.m1()
c2.m3()

# 4. Multiple Inheritance:

class P1:
    def m1(self):
        print("Parent-1 Method")

class P2:
    def m2(self):
        print("Parent-2 Method")

class C(P2,P1):
    def m3(self):
        print("Child Method")

c = C()
c.m1()
c.m2()
c.m3()

class P1:
	def m(self):
		print('Parent-1 Method')
class P2:
	def m(self):
		print('Parent-2 Method')
class C(P2,P1):
	def m1(self):
		print('Child Method')
c = C()
c.m()
c.m1()

# 6. Cyclic Inheritance:
# -----------------------

# Ex-1
# class A(A):pass
# # NameError: name 'A' is not defined

# # Ex-2:
# class A(B):
# 	pass
# class B(A):
# 	pass
# # NameError: name 'B' is not defined

# super() method:
# ==============
# 	super() is a built-in method which is useful to call the super class constructors, variables and methods from the child class.

# EX : 1
# ---------

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Rollno:',self.rollno)
        print('Marks:',self.marks)

s = Student('Durga',48,101,100)
s.display()

# EX - 2 :

class P:
    a = 10
    def __init__(self):
        self.b = 20
    
    def m1(self):
        print("Parent Instance Method")
    
    @classmethod
    def m2(cls):
        print("Parent Class Method")

    @staticmethod
    def m3():
        print("Parent Static Method")

class C(P):
    a = 333

    def __init__(self):
        self.b = 999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()


c = C()

# From the child class we are not allowed to access parent. Class instance variable by using super(), Compulsory we should use self only.
# But we can access parent class static variable by using super().

class P:
    a = 10
    def __init__(self):
        self.b = 20


class C(P):
    def m1(self):
        print(super().a)
        # print(super().b)  #Invalid
        super().__init__()
        print(self.b)

c = C()
c.m1()


'''
Method Resolution Order(MRO):
-------------------------------
* In hybrid inheritance the method resolution order is decided based on MRO algorithm.
* The algorithm is also known as C3 algorithm
* SAMUELE PEDRONI  proposed this algorithm.
* It follows DLR(Depth First Left to Right).
* That is child will get more priority than parent.
* Left parent will get more priority than right parent
*        MRO(X) = X + Merge(MRO(P1),MRO(P2),..........,ParentList)


 Head element vs Tail Terminology:
 ----------------------------------
* Assume C1,C2,C3,..............., are classes
* In the list: C1C2C3C4C5....................
* C1 is considered as Head element and remaining is considered as tail.

How to find Merge:
-------------------
* Take the head of the first list.
* If the head is not in the tail part of any other list, then add this head to result and remove it from the lists in the merge.
* If the head is present in the tail part of any other list, then consider the head element of the next list and continue the same process.

Note:
------
* We can find MRO of any class by using mro() function.

syntax:  print(ClassName.mro())
'''

# EX - 1

class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(D.mro())

# EX - 2    

# Finding mro(P) by using C3 algorithm:
# ---------------------------------------------------------
# MRO(X) = X + Merge(MRO(P1),MRO(P2),....,ParentList)

# mro(P)	= P + Merge(mro(X),mro(Y),mro(C),XYC)
# 			= P + Merge(XABO,YBCO,CO,XYC)
# 			= P + X + Merge(ABO,YBCO,CO,YC)
# 			= P + X + A + Merge(BO,YBCO,CO,YC)
# 			= P + X + A + Y + Merge(BO,BCO,CO,C)
# 			= P + X + A + Y + B + Merge(O,CO,CO,C)
# 			= P + X + A + Y + B + C + O

# ----------
class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(P.mro())

# Ex-3:
# --------
# mro(D)=D,object
# mro(E)=E,object
# mro(B)=B,DE,object
# mro(C)=C,D,F,object
# mro(A)=A + Merge(mro(B),mro(C),BC)
# 		  =A + Merge(BDEO,CDFO,BC)
# 		  =A + B + Merge(DEO,CDFO,C)
# 		  =A + B + C + Merge(DEO,DFO)
# 		  =A + B + C + D + Merge(EO,FO)
# 		  =A + B + C + D + E + Merge(O,FO)
# 		  =A + B + C + D + E + F + O

class D:	pass
class E:	pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass
print(A.mro())