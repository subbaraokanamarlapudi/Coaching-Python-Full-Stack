'''
-----------------------------------NUMPY-----------------------------

Python for Data Science, ML, DL and AI
-----------------------------------------------------------
Python for devopps-->Regular core python knowledge
	concise code
	Rich libraries-->70% to 90% our libraries 10% we have to write the code

Data Science:

Devopps Vs DataScience:
Programming background--->data science

What is this line in python:
		import numpy as np

Numpy-->Entry point from python for datascience
Numpy-->Numerical Python Library

How to install Numpy?
----------------------------------
2-ways
----------
1st way:Anakonda---->
2nd way:pip install numpy

how to check version:
	goto python shell:
		import numpy as np
		print(np.__version__)

What is the need of Numpy?
-----------------------------------------
Python performs basic mathematical operations.
a = 10
b = 20
+b
a-b
a*b
a/b

math.sqrt(10)

But in Data Science , ML, DL and AI required complex mathematical operations.

1.Numpy defines several functions to perform complex mathematical operations.
2.To fullfill performance gaps
	most of the numpy is implemented in C-Language
	superfast
3.nd array(To store large data in nd array for matplotlib graph style)
	-->n dimensional array or numpy array
	numpy acts as backbone for remaining libraries also.

Ex:
	matrix with all zero 10X10 shape
	nested list
	[[0,0,0....],[0,0,0....],..[],[]......]


'''

import numpy as np
a = np.zeros((10,10))
print(a)


# If we want only int type:
a = np.zeros((10,10),dtype=int)
print(a)

# List of 100 numbers
a = np.arange(1,101)
print(a)

# Please convert into 2-D
a = a.reshape(10,10)

# Identity matrix
a = np.identity(3)
print(a)

a = np.identity(5)
print(a)

# 3.Data Analysis
# 	2-crores samples are analyzed......
# 	100 points---->
# 	new patient--->corona 

# History of Numpy:
# ---------------------------
# Origin of Numpy--->Numeric Library
# Numeric Library--->Jim Hugunin
# Numpy--->Travis Oliphant and multiple contributors 2005
# Opensource and freeware

# Q.In which language Numpy was written
# C and Python

# Q.What is nd array in numpy?
# 	The fundamental data type to store our data:nd array

a = np.identity(5)
print(type(a))

# Array:an indexed collection of homogenious elements.

# 1 dimensional arrays-->Vector
# 2-D arrays--->Matrix
# .
# N-D array-->No name

# Application Areas of Numpy:
# 	To perform linear algebra functions
# 	To perform linear regression
# 	To perform logistic regression
# 	Deep neural networks
# 	Control Systems
# 	Operationa Research

# Numpy Basic Introduction
# Array creation:
# 	10+ ways are

np.ones((2,3))
np.ones((10))

# Attributes
# How to access  elements of array:
# 	Basic Indexing
# 	Slice operator
# 	Advanced Indexing
# 	Condition based selection

# Ex:
a = np.arange(1,21)
a[a%6 == 0]
 

# How to iterate elements of an array:
# 	python's normal loops
# 	nditer()
# 	ndenumerate()

# Arithmetic operators
# Broadcasting
# Array Manipulation functions:
# 	reshape()
# 	resize()
# 	flatten()
# 	ravel()
# 	transpose()
# 	etc......

# Matrix class


# Ex:What is the need of Numpy?
# -----------------------------------------------
# Boys and Girls are attending Mahesh sir Python classes.
# For boys fees is $3 and for girls fees is $8, For a certain batch 2200 people attended 
# and $10100 fees collected. How many boys and girls attended for that batch?

# x ---->no of boys
# y ---->no of girls

# x + y = 2200
# 3x + 8y = 10100

# coefficient matrix:
# 	a =	1  1
# 			3  8

# value matrix:
# 	b = [2200,10100]

import numpy as np
a = np.array([[1,1],[3,8]])
b = np.array([2200,10100])
np.linalg.solve(a,b)

# Performance Test:
# ----------------------------
# Numpy vs Normal Python
# --------------------------------------
'''a = [10,20,30]
b = [1,2,3]
for i,j in zip(a,b):
	print(i,j)'''

import numpy as np
from datetime import datetime
a = np.array([10,20,30])
b = np.array([1,2,3])

#dot product:A.B:10*1 + 20*2 + 30*3 = 140

#Traditional python program
def dot_product(a,b):
	result = 0
	for i,j in zip(a,b):
		result = result + i*j
	return result
before = datetime.now()
for i in range(100000):
	dot_product(a,b)
after = datetime.now()
print('The time taken by traditional python:',after-before)

#Numpy library code
before = datetime.now()
for i in range(100000):
	np.dot(a,b)#This is from numpy
after = datetime.now()
print('The time taken by numpy library:',after-before)

# Array:
# --------
# 	An indexed collection of homogenious data elements

# How to create arrays in python
# ----------------------------------------------
# Inbuilt arrays concept is not there in python

# 2-ways:
# 	1.By using array module
# 	2.By using numpy module

# 1.By using array module(Not recommended)
# -----------------------------------------------------------------
# test.py
# -----------
import array
a = array.array('i',[10,20,30])#i represents type:int array
print(type(a))
print(a)
print('Elements one by one:')
for x in a:
	print(x)

# Note:array module is not recommended because much library support is not available.

# 2.By using numpy module:
# ----------------------------------------
import numpy
a = numpy.array([10,20,30])
print(type(a))
print(a)
print('Elements one by one:')
for i in a:
	print(i)

# Python's List vs Numpy ndarray:
# -------------------------------------------------
# 1.Similarities:
# ----------------------
# -->Both are used for store data.
# -->The order will be preserved in both. Hence indexing and slicing concepts are applicable.
# -->Both are mutable, i.e we can change the content.

# 2.Differences:
# --------------------
# 1.list is pythons inbuilt type. We have to install and import numpy explicitly.
# 2.list can contain hetrogenious elements. But array contains only homogenious elements.

# Ex:
import numpy
l = [10,10.5,'Mahesh',True]
print(l)
a = numpy.array(l)
print(a)

# 3.On list, we cannot perform vector operations. But on ndarray we can perform vector operations.

l = [10,20,30,40]
import numpy as np
a = np.array(l)
l + 2 #Invalid
a + 2 #array([12, 22, 32, 42])
a/2 #array([ 5., 10., 15., 20.])
l/2 #Invalid
l*2 #[10, 20, 30, 40, 10, 20, 30, 40]
a*2 #array([20, 40, 60, 80])

# 4.Arrays consume less import numpy as np
import sys
l = [10,20,30,40,50,60,70,80,90,100]
a = np.array([10,20,30,40,50,60,70,80,90,100])
print('The size of list:',sys.getsizeof(l))
print('The size of ndarray:',sys.getsizeof(a))

# 5.Arrays are superfast when compared with list.
# 6.Numpy arrays are more convenient to use while performing complex mathematical operations.


'''
How to create Numpy Arrays:
-------------------------------------------
1.array()
2.arange()
3.linspace()
4.zeros()
5.ones()
6.full()
7.eye()
8.identity()
9.empty()
10.numpy.random library:
			1.randint()
			2.rand()
			3.uniform()
			4.randn()
			5.normal()
			6.shuffle()


1.randint()==>To generate random int values in the given range.
2.rand()==>To generate uniform distributed float value [0,1)
3.uniform()==>To generate uniform distributed float value in the given range [low,high)
4.randn()==>normal distributed float values with mean 0 and standard deviation 1
5.normal()==>normal distributed float values with specified meand and standard deviation.
6.shuffle()==>To shuffle order of elements in the given nd array.

'''


