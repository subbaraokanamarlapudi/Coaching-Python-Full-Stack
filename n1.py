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