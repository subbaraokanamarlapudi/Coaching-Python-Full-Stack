'''
*********************************************************** SET ****************************************************
* It is a unordered and mutable collection of unique elements.
* It is denoted by {}
* Insertion order is preserved.
* Hetrogenious objects are allowed.
* Duplicates are not allowed.
* Doesnot perform Indexing and slicing.

'''

# Creation of set object:
# ---------------------------------
s = {10,20,30,40}
type(s)

l = [10,20,30]
s = set(l)
print(s)

s = set(range(5))
print(s)

s = {}
type(s) #<class 'dict'>

s = set()
type(s)

# -------------------------------------------------------------Functions of set-------------------------------------------
# -------------------------
# 1.add(x):
	# Add item x to the set.

s = {10,20,30}
s.add(40)
print(s)

# 2.update(x,y,z):
# 	-->To add multiple items to the set.
# 	-->Args are not individual elements and these are iterable elements like list, range etc.....
# 	-->All elements present in the given iterable objects will be added to the set.

s = {10,20,30}
l = [40,50,60]
s.update(l,range(5))
print(s)

# Q.What is difference between add() and update() functions in set?
# -------------------------------------------------------------------------------------------------
# -->We can use add() to add individual items to the set, where as we can use update() function to add multiple items to the set.
# -->add() function can take only one argument where as update() function can take any number of args but all args should be iterable objects.

# Q.Which are valid?
s.add(10)	#Valid
s.add(10,20) #Invalid
s.update(30) #Invalid
s.update(range(5)) #Valid

# 3.copy():
# 	Returns copy of the set
# 	It is cloned object.

s = {10,20,30}
s1 = s.copy()
print(s1)


# 4.pop():
# 	It removes and returns some random element from the set.

s = {20,10,40,30}
print(s.pop())
print(s)

# 5.remove(x):
# 	-->It removes specified element from the set.
# 	-->If the specified element not present in the set then we will get KeyError.

s = {10,20,30}
s.remove(10)
print(s)
s.remove(40)#KeyError: 40

# 6.discard(x):
# 	-->It removes specified element from the set.
# 	-->If the specified element not present in the set then we wont get any error.

s = {10,20,30}
s.discard(30)
s.discard(50)#No Error

# 7.clear():
# 	To remove all elements from the set.

s = {10,20,30}
s.clear()
print(s)

# Mathematical operations on the set:
# -------------------------------------------------------
# 1.union():
# 	x.union(y)		or		x | y:
# 		Returns all elements present in both sets

x = {10,20,30,40}
y = {30,40,50,60}
print(x.union(y))
print(x | y)

# 2.intersection():
# 	x.intersection(y)	or		x & y:
# 		Returns common elements present in both x and y.

x = {10,20,30,40}
y = {30,40,50,60}
print(x.intersection(y))
print(x & y)

# 3.difference():
# 	x.difference(y)	or		x - y:
# 		Returns the elements present in x but not in y.

x = {10,20,30,40}
y = {30,40,50,60}
print(x.difference(y))
print(x - y)
print(y.difference(x))
print(y - x)

# 4.symmetric_difference():
# 	x.symmetric_difference(y)		or		x ^ y
# 		Returns element present in either x or y but not in both.

x = {10,20,30,40}
y = {30,40,50,60}
print(x.symmetric_difference(y))#{10, 50, 20, 60}
print(x ^ y)#{10, 50, 20, 60}

# Set comprehensions:
# -------------------------------
# Set comprehensions is possible.

x = {i*i for i in range(5)}
print(type(x))
print(x)

# Q.w.a.p to eliminate duplicates present in the list
# ---------------------------------------------------------------------------
# 1st way:
# ------------
l = eval(input('Enter list of values'))
s = set(l)
print(s)

# 2nd way:
# -------------
l = eval(input('Enter list of values'))
l1 = [ ]
for x in l:
	if x not in l1:
		l1.append(x)
print(l1)

# Q.w.a.p to print different vowels in the given word?
# ----------------------------------------------------------------------------
w = input('Enter word to search for vowels:')
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print('The different vowels present in',w,'are:',d)

# Q.
list = [1,0,2,0,3,0]
for i in list:
	if i == 0:
		list.remove(i)
		list.append(i)
print(list)#[1, 2, 3, 0, 0, 0]

# Q.
a = [1,2,3,4,5]
for i in a:
	a.remove(i)
print(a)#[2,4]

# Q.
a,b = '06'
b,c = '26'
print(a+b+c)#026