# 1.Creation of numpy arrays by using array():
# ------------------------------------------------------------------
# For the given list or tuple.

import numpy as np
help(np.array)

#  array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
#           like=None)

# 1-D array:
# ---------------
l = [10,20,30]
type(l) #<class 'list'>
a = np.array(l)
type(a) #<class 'numpy.ndarray'>
a #array([10, 20, 30])
print(a) #[10 20 30]
a.ndim #1
a.dtype #dtype('int32')

# Note:
# 	a.ndim--->To know dimension of ndarray
# 	a.dtype--->To know data type of elements

# 2-D array creation:
# -----------------------------

# [[10,20,30],[40,50,60],[70,80,90]]------->Nested list

a = np.array([[10,20,30],[40,50,60],[70,80,90]])
type(a)
a.ndim #2
a


# shape of this array:(3,3)
a.shape #(3, 3)
a.size #9

# Ex:To create 1-D array from the tuple
# --------------------------------------------------------
a = np.array(('sunny','bunny','vinny'))
type(a)
a.ndim #1
a.shape #(3,)
a.dtype #dtype('<U5')

# Note:Array contains only homogenious elements.
# If the list contains hetrogenious elements:Upcasting will be performed.

a = np.array([10,20,10.5])
a #array([10. , 20. , 10.5]) Upcasting int to float
a.dtype #dtype('float64')

# Ex:

a = np.array([10,20,'a'])
a
 

# How to create a particular type:
# -----------------------------------------------
# We have to use dtype argument.

a = np.array([10,20,30.5],dtype=int)
a #array([10, 20, 30])

a = np.array([10,20,30.5],dtype=bool)
a #array([ True,  True,  True])

a = np.array([10,20,30.5],dtype=float)
a #array([10. , 20. , 30.5])

a = np.array([10,20,30.5],dtype=complex)
a #array([10. +0.j, 20. +0.j, 30.5+0.j])

a = np.array([10,'sunny'],dtype=int) #Invalid

# How to create object type array
# -----------------------------------------------
# Here any type of elements are allowed.
# Ex:

a = np.array([10,'sunny',True,1.2,10+3j],dtype=object)
a #array([10, 'sunny', True, 1.2, (10+3j)], dtype=object)

# Ex:If we are not given dtype then
a = np.array([10,'sunny',True,1.2,10+3j])
a #array(['10', 'sunny', 'True', '1.2', '(10+3j)'], dtype='<U64')

# array()-->To create ndarray from the given list or tuple.

# 2).Creation os ndarray by using arange() function:
# --------------------------------------------------------------------------
# Python:
# 	range(10)===>0 to 9
# 	range(1,11)===>1 to 10
# 	range(1,11,2)==>1,3,5,7,9

help(np.arange)
			# arange([start,] stop[, step,], dtype=None, *, like=None)

# Ex-1:create 1-D array 0 to 9
# ------------------------------------------
a = np.arange(10)
a #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.ndim #1
a.shape #(10,)
a.dtype #dtype('int32')

# Ex:
a = np.arange(1,11)
a

# Ex:

a = np.arange(1,11,2)
a #array([1, 3, 5, 7, 9])


a = np.arange(1,11,2,dtype=float)
a #array([1., 3., 5., 7., 9.])

# 3).linspace():
# 	In the specified interval linearly spaced values.

# >>> help(np.linspace)
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
#     Return evenly spaced numbers over a specified interval.

# Ex:
np.linspace(0,1,2)
array([0., 1.])

np.linspace(0,1,3)
array([0. , 0.5, 1. ])

np.linspace(0,1,4)
array([0.        , 0.33333333, 0.66666667, 1.        ])

np.linspace(0,1)#50 values will be generated

np.linspace(1,100,10,dtype=int)
array([  1,  12,  23,  34,  45,  56,  67,  78,  89, 100])

# 1 to 12--->11 numbers
# 12 to 23-->11 numbers
# equally spaced values

# arange() vs linspace():
# --------------------------------
# arange():Elements will be considered in the given range based on step value.
# linspace():The specified number of values will be considered in the given range.


# 4).zeros():
# 	zeros(shape, dtype=float, order='C', *, like=None)
#     Return a new array of given shape and type, filled with zeros.

# (10,)--->1-D array contains 10 elements

# (5,2)--->2-D array contains 5-rows and 2-columns
# 			2-D array means collection 1-D arrays

# (2,3,4)-->3-D array
# 			3-D array contains a collection 2-D arrays

# 			2-->2-number of 2-D arrays
# 			3-->The number of rows in every 2-D array
# 			4-->The number of columns in every 2-D array
# 			size:24
# Ex:

np.zeros((4,))
np.zeros(4)
np.zeros((4,3))
np.zeros((4,3),dtype=int)

# do we have (1,3,2) array?
# 1 2-D array
# 3-rows
# 2-columns
# >>> np.zeros((1,3,2))

# -->Perform some operations the result we have to store somewhere.

# 5).ones():
# 	Exactly same as zeros except that instead of zero array filled with 1.

# >>>help(np.ones)
# ones(shape, dtype=None, order='C', *, like=None)
#     Return a new array of given shape and type, filled with ones.

np.ones(10)
np.ones((4,2))
np.ones((4,2),dtype=int)
np.ones((2,3,4),dtype=int)

# 6).full():

# >>> help(np.full)

# 	full(shape, fill_value, dtype=None, order='C', *, like=None)
#     Return a new array of given shape and type, filled with `fill_value`.

# Ex:

np.full(10,3)
np.full((5,4),9)
np.full((2,3,4),9)

# Note:
np.full(shape=(2,3),fill_value=3)
np.full((2,3),fill_value=3)
np.full((2,3),3)
# np.full(shape=(2,3),3)#Invalid

# 7).eye():
# 		>>> help(np.eye)
		
# 		eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
# 		Return a 2-D array with ones on the diagonal and zeros elsewhere.

# 		N--->Number of rows
# 		M--->Number of columns
# 		k-->Meant for diagnol
# Ex:

np.eye(2,3)
np.eye(3,3)
np.eye(3)
np.eye(3,dtype=int)
np.eye(5,dtype=int)
np.eye(5,k=1,dtype=int)
np.eye(5,k=-3,dtype=int)

# 8).identity():
# 	It is exactly same as eye() function except that
# 		1.It is always square matrix(the number of rows and number of columns always same)
# 		2.Only main diagnol contains 1's
# 	identity is special case of eye()_

help(np.identity)

# Ex:

np.identity(5)
np.identity(5,dtype=int)

# 9).empty():
# 		>>> help(np.empty)
# 	    empty(shape, dtype=float, order='C', *, like=None)
# 	    Return a new array of given shape and type, without initializing entries.
# Ex:

np.empty(3)
np.empty((3,3))
np.empty((2,3,4))
np.empty(10)

