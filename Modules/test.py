'''
MODULES:
=========
-->A group of functions,variables and classes saved into a file, which is nothing but module.
-->Every python file(.py) acts as a module.
-->Advantages of modules are:Reusability,Readability & Maintainability

Ex:kvsr.py
----------------------------
x = 333
def add(a,b):
	return a+b
def product(a,b):
	return a*b

-->kvsr module contains one variable and 2-functions.
-->If we want to use members of the module in our program then we should import that module.
						import modulename
-->We can access members by using module name
						modulename.variable
						modulename.function()

                        
Renaming a module at the time of import(module aliasing):
----------------------------------------------------------
Ex:
		import kvsr as k

-->Here kvsr is original module name and k is alias name.
-->We can access members by using alias name k.

from.......import : 
---------------------
* We can import a particular member of module by using from.....import
* The main advantage of this is we can access members directly without using module name.

Ex :
from kvsr import x,product
print(x)
print(add(10,20))
print(product(10,20)) #NameError.

* We can import all the members of a module as : from kvsr import *

Member aliasing : 
-------------------
from kvsr import x as y,add as sum
print(y)
print(sum(10,20))

* once we defined as alias name, we should use alias name only and we should not use original name.

from kvsr import x as y
print(x) # NameError

Various possibilities of import :
---------------------------------
1).import modulename
2).import module1,module2,module3
3).import module1 as m1
4).import module1 as m1,module2 as m2,module3 as m3
5).from module import member
6).from module import member1,member2,member3
7).from module import member1 as m1
8).from module import *


Reloading a module :
----------------------
Bydefault module will be loaded once eventhough we are importing multiple times.

Ex : module1.py
----------------
print("This is from module1")

test.py
--------
import module1
import module1
import module1
print('This is test module)

* In the above module1 will be loaded only once eventhough we are importing multiple times.
* The problem in this approach is after loading a module if it is updated outside then updated version of module1 is not avaliable to our program.
* We can reload a module by using reload() function of importlib module.


Ex:
import module1,time
from importlib import reload
print('Program entering into sleeping state')
time.sleep(30)
reload(module1)
print('This is the last line of the program')

-->The main advantage of explicit module reloading is we can ensure that updated version is always available to our program.

Finding members of module:
-------------------------------------------
Python provides inbuilt func dir() to list out all the members of current module or a specified module.

dir()==>To list out all members of current module.
dir(module name)==>To list out all the members of specified module.

test.py
----------
x = 333
def add(a,b):
	return a+b
print(dir())

To display members of a particular module(maheshmath)
--------------------------------------------------------------------------------------
import maheshmath
print(dir(maheshmath))

Note:
	For every module at the time of execution python interpreter will add some special properties automatically for internal use.

Ex:'__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__'

-->Based on our requirement we can access these properties also in our program.

test.py
----------
print(__builtins__)
print(__cached__)
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)
print(__spec__)

The special variable __name__:
---------------------------------------------
-->For every python program, a special variable __name__ will be added internally. This variable stores information regarding whether the program executed as an individual program or as a module.
-->If the program executed as an individual program then the value of this variable is __main__.
-->If the program executed as a module from some other program then the value of this variable is the name of the module where it is defined.
-->Hence by using this __name__ variable we can identify whether the program executed directly or as a module.

module1.py
------------------
def f1():
	if __name__ == '__main__':
		print('The code executed directly as a program')
		print('The value of __name__:',__name__)
	else:
		print('The code executed indirectly as a module from some other module')
		print('The value of __name__:',__name__)
f1()

test.py
----------
import module1
module1.f1()

D:\Mahesh_Classes>py module1.py
The code executed directly as a program
The value of __name__: __main__

D:\Mahesh_Classes>py test.py
The code executed indirectly as a module from some other module
The value of __name__: module1

'''

import kvsr
print(kvsr.x)
print(kvsr.add(10,20))
print(kvsr.product(10,20))

import kvsr as k
print(k.x)
print(k.add(10,20))
print(k.product(10,20))

x = 333
def add(a,b):
	return a+b
print(dir())


import kvsr
print(dir(kvsr))

import kvsr
kvsr.f1()