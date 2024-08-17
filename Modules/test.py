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

'''

import kvsr
print(kvsr.x)
print(kvsr.add(10,20))
print(kvsr.product(10,20))

import kvsr as k
print(k.x)
print(k.add(10,20))
print(k.product(10,20))