# zeros() vs empty():
# ---------------------------
# If we required an array only with zeros then we should go for zeros()
# If we never worry about data, just we required an empty array for future purpose, then we should go for empty().
# The time required to create empty array is very very less when compared with zeros array. i.e performance wise empty function is recommended than zeros if we are not worry about data.

#Performance comparision of zeros() and empty()
import numpy as np
from datetime import datetime
begin = datetime.now()
a = np.zeros((200000,300,400))
after = datetime.now()
print('Time taken by zeros:',after-begin)
a = None
begin = datetime.now()
a = np.empty((200000,300,400))
after = datetime.now()
print('Time taken by zeros:',after-begin)


# Array creation by using random library
# ----------------------------------------------------------
# This library contains several functions to create nd arrays with random data.
# randint(), rand(), uniform(), normal(), shuffle()

# 			Numpy: ndarray
# 					Scipy--->Scintific Python
# 			Pandas: Series and DataFrame
# 			Matplotblib ---> Seaborn --> Plotly



# Array creation by using random library
# ----------------------------------------------------------
# This library contains several functions to create nd arrays with random data.
# randint(), rand(), uniform(), normal(), shuffle()

# 1.randint:
# 	To generate random int values in the given range.

help(np.random.randint)

# Ex:
np.random.randint(10,20)
np.random.randint(10,20)

# -->It will generate a single random int value in the range 10 to 19.

# Ex:To create 1-D ndarray of size 10 with random values from 1 to 9
np.random.randint(1,9,size = 10)
np.random.randint(1,9,size = 10)

# Ex:To create 2-D ndarray with shape(3,5)
np.random.randint(100,size=(3,5))

# Ex:To create 3-D array with shape(2,3,4)
# 3D array contains 2 2-D arrays
# Each 2-D array contains 3-rows and 4-columns

np.random.randint(100,size=(2,3,4))

np.random.randint(1,10,size=10,dtype=float)

# Syn:
# 			randint(low, high=None, size=None, dtype=int)
# int8
# int16
# int32
# int64

a = np.random.randint(1,11,size=(20,30))
a.dtype
 
a = np.random.randint(1,11,size=(20,30),dtype='int8')
a.dtype
# dtype('int8')#Memory utilization

# Ex:

import sys
a = np.random.randint(1,11,size=(20,30))
sys.getsizeof(a)
# 2528
a = np.random.randint(1,11,size=(20,30),dtype='int8')
sys.getsizeof(a)
# 728

# How to convert from one array type to another type:
# -------------------------------------------------------------------------------
# we have to use astype() method

a = np.random.randint(1,11,size=(20,30))
a.dtype
# dtype('int32')
b = a.astype('float')
# b.dtype

# 2).rand():
# 	uniform distribution	---->	10 11 9 10 11 10
# 	normal distribution	---->	6 4 10 4 14(10 is the mean value)

# It will generate random float values in the range [0,1) from uniform distribution samples.

# Ex:
np.random.rand()  #-->A single float value will be generated

# 1-D array
# --------------
np.random.rand(10)

# 2-D array:
np.random.rand(3,5)

# 3-D array:
np.random.rand(2,3,4)

# 3).uniform():
# 	rand() ---> range is always [0,1)
# 	unoform --> customize range
# 	 uniform(low=0.0, high=1.0, size=None)

# Ex:
np.random.uniform()
np.random.uniform(10,20)

# 1-D array:
# ---------------
np.random.uniform(10,20,size=5)

# 2-D array:
# ---------------
np.random.uniform(10,20,size=(3,4))

# 3-D array:
# ---------------
np.random.uniform(10,20,size=(2,3,2))

# 4).randn():
# 	values from normal distribution with mean 0 and variance is 1

np.random.randn(10)
np.random.randn(2,3)
np.random.randn(2,3,4)

# 5).normal():
# 	We can customize mean and varience
# 	 normal(loc=0.0, scale=1.0, size=None)
#     Draw random samples from a normal (Gaussian) distribution.

np.random.normal(10,4,size=10)
np.random.normal(10,4,size=(2,3,4))

# 6).shuffle():

# >>> help(np.random.shuffle)
# This function only shuffles the array along the first axis of a
# multi-dimensional array. The order of sub-arrays is changed but their contents remains the same.

# 1-D array:
# ---------------
a = np.arange(9)
a
np.random.shuffle(a)
a

# 2-D array:
# ---------------
a = np.random.randint(1,101,size=(6,5))
a
np.random.shuffle(a)
a

# 3-D array :(4,3,4)
# 	4 : number of 2-D ararys
# 	3 : number of rows
# 	4 : number of columns

a = np.arange(48).reshape(4,3,4)
a
np.random.shuffle(a)
a


# Array Attributes:
# -------------------------
# 1).ndim==>return the dimension of the array
# 2).shape==>returns the shape of the array.(10,):1-D, (10,2):2-D
# 3).size==>To get total number of elements
# 4).dtype==>To get data type of elements of the array.
# 5).itemsize==>Length of each element of array in bytes(4-bytes)

a = np.array([10,20,30,40])
a.ndim #1
a.shape #(4,)
a.size #4
a.dtype #dtype('int32')
a.itemsize #4

# Ex:2-D array with int32(default)
# -----------------------------------------------
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
a.ndim #2
a.shape #(3,3)
a.size #12
a.dtype #dtype('int32')
a.itemsize #4

# Numpy Data Types:
# ------------------------------
# Python data types: int ,float, bool, complex and str

# Numpy data types: multiple data types present(python + C)

# i ==> integer(int8, int16, int32, int64)
# b ==> boolean
# u ==> unsigned integer(uint8,uint16,uint32,uint64)
# c ==> complex(complex64,complex128)
# f ==> float(float16, float32, float64)
# s ==> String
# U ==> Unicode String
# M ==> datetime etc.......



# int8->i1; int16->i2; int32->i4(default); int64->i8
# float16->f2; float32->f4(default); float64->f8

# int8:
# 	-->The value will be represented by 8-bits.
# 	-->MSB is reserved for sign
# 	-->The range:-128 to 127

# int16:
# 	-->The value will be represented by 16-bits.
# 	-->MSB is reserved for sign
# 	-->The range:-32768 to 32767

# int32:
# 	-->The value will be represented by 32-bits.
# 	-->MSB is reserved for sign
# 	-->The range:-2147483648 to 2147483647

# EX:
# ----

import numpy as np
import sys
a = np.array([10,20,30,40])
a.dtype
sys.getsizeof(a)

a = np.array([10,20,30,40],dtype='int8')
a.dtype
sys.getsizeof(a)


# Changing the data type of an existing array:
# -----------------------------------------------

# Ex:1

a = np.array([10,20,30,40])
a.dtype

b = a.astype('float64')
b.dtype

# Ex:2

a = np.array([10,0,20,0,30])
x = np.bool(a)   #Invalid 

x = np.bool_(a)
x

# How to get/access elements of numpy array:
# --------------------------------------------------

# 1. Indexing ----> Only one element
# 2. Slicing ----> group (or) Multiple elements
# 3. Advanced Indexing

# 1. Indexing:
# -------------------

# * By using index, we can get single element from the array.
# * Zero based indexing. i.e the index of first element is 0, second element is 1 and so on.
# * Supports both positive and negative indexing.

# Ex:
a = np.array([10,20,30,40,50,60])
a
a[0] #10
a[-1] #60
a[10] #IndexError

