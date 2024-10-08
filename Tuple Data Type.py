'''
---> Tuple:

* It is one of the datatype.
* It is represented by "()".
* It allows different types of elements.
* It allows duplicates.
* It allows indexing and slicing.
* It is immutable. -----> Data cannot modify.
* No methods. We can use in-bulit functions.


Tuple operations:
* concatentaion.
* Iteration.
* Membership operation.
* Identity operation.
* Repetation.

'''

# Tuple Creation : 

# 1. 
c = ()
print(type(c))

# 2. By using tuple() function

l = [10,20,30]
t = tuple(l)
t = tuple(range(5))
print(t)

# --------------------------Accessing element of tuple.------------------------------

# 1. By using index : 
t = (10,20,30)
t[0]
t[-1]
t[100]

# 2. By using slice operator : 
t = (10,20,30,40)
print(t[0:2])

# --------------------------Tuple vs Immutability------------------

# ----> Once we create tuple,we cant change its content.
# -----> Hence tuple objects are immutable.

t = (10,20,30)
print(t[100])    # TypeError.

# ------------------- Mathematical operations for tuple -----------------------

# 1. Concatenation operator(+):

t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1+t2
print(t3)

# 2. Repetition operator(*):

t1 = (10,20,30)
t2 = t1*3
print(t2)

# ------------------- Functions in tuple ---------------------------------

'''
1.len():
	To return number of elements present in tuple.

2.count():
	To return number of occurences of given element in the tuple.

3.index():
	Returns index of first occurence of the given element.
	If the specified element is nor available then we will get ValueError.

4.sorted():
	To sort elements based on default natural sorting order.
'''

# 4. sorted()
t = (40,10,30,20)
t1 = tuple(sorted(t))
print(t1)

# 5. Min and Max : 

t = (40,10,20,50,30)
print(min(t))
print(max(t))

s = 'radhika'
print(min(s))
print(max(s))

# --------------Tuple packing and unpacking ------------------
# ---> We can create a tuple by using packing a group of variables.

#  Packing example in tuple : 

a = 10
b = 20
c = 30
t = a,b,c
print(t)

# ------> Here a,b,c,d are packed into a tuple t. This is nothing but tuple packing.

# Unpacking example in tuple :

# -->Tuple unpacking is the reverse process of tuple packing.
# -->We can unpack a tuple and assign its values to different variables.

t = (10,20,30,40)
a,b,c,d = t
print('A:',a)
print('B:',b)
print('C:',c)
print('D:',d)

# Note: At the time of tuple unpacking the number of variables and number of values should be same. Otherwise we will get an error.

# ---------------Tuple comprehensions----------------------
'''
Tuple Comprehensions:
-----------------------------------
Tuple comprehension is not supported by python.
Ex:
				t = (x*x for x in range(5))
-->Here we are not getting tuple object and we are getting generator object.

'''

x = (i*i for i in range(5))
print(type(x))#<class 'generator'>
for i in x:
	print(i)

# w.a.p to take tuple of numbers from the keyboard and print sum and average

t = eval(input('Enter tuple of numbers:'))
l = len(t)
sum = 0
for x in t:
	sum += x
print('The sum is:',sum)
print('The average is:',sum/l)

'''
Q.Difference between List and Tuple?
-------------------------------------------------------
			List											Tuple
			------											--------
1.List a group of comma separated values	1.Tuple is a group of comma separated
within the square brackets and square		values within the parenthesis, It is an
brackets are mandatory.							optional.
Ex:	l = [10,20,30]										Ex: t=(10,20,30) or t = 10,20,30

2.List objects are mutable. i.e once we		2.Tuple object is immutable. i.e once
create list object we can perform any			we create tuple object we can't change
changes in that object.								its content.

3.If the content is not fixed and keep on	3.If the content is fixed and never 
changing then we should go for list.			changes then we should go for tuple.

4.Comprehension are available.					4.There is no comprehensions.

'''

t = (5,10,15)
x,_,y = t
print(x,y)#5 15

# Q.
a = 1_2
b = a*2
b #24

# Q.
x,y = 4,3
z = (x--x) + (y--y)
print(z)#14

# Q.
a = 2
b = 3
a**b*a**b #64

# Q.
a = 4
b = 5
c = 8
print(a|b|c)#13

# Q.
print(min(max(False,-7.5,-7),2,1,9))

# Q.
text = 'hello world'
expr = ('d', 'rld')
result = text.endswith(expr)
print(result)