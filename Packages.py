'''
Packages:
=========

* It is encapsulation mechanism to group related modules into a single unit.
* Packages is nothing but folder or directory which represents collection of python modules.
* A package can contains sub packages also.

Example : 1
===========

D:\test.py
    |-- com
        |-- module.py
            |-- f1()
        |-- module1
            |-- f2()

module.py
-----------------
def f1():
	print('Hello this is from module-1 present in com')

module1.py
-----------------
def f2():
	print('Hello this is from module-2 present in com.nareshit')

test.py
----------
from com.module import f1
from com.module1 import f2
f1()
f2()

'''