# Accessing elements from 2-D array:
# -----------------------------------

# a[row index][column index]

a = np.array([[10,20,30],[40,50,60]])
a

# To access 50 [possibities]:
# ------------------------------

a[1][1]
a[1][-2]
a[-1][-2]
a[-1][1]

# Accessing elements from 3-D array:
# -----------------------------------

# (2,3,4)
	
# 		a[i][j][k]:
# 			i-->represents which 2-D array(index of 2-D array)
# 			j-->represents row index in that 2-D array
# 			k-->represents column index in that 2-D array

# a[0][1][2]:
# 	0-indexed 2-D array
# 	In that 2-D array 1 indexed row and 2-indexed column

l = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]

l = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
a = np.array(l)
a
a.ndim #3

# To access 14
# -------------------
a[1][1][1]
a[-1][-2][-2]
a[1][-2][-2]
a[-1][1][-2]

# Accessing elements of 4-D array:
# -------------------------------------------------
# 	-->4-D array contains multiple 3-D arrays
# 	-->Every 3-D array contains multiple 2-D arrays
# 	-->Every 2-D contains rows and columns
# 				(i,j,k,l)==>(2,3,4,5)
# 	-->2==>represents the number of 3-D arrays
# 	-->3 ==>Every 3-D array contains 3 2-D arrays
# 	-->Every 2-D array contains 4-rows and 5-columns

# a[i][j][k][l]:
# 	i==>represents which 3-D array
# 	j==>In that 3-D array which 2-D array
# 	k==>row index of the 2-D array
# 	l==>column index of the 2-D array

# Ex:

a = np.arange(1,121).reshape(2,3,4,5)
a
# To find 88 position in the array
np.where(a==88)

#Accessing elements at a[1][1][1][2]
a[1][1][1][2]

# Accessing elements of ndarray by using slice operator
# --------------------------------------------------------------------------------
# Slice operator 1-D array:
# -------------------------------------
# a[begin:end:step]
# Same rules of python's slice operator applicabpe here.

a = np.arange(10,101,10)
a
a[2:5]
a[::1]
a[::-1]
a[::-2]

# Slice operator on 2-D Numpy Array:
# ----------------------------------------------------
# a[row,column]
# a[begin:end:step, begin:end:step]

a = np.array([[10,20],[30,40],[50,60]])
a
array([[10, 20],
       [30, 40],
       [50, 60]])

# To acess:[10,20]
# -------------------------
a[0:1,:]

# To access:[20,40]
# ---------------------
a[:2,1:]

a[0::2,:]

# Ex:
# -----
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
a[0:2,:]
a[0::3,:]
a[:,0:2] 
a[:,::2] 
a[1:3,1:3]
a[::3,::3]

# Slice on 3-D array:
# ---------------------
# (2,3,4)   2->number of 2-D arrays
# 3-> number of rows in every 2-D array
# 4-> number of columns in every 2-D array

# EX:
# -------

# import numpy as np

l = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
a = np.array(l)
print(a)

# a[i,j,k]  ----------> a[begin:end:step,begin:end:step,begin:end:step]

print(a[:,:,0:1])
print(a[:,:1,:])
print(a[:,::2,:])
print(a[:,:2,1:3])
print(a[:,::2,::3])

# To use slice operator, compulsory elements should be in order. We cannot select elements which are out of order. i.e we cannot select arbitrary elements.

# Advanced Indexing:
# ---------------------------

# By using index, we can access only one element at a time. a[i],a[i][j], a[i][j][k]

# By using slice operator we can access multiple elements at a time, but all elements should be in order.

# a[begin:end:step]
# a[begin:end:step,begin:end:step]
# a[begin:end:step,begin:end:step,begin:end:step]


# Accessing multiple arbitrary elements
# ----------------------------------------------------------
# 1-D array:
# 	array[x]: x can be either ndarray or list, which represents required indexes.

a = np.array([10,20,30,40,50,60,70,80,90,100])
print(a)

# required values are:[30,50,60,90]
# --------------------------------------------------
# 1st way
# -----------
# cretae ndarray with required indices
indices = np.array([2,4,5,8])
a[indices] #array([30, 50, 60, 90])

# 2nd way:
# --------------
l = [2,4,5,8]
a[l] #array([30, 50, 60, 90])


# Ex:
# -----
# [10,50,70,100]
# ----------------------
# >>> a[[0,4,6,9]]

# [10,100,50,70]
# ----------------------
# >>> a[[0,9,4,6]]

# [10,100]
# ------------
# >>> a[[0,-1]]

# Accessing elements of 2-D array:
# --------------------------------------------------

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a = np.array(l)
print(a)


# I want to select:1,6,11,16
# Syn:
# 	a[[row_indices],[column_indices]]
# 	a[[0,1,2,3],[0,1,2,3]]
# 	It select elements from  (0,0),(1,1),(2,2),(3,3)

a[[0,1,2,3],[0,1,2,3]]
# array([ 1,  6, 11, 16])

# To select:2,8,9,15
a[[0,1,2,3],[1,3,0,2]]


# L-shape elements:
# ----------------------------
# to select:1,5,9,13,14,15,16
a[[0,1,2,3,3,3,3],[0,0,0,0,1,2,3]]

# Note:
# 	a[[0,1,2],[0,1]]#Error
# 	a[[0,1],[0,1,2]] #Error
# 	a[[0,1,2],[0]]#array([1, 5, 9])
# 	a[[0],[0,1,2]]#array([1, 2, 3])

# Accessing multiple arbitrary elements in 3-D array:
# ----------------------------------------------------------------------------
a = np.arange(1,25).reshape(2,3,4)
a
array([[[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]],

       [[13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]]])

#Accessing 7 and 18 from the array
# Syn:
# 	a[[indices of 2-D array],[row indices],[column indices]]

# step-1:Find coordinates of arbitrary elements:
# 			7:						18:
# 				i=0					i=1
# 				j=1					j=1
# 				k=2					k=1
# step-2:create list of i,j,k
# 				i:[0,1]
# 				j:[1,1]
# 				k:[2,1]
# step-3:pass the list as argument to the original array
a[[0,1],[1,1],[2,1]]
# array([ 7, 18])


# Condition based selection:
# ----------------------------------------
# Syn:
# 	array[boolean_array]
# -->In the boolean_array, where ever True present, the corresponding value will be selected.

a = np.array([10,20,30,40])
boolean_array=np.array([True,False,False,True])
boolean_array #array([ True, False, False,  True])
a[boolean_array] #array([10, 40])

# Select elements which are greater than 25
# ---------------------------------------------------------------
b_a = a>25
a[b_a] #array([30, 40])
a[a>25] #array([30, 40])

# Ex:
# -----
a = np.array([10,-5,20,40,-3,-1,75])
# Select only negative numbers
a[a<0] #array([-5, -3, -1])
# Select only +ve numbers
a[a>0]#array([10, 20, 40, 75])
# Only even numbers
array([10, 20, 40])

# Condition based section 2-D array also
# ----------------------------------------------------------
a = np.arange(1,26).reshape(5,5)
a
a[a%2==0]
array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24])
a[a%10==0]
array([10, 20])

# Slicing vs Advanced Indexing:
# ---------------------------------------------
# Python's Slicing:
# -------------------------
# In case of list, slice operator will creates a separate copy.
# If we perform any changes in one copy those changes wont be reflected in other copy

