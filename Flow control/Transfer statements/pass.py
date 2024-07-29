'''
pass:
------------
-->In our programming syntactically if a block is required which wont do anything then we can define that empty block with pass keyword.

pass:
	-->It is an empty statement.
	-->It is null statement.
	-->It won't do anything.

'''
# Ex:
if True:pass

def f1():pass

# Ex:
for i in range(100):
	if i%9 == 0:
		print(i)
	else:
		pass


'''
del statement:
---------------------
-->del is a keyword in python.
-->After using a variable it is highly recommended to delete that variable if it is no longer required, so that the corresponding object is eligible for garbage collection. We can delete variable by using del statement.

'''

# Ex:
s = 'sunny'
del s[0] #TypeError: 'str' object doesn't support item deletion

# Ex:
x = 10
print(x)
del x
print(x) #NameError: name 'x' is not defined

# Note:We can delete variables which are pointing to immutable objects. 
# But we cant delete the elements present inside the immutable objects.