l1 = [10,20,30,40]
l2 = l1[:]
l1[0] = 333
l1 #[333, 20, 30, 40]
l2 #[10, 20, 30, 40]

# Numpy Array Slicing:
# --------------------------------
# A separate copy wont be created and just we are getting view of the original copy.

# Table and View
# View is logical entity where as Table is physical entity.

a = np.arange(10,101,10)
a #array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
b = a[0:4]
b #array([10, 20, 30, 40])
a[0] = 333
a #array([333,  20,  30,  40,  50,  60,  70,  80,  90, 100])
b #array([333,  20,  30,  40])
b[1] = 999
b #array([333, 999,  30,  40])
a #array([333, 999,  30,  40,  50,  60,  70,  80,  90, 100])

# Advanced indexing and condition based selection:
# ---------------------------------------------------------------------------
# It will sleect required elements based on provided index or condition with those elements a new 1-D array obejct will be created.
# The output is always a new 1-D array only.

a = np.arange(10,101,10)
a
b = a[[0,2,5]]
b #array([10, 30, 60])
a[0] = 333
a #array([333,  20,  30,  40,  50,  60,  70,  80,  90, 100])
b #array([10, 30, 60])
b[1] = 999
b #array([ 10, 999,  60])
a #array([333,  20,  30,  40,  50,  60,  70,  80,  90, 100])

'''
Slicing:
---------
* The element should be in order.
* We can't select arbitrary elements.
* Conditional based selection is not possible.
* Just we will get view but not copy.
* Memory,performance wise it is the best.

Advanced Indexing:
-------------------
* The element need not be in order.
* We can select arbitrary elements.
* Conditional based selection is possible.
* Just we will get copy but not view.
* Memory,performance wise it is the worst.

'''


# How to iterate elements from ndarray:
# ---------------------------------------
# 1. By using python's loop
# 2. nditer() function
# 3. ndenumerate() function

# By using python's loop:
# -----------------------------
# To iterate elements of 1-D array:
# ---------------------------------------

a = np.arange(10,51,10)
for x in a:
	print(x)

# To iterate elements of 2-D array:
# ---------------------------------------

a = np.array([[10,20,30],[40,50,60],[70,80,90]])
for x in a:   #x is 1-D array but not scalar value
	for y in x: #y is a scalar value present in 1-D array
		print(y)

# To iterate elements of 3-D array:
# ---------------------------------------

a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
for x in a:   #x is 2-D array but not scalar value
	for y in x:  #y is 1-D array but not scalaerr value
		for z in y:  #z is scalar value
			print(z)

# Note : To iterate elements of N-D array we required 'n' loops.

# 2. By using numpy's nditer() function:
# ------------------------------------------------
# * Advantage : For any n-D array only one loop is required.
# * nditer is a class present in numpy module.
# * nditer() --> creating an object for nditer class.

# 1-D array:
# ---------------
import numpy as np
a = np.arange(10,51,10)
for x in np.nditer(a):
	print(x)

# 2-D array:
# ---------------
import numpy as np
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
for x in np.nditer(a):
	print(x)

# 3-D array:
# ---------------
import numpy as np
a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
for x in np.nditer(a):
	print(x)

# Iterate elements of sliced array:
# ---------------------------------------
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
for x in np.nditer(a[:,:2]):
	print(x)

# Using nditer() to get elements of required data type:
# --------------------------------------------------------- 
# we have to use op_dtype
help(np.nditer)

import numpy as np
a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
for x in np.nditer(a,flags=['buffered'],op_dtypes=['float']):
	print(x)


# Normal python's loop VS nditer():
# ----------------------------------
# 1. n loops are required.
# 2. only one loop is required.
# 3. There is no way to specify our required data type.
# 4. There is a way to specify required data type. For this we have to use op_dtype argument.


# 3).By using ndenumerate() function:
# ------------------------------------------------------
# If we want to find co-ordinates alsi in addtion to elements

# array indices(coordinates) and values

# 1-D array:
# ---------------
import numpy as np
a = np.array([10,20,30,40,50,60,70])
for pos,element in np.ndenumerate(a):
	print(f'{element} element present at index/pos:{pos}')

# 2-D array:
# ---------------
import numpy as np
a = np.array([[10,20,30],[40,50,60],[70,80,90]])
for pos,element in np.ndenumerate(a):
	print(f'{element} element present at index/pos:{pos}')

# 3-D array:
# ---------------
import numpy as np
a = np.arange(1,25).reshape(2,3,4)
for pos,element in np.ndenumerate(a):
	print(f'{element} element present at index/pos:{pos}')


# Arithmetic operators:
# --------------------------------
# 		+, -, *, /, %, //, **

# Arithmetic operators for Numpy arrays with scalar:
# ----------------------------------------------------------------------------
# 1-D array:
# ---------------
a = np.array([10,20,30,40])
a #array([10, 20, 30, 40])
a+2 #array([12, 22, 32, 42])
a-2 #array([ 8, 18, 28, 38])
a*2 #array([20, 40, 60, 80])
a%2 #array([0, 0, 0, 0], dtype=int32)
a/2 #array([ 5., 10., 15., 20.])
a//2 #array([ 5, 10, 15, 20], dtype=int32)

# 2-D array:
# ---------------
a = np.array([[10,20,30],[40,50,60]])
a
a+2
a-2
a*2
a**2
a/2
a//2
a%2

# -->In python anything by zero including zero/zero alse result s in:10/0 and 0/0
# ZeroDivisionError

# But in Numpy there is no ZeroDivisionError
# 10/0==>Infinity(inf) 
# 0/0 ==>Undefined(NaN)-->Not a Number

# Ex:
a = np.arange(6)
a #array([0, 1, 2, 3, 4, 5])
a/0 #array([nan, inf, inf, inf, inf, inf])

# Arithmetic operators for Array with Arrays:
# 	To perform arithmetic operators between numpy array, compulsory both arrays should have:
# 			-->same dimension
# 			-->same shape 
# 			-->same size
# 	otherwise we will get error.

# Ex:1-D array
# -------------------
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
a+b #array([11, 22, 33, 44])
a-b #array([ -9, -18, -27, -36])
a*b #array([ 10,  40,  90, 160])
b/a #array([10., 10., 10., 10.])
b//a #array([10, 10, 10, 10])

# 2-D array:
# ---------------
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
a+b
a-b
a*b
b/a
b//a

# Ex:
a = np.array([10,20,30,40])
b = np.array([10,20,30,40,50])
a + b
# ValueError: operands could not be broadcast together with shapes (4,) (5,)

# Equavalant functions for arithmetic operators in numpy
# -----------------------------------------------------------------------------------
a = np.array([10, 20, 30, 40])
b = np.array([1,2,3,4])
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)
np.floor_divide(a,b)
np.mod(a,b)
np.power(a,b)

# Nply():Element multiplicationote:The functions which operates element by element on whole array are called Univerals functions (ufunc)

# Q.What is difference between np.dot() and np.multiply()?
# 			np.dot():Matrix multiplication/Dot product
# 			np.multiply():Element multiplication

# Broadcasting:
# ----------------
# * Eventhough dimensions are different, shapes are different and sizes are different still some arithematic operations are allowed by broadcasting.
# * Broadcasting will be performed automatically by numpy itself and we are not required to perform explicitly.

# Rules:
# ---------
# 1. Make sure both array should have same dimension. Padded(Add) 1's in the shape of  lesser dimension array of the left side, untill both arrays have same dimension.

# Before:
# 	(4,3)--->2D
# 	(3,)-->1D

# After:
# 	(4,3)
# 	(1,3)

# 2. If the size of 2-arrays does not match in any dimension, then the arrays with size of other dimension to match.

# Note : In any dimension, the sizes are not matched and neither equal to 1, then we will get error, numpy does not able to perform broadcasting between those array.

# Before:
# 	(4,3)
# 	(1,3)
# After:
# 	(4,3)-->2-D
# 	(4,3)-->2-D
# -->Now dimensions,shapes and sizes are equal.



# Ex:
# Broadcasting between (3,2,2) and (3,) possible or not.
# Before Rule-1:
# 	(3,2,2)
# 	(3,)
# After Rule-1:
# 	(3,2,2)
# 	(1,1,3)

# After Rule-2:
# 	(3,2,2)
# 	(3,2,3)
# Same dimensions. but shapes, so numpy unable to perform broadcasting.

# Note:
# 	The data will be reused from the same input array.
# 	If the rows are required then re-use existing rows.
# 	If the columns are required then re-use existing columns.
# 	The result is always higher dimension of input array.

# Ex-1:
# --------
a = np.array([10,20,30,40])
b = np.array([1,2,3])
a + b
# ValueError: operands could not be broadcast together with shapes (4,) (3,)

# Ex-2:
a = np.array([10,20,30])			#--->1-D	shape(3,)
b = np.array([40])					#--->1-D	shape(1,)
a + b #array([50, 60, 70])

# Ex:
# ----
a = np.array([[10,20],[30,40],[50,60]])	#--->2D----> shape(3,2)
b = np.array([10,20]) #--->1-D	-->shape(2,)
a + b
 

# Ex:
# ------
a = np.array([[10],[20],[30]])	#--->2-D	shape(3,1)
b = np.array([10,20,30])			#-->1-D	shape(3,)
a+b
 

#  Array Manipulation Functions:
# ---------------------------------------------
# 1.reshape()
# 2.resize()
# 3.flatten()
# 4.flat variable
# 5.ravel()
# 6.transpose()
# 7.swapaxes()

# 1.reshape():
# -------------------
# 	shape to another shape.
# 	(10,) -->(5,2),(2,5),(1,10),(10,1)
# 	(24,)--->(3,8)-->(2,3,4),(6,4),(2,2,2,3)

# 1).The data should not be changed
# 		input size and output size must be matched.

# np.reshape(array,shape)
# array.reshape(shape)

# Ex:
# -----
a = np.arange(10)
a.ndim
a.shape
b = np.reshape(a,(5,2))
b
b = np.reshape(a,(10,1))
b
b.ndim
b.shape
b = a.reshape(1,5,2)
b
b.ndim
b.shape
b.size

# Ex:
a = np.arange(24)
a
b = np.reshape(a,(6,4))
b
b = np.reshape(a,(6,5))#Error
b = np.reshape(a,(2,3,4))
b

# 2).No changes in the data. New array object won't be created.
# 	Just we are getting view of existing object.
# 	View but not copy
# 	If we perform any changes in the original array, that changes will be reflected to reshaped array. Viceversa.

a = np.arange(12)
a
b = np.reshape(a,(4,3))
b
a[0] = 333
a
b
b[1][1] = 3113
b
a

# 3).If we can specify unkown dimension size as -1

# a = (12,)
# b = (6,-1)===>(6,2)

a = np.arange(12)
a
b = np.reshape(a,(6,-1))
b.shape #(6,2)
b = np.reshape(a,(-1,3))
b.shape #(4,3)
b = np.reshape(a,(-1,-1))#Error

# Ex:
a = np.arange(24)
b = np.reshape(a,(2,3,-1))
b = np.reshape(a,(2,-1,4))
b = np.reshape(a,(-1,3,4))
b = np.reshape(a,(3,4,-1))
b = np.reshape(a,(5,-1))


# 4).
# help(np.reshape)
# 		reshape(a, newshape, order='C')

# C style--->Row Major order
# Fortran style-->Column major order

a = np.arange(12).reshape(3,4)
a
b = np.reshape(a,(12,),'C')
b
b = np.reshape(a,(12,),'F')
b

# EX : 
a = np.arange(24)
a
np.reshape(a,(6,4),'C')
np.reshape(a,(6,4),'F')

# Conclusion:
# --------------
# 1. To reshape array without changing data.
# 2. The size must be matched.
# 3. We can use either numpy library function or ndarray class method.
# 	-->np.reshape()
# 	-->a.reshape()
# 4.It wont create a new array object, just we will get view.
# 5.We can use -1 in unknown dimension, but only once.
# 6.Order:'C','F'


# 2.resize():
# -------------
# output array be any dimension,any shape,any size.
# 1. Input size and output size must not be matched.
# 2. The data may be chaanged.
# 3. We will get copy but not view.
# 4. How to get that the new data.
# 	np.resize()--->repeat elements of input array.
# 	a.resize()-->use zeros for extra elements.
# 5.-1 such type of story not applicable for resize()
# 		input:(10,)
# 		reshape:(5,-1)
# 		resize:(5,-1)
# 6.If we use ndarray class resize() method, inline modification will be happened.

# Ex:
a = np.arange(1,6)
a 
b = np.resize(a,(4,3))
b
a[0] = 333
b[0][1] = 999
a
b
b = np.resize(3,-1)   #value error

refcheck = False
a = np.arange(1,6)
a.resize(5,3)
a

# Q.Difference between np.resize() and ndarray.resize()?
# --------------------------------------------------------------------------------
# 	np.resize()												ndarray.resize()		
# 	----------------									    ------------------------
# 1.It is library function in numpy module.	    1.It is method present in ndarray class.

# 2.It will create new array and returns it.		2.It wont return new array and existing
# 													array will be modified.
							
# 3.If the new_shape required more elements        3.Extra elements filled with zeros.
# then repeated copies of original array will
# be returned.

# Q.Differences between reshape() and resize()?
# -------------------------------------------------------------------
# 		reshape()											resize()
# 		--------------									  -----------
# 1.It is just to reshape to array without	  1.It is to resize an array, data may be
# changing size and data.							changed, size may be changed.

# 2.Just view will be created but not copy,	  2.Separate copy will be created. If we
# if we perform any change in the original	   perform any changes in the original array
# array, automatically those changes will		   those changes wont be reflected in resize
# be reflected in reshaped copy also.				array.

# 3.We can use -1 in unknown dimension		  3.There is no story like -1.


# 3).flatten():
# ---------------
# 1-D,2-D,3-D......n-D

# 1.Convert any n-D array to 1-D array.
# 2.It is method present in ndarray class but not numpy library function.
# 			a.flatten()-->valid
# 			np.flatten()-->invalid
# 3.a.flatten(order='C')
# 	C-style===>row major order
# 	F-style===>column major order
# 4.It will create a new array and returns it(i.e copy but not view)
# 5.The output of flatten method is always 1-D array.

# EX : 
a = np.arange(6).reshape(3,2)
a
a.flatten()
a.flatten('F')
b = a.flatten()
b
a[0][0] = 333
a
b[1] = 999
b
a

# Ex:
a = np.arange(1,19).reshape(3,3,2)
a
a.ndim #3
b = a.flatten()
b

# flat variable:
# ------------------
# It is a 1-D iterator over the array
# This is  a 'numpy.flatiter' instance

help(np.flatiter)

a = np.arange(1,19).reshape(3,3,2)
a
a.flat[2]
a.flat[10]
for x in a.flat:print(x)

# 5).ravel():
# 
# 	It is exactly same as flatten function except that it returns view but not copy.

# 1.Convert any n-D array to 1-D array
# 2.It is method present in ndarray class and also numpy library function.		
# 					a.ravel()
# 					np.ravel()
# 3.a.ravel(order='C'/'F')
# 4.It returns view but not copy.
# 5.The output of ravel() method is always 1-D array.

# Ex:
a = np.arange(24).reshape(2,3,4)
a
b = a.ravel()
b
b[0] = 333
b
a


# Q.Difference between flatten() an dravel()?
# --------------------------------------------------------------
# 		flatten()											ravel()
# 		------------										----------
# 1.To convert any n-D array to 1-D array		    1.To convert any n-D array to 1-D array
# and a new array object will be created.		    but returns just view but not copy.

# 2.If we perform any changes in the				2.If we perform any changes in the ravel
# flatten copy, then those changes wont		    copy, then those changes will be
# be reflected in the original copy.				reflected in the original copy.

# 3.It is ndarray class method but not			3.We can use as a method and as well as
# numpy library function.							a function.

# 6).transpose():
# 	To find transpose of given ndarray

# Ex:
a = np.arange(1,5).reshape(2,2)
a
b = np.transpose(a)
b

# Note : No changes in data hence it returned only view but not copy.

a[0][0] = 333
a
b

# for 3-D array:
# --------------------
# (2,3,4)
# 2--->2-D arrays
# 3--->number of rows
# 4--->number of columns
# 24--->total size.

# If we transpose this array:
help(np.transpose)

np.transpose(a)
# (4,3,2)
# 4--->2-D arrays
# 3--->number of rows
# 2--->number of columns
# total size:24

a = np.arange(24).reshape(2,3,4)
a
b = np.transpose(a)
b.shape
(4, 3, 2)
b

# 4-D array:
# ---------------
a = (2,3,4,5)
np.transpose(a) (5,4,3,2)


# axes parameter:
# -----------------------
# -->If we are not using axes parameter, then dimension will be reversed.
# -->axes parameter describes in which order we have to take axes.
# -->It is very helpful for 3-D and 4-D arrays.

# for 3-D array:(2,3,4)

# The size of axis-0: 2
# The size of axis-1: 3
# The size of axis-2: 4

# np.transpose(a)---->(4,3,2)

# My required order is:(2,4,3)/(4,2,3)/(3,4,2)

a = np.arange(24).reshape(2,3,4)
a
b = np.transpose(a,axes=(0,2,1))
b.shape #(2, 4, 3)
b

# My required order is:(3,4,2)
b = np.transpose(a,axes=(1,2,0))
b.shape #(3, 4, 2)

b = np.transpose(a,axes=(2,0,1))
b.shape
(4, 2, 3)

# for 2-D array:
# --------------------
# axis-0--->number of rows
# axis-1--->number of columns

a = np.array([[10,20,30],[40,50,60]])
a
a.shape #(2, 3)
np.transpose(a,axes=(1,0))
np.transpose(a,axes=(0,1))
np.transpose(a)

# Note:
# --------
# 1.For 1-D array, there is no impact of transpose() function.
# 2.If we are not using axes argument, then dimensions will be reversed.
# 3.If we provide axes argument, then we can specify our own order axes.
# 4.Repeated axes in transpose is not allowed.
# 5.axes parameter is more helpful from 3-D array onwards but not for 2-D array

# ndarray class transpose() method:
# ---------------------------------------------------
help(np.ndarray.transpose)
# a.transpose(*axes)
#     Returns a view of the array with axes transposed.
# Ex:
a = np.arange(24).reshape(2,3,4)
b = a.transpose()
b.shape #(4, 3, 2)
b = a.transpose((2,0,1))
b.shape #(4, 2, 3)
a.shape #(2, 3, 4)
b = a.T
b.shape #(4, 3, 2)

# 7).swapaxes():
# --------------------
# input:(2,3,4)
# output:(4,3,2)/(3,2,4)/(2,4,3)/(3,4,2) etc........

# By transpose() function, we can interchange any number of dimensions.
# But if we want to interchange only two dimensions then we should go for swapaxes.

# swapaxes(a, axis1, axis2)
#     Interchange two axes of an array.

# a = (2,3,4)
# np.swapaxes(a,0,2)--->(4,3,2)
# np.swapaxes(a,1,2)--->(2,4,3)

a = np.arange(24).reshape(2,3,4)
a
b = np.swapaxes(a,0,2)
b.shape #(4, 3, 2)
b = np.swapaxes(a,1,2)
b.shape #(2, 4, 3)

# Q.Difference between transpose() and swapaxes()?
# -------------------------------------------------------------------------
# By using transpose() we can interchange any number of dimensions.
# But by using swapaxes() we can interchabge only two dimensions.

# Joining of multiple ndarrays into a single array:
# ------------------------------------------------------------------------
# It is something like join queries in Oracle.

# 1.cocatenate()
# 2.stack()
# 3.vstack()
# 4.hstack()
# 5.dstack()

# Joining of multiple ndarrays into a single array by using concatenate():
# ---------------------------------------------------------------------------------------------------------
# >>> help(np.concatenate)
# 	concatenate(...)
#     concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
#     Join a sequence of arrays along an existing axis.

# 2-D array + 2-D array
# axis=0(default):vertical concatination will happens
# axis=1: Horizontal concatenation will happens
# axis=None
# These 2-D arrays will be flatten to 1-D array and then concatenation will be happened.

# Ex:
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.concatenate((a,b))
np.concatenate((a,b),axis=0)
np.concatenate((a,b),axis=1)
np.concatenate((a,b),axis=None)

# Rules:
# ----------
# 1.We can join any number of arrays, but all arrays should be same dimension.
# 2.The sizes of all axes, except concatenation axes must be matched.
# 			(2,3)
# 			(5,3)
# 3.The result of concatenation and output have same shape.

# Ex:Concatenation of two 1-D arrays:
# ------------------------------------------------------
a = np.arange(4)
b = np.arange(5)
np.concatenate((a,b))#array([0, 1, 2, 3, 0, 1, 2, 3, 4])

# Concatenate of three 1-D arrays:
# -------------------------------------------------
c = np.arange(3)
np.concatenate((a,b,c)) #array([0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2])

# Storing result out parameter
# -------------------------------------------
a #array([0, 1, 2, 3])
b #array([0, 1, 2, 3, 4])
c #array([0, 1, 2])
d = np.zeros(12,dtype=int)
d #array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.concatenate((a,b,c),out=d)
d #array([0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2])

d = np.empty(12,dtype=int)
d
np.concatenate((a,b,c),out=d)
d
d = np.empty(10,dtype=int)
np.concatenate((a,b,c),out=d)#ValueError: Output array is the wrong shape

# Using dtype parameter:
# -----------------------------------
np.concatenate((a,b),dtype='float')
array([0., 1., 2., 3., 0., 1., 2., 3., 4.])
np.concatenate((a,b),dtype='str')
array(['0', '1', '2', '3', '0', '1', '2', '3', '4'], dtype='<U11')

# Note:
# 	We cannot use dtype and out simultaneously, because out array has its own dtype.

c = np.empty(9)
np.concatenate((a,b),out=c,dtype='int')
# TypeError: concatenate() only takes `out` or `dtype` as an argument, but both were provided.

# Q.Is it possible to join 1-D array and 2-D array?
# Not possible. To use concatenate function, compulsory all input arrays must have same dimension.

a = np.arange(5)
b = np.arange(12).reshape(3,4)
np.concatenate(a,b)
# TypeError: only integer scalar arrays can be converted to a scalar index

# Joining of 2-D arrays:
# ---------------------------
# For 2-D array the exisiting axes are:
#     axis - 0 ==> Represents the number of rows
#     axis - 1 ==> Represents the number of columns

# * We can perform concatenation based on either axis - 0 or axis - 1.
# * The size of all dimensions(axes) must be matched except concatenation axis.
# * If we are not specifying axis the default value is 0. If axis is None, then arrays will be flattened to 1-D array and then concatenation will be happened.

# Ex-1:
# --------
a = np.array([[10,20],[30,40],[50,60]])
a
b = np.array([[70,80],[90,100]])
b
np.concatenate((a,b))
np.concatenate((a,b),axis=1)#Not Possible
np.concatenate((a,b),axis=None)

# Ex-2:
# --------
a = np.arange(6).reshape(3,2)
a
b = np.arange(9).reshape(3,3)
b
np.concatenate((a,b),axis=0)#Not possible
np.concatenate((a,b),axis=1)
np.concatenate((a,b),axis=None)

# Concatenation of 3-D arrays:
# -------------------------------------------
# (x,y,z)
# axis-0-->The number of 2-D arrays
# axis-1-->The number of rows in every 2-D array
# axis-2-->The number of columns in every 2-D array

# Ex-1:
# --------
a = (2,2,2)
b = (2,2,2)

a = np.arange(8).reshape(2,2,2)
b = np.arange(8).reshape(2,2,2)
a
b
np.concatenate((a,b),axis=0)
np.concatenate((a,b),axis=1)
np.concatenate((a,b),axis=2)

# Ex-2:
# -------
a = (2,3,2)
b = (2,3,3)

# axis-0-->no
# axis-1-->no
# axis-2-->yes

a = np.arange(12).reshape(2,3,2)
b = np.arange(18).reshape(2,3,3)
a
b
np.concatenate((a,b),axis=0)#Not possible
np.concatenate((a,b),axis=1)#Not possible
np.concatenate((a,b),axis=2)

# Q.
# a:(2,3,3)
# b:(1,3,3)
# axis-0 only possible

# Q.(3,2,3) and (2,1,3)
# not possible to perform concatenation on any axis
# But axis=None is possible


# Joining of multiple arrays by using stack() function:
# -----------------------------------------------------------------------------
# 1-D + 1-D ---> 2-D
# 2-D + 2-D ---> 3-D

# Rules:
# 	The input arrays must have same shape
# 	The resultant stacked array has one more dimension than the input array.
# 	Joining will be happended along new axis of newly created array.

# For stacking of 1-D array:
# --------------------------------------
# Ex-1:
# --------
a = np.array([10,20,30])
b = np.array([40,50,60,70])
np.stack((a,b))

# Ex-2:
# --------
a = np.array([10,20,30])
b = np.array([40,50,60])
np.stack((a,b))
array([[10, 20, 30],
       [40, 50, 60]])
np.stack((a,b),axis=1)
array([[10, 40],
       [20, 50],
       [30, 60]])

# Ex:Stacking of 2-D array
# ------------------------------------
# The resultant array will be:3-D array
# 3-D array shape:(x,y,z)

a = np.array([[1,2,3],[4,5,6]])
a
b = np.array([[7,8,9],[10,11,12]])
b
np.stack((a,b),axis=0)
np.stack((a,b),axis=1)
np.stack((a,b),axis=2)

# Ex:
a = np.arange(1,7).reshape(3,2)
b = np.arange(7,13).reshape(3,2)
c = np.arange(13,19).reshape(3,2)
a
b
c
np.stack((a,b,c),axis=0)
np.stack((a,b,c),axis=1)
np.stack((a,b,c),axis=2)

# Stacking three 1-D array
# -------------------------------------
a = np.arange(4)
b = np.arange(4,8)
c = np.arange(8,12)
a
b
c
np.stack((a,b,c),axis=0)
np.stack((a,b,c),axis=1)

# Q.What is the difference between concatenate() and stack()?

# Joining of arrays by using vstack() function:
# ------------------------------------------------------------------
# vstack-->vertical stack-->joining is always based on axis-0
# For 1-D arrays ---> 2-D arrays is output
# For the remaining dimensions it acts as concatenating along with axis-0
# The result of vstack() function should be atleast 2-D.
# For 1-D array the size must be same.

# Ex-1
# -------
a = np.array([10,20,30,40])
b = np.array([50,60,70,80])
np.vstack((a,b))

# Ex:-2:
# ---------
a = np.arange(1,10).reshape(3,3)
a
b = np.arange(10,16).reshape(2,3)
b
np.vstack((a,b))

# Ex-3:
# -------
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,16).reshape(3,2)
np.vstack((a,b))#Not possible

# Ex-4:For 3-D array
# ---------------------------
# axis-0 means the number of 2-D arrays

a = np.arange(1,25).reshape(2,3,4)
b = np.arange(25,49).reshape(2,3,4)
np.vstack((a,b))

# Joining of arrays by using hstack() function:
# ------------------------------------------------------------------
# Exactly same as concatenate() but joining is always based on axis-1
# hstack--->horizontal stack--->column wise
# 1-D + 1-D -->1-D

# Ex:For 1-D array:
# --------------------------
a = np.array([10,20,30])
b = np.array([40,50,60,70])
np.hstack((a,b))

# Ex-2:For 2-D array
# ----------------------------
a = np.arange(1,7).reshape(3,2)
b = np.arange(7,16).reshape(3,3)
np.hstack((a,b))

# Ex:
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,16).reshape(3,3)
np.hstack((a,b))#Not possible

# Joining of arrays by using dstack() function:
# -------------------------------------------------------------------
# dstcak means ---> depth stack/height stacke based on axis-2
# 1-D and 2-D arrays will be converted to 3-D array
# The result is minimum 3-D array.

a = np.array((1,2,3))
b = np.array((2,3,4))
np.dstack((a,b))

# Ex:
a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
np.dstack((a,b))

# Summary of joining of nd-arrays:
# --------------------------------------------------
# 1).concatenate()==>Join a sequence of arrays along an existing axis.
# 2).stack()==>Join a sequence of arrays along a new axis.
# 3).vstack()==>Stack arrays in sequence vertically according too first axis-0
# 4).hstack()==>Stack arrays in sequence horizontally according too second axis-1
# 5).dstack()==>Stack arrays in sequence depth wise according to third axis-2
