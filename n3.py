# ndarrays: a and b
import numpy as np
a = np.array([[10,20],[30,40]])
b = np.array([[1,2],[3,4]])
a
b
a*b


# If we want matrix multiplication then we should go for dot() function

np.dot(a,b)

# A.B ===>a.dot(b)

# -------------------------------------------------------------- Importance of matrix class in numpy library --------------------------------------------

# 1-D array is caled ---> Vector
# 2-D array is called --> Matrix

# Matrix class is specially designed class to create 2-D arrays.
# How to creare 2-D array:
# 	1.By using ndarray
# 	2.By using matrix class

# >>>help(np.matrix):
# 	class matrix(ndarray)
# 	  matrix(data, dtype=None, copy=True)	

# Creating matrix object from string:
a = np.matrix('col1 col2 col3;col1 col2 col3')
a = np.matrix('col1,col2,col3;col1,col2,col3')

# Ex:
a = np.matrix('10,20;30,40')
type(a) #<class 'numpy.matrix'>
a
b = np.matrix('10 20;30 40')
type(b) #<class 'numpy.matrix'>
b

# Creating matrix object from nested list
a = np.matrix([[10,20],[30,40]])
a

# Create a matrix from ndarray
a = np.arange(6).reshape(3,2)
type(a) #<class 'numpy.ndarray'>
b = np.matrix(a)
type(b) #<class 'numpy.matrix'>

# + operator in ndarray and matrix:
# 	The behaviour is the same for both.
# Ex:
a = np.array([[1,2],[3,4]])
m = np.matrix([[1,2,],[3,4]])
a+a
m+m

# * operator in ndarray and matrix:
# 	-->In case of ndarray * operator performs element level multiplication
# 	-->In case of matrix * operator performs matrix multiplication

a = np.array([[1,2],[3,4]])
m = np.matrix([[1,2,],[3,4]])
a*a
m*m

# ** operator in ndarray and matrix:
# 	-->In case of ndaaray ** operator performs power operation at element level.
# 	-->In case of matrix ** operator performs power operation at matrix level
# 							m**2 ==> m * m
# Ex:
a
 
a**2
m
m**2
 

# T in ndarray and matrix:
# 	T behaves same way in both.


a
a.T
m
m.T

# Note:It is no longer recommended to use this class, even for linear algebra. 
# 		Instead use regular arrays. The class may be removed in the future.

# Differences between ndarray and matrix?
# -------------------------------------------------------------
# 			ndarray												matrix
# 			-----------										   -----------
# 1.It can represent any n-dimension array.		1.It can represent only 2-D array.

# 2.We can create from any array_like object		2.We can create from either array_like
# but not from the string.									object or from string.

# 3.* operator meant for element multiplication3.* operator for dot product not for
# but not for dot product									element multiplication.

# 4.** meant for element level power operation.	4.** meant for matrix power operation.

# 5.It is the parent class.									5.It is the child class.

# 6.It is the recommended to use						6.It is not recommended to use and it 
# 																	is depricated.

# Chapter-18:Linear Algebra functions from linalg module
# ------------------------------------------------------------------------------------
# numpy.linlag ---> To perform linear algebra operations.

# 1.inv() ---> To inverse() of a matrix.
# 2.matrix_power() ---> To find power of matrix line A power(n).
# 3.det() -->To find determinant of matrix.
# 4.solve() ---> To solve linear algebra equations.

# 1.inv():To find inverse of a matrix
# --------------------------------------------------
help(np.linalg.inv)

# inv(a)
#     Compute the (multiplicative) inverse of a matrix.

#     Given a square matrix 'a', return the matrix 'ainv' satisfying
#     dot(a, ainv) = dot(ainv, a) = eye(a.shape[0]).

a = np.array([[1,2],[3,4]])
a

ainv = np.linalg.inv(a)
ainv

# How to check:
# ---------------------
i = np.eye(2)
i

np.dot(a,ainv)
np.allclose(i,np.dot(a,ainv))
True

# allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
#     Returns True if two arrays are element-wise equal within a tolerance.

# Note:
# 	We can find inverse only for square matrices, otherwise we will get an error.
# Ex:
a = np.array([[10,20,30],[40,50,60]])
a
np.linalg.inv(a) #Last 2 dimensions of the array must be square

# How to find inverse of 3-D array:
# -------------------------------------------------
# 3-D arrays contains collection of 2-D arrays.
# Finding inverse of 3-D array means, finding inverse for every 2-D array.

a = np.arange(8).reshape(2,2,2)
a
np.linalg.inv(a)


# 2.matrix_power():To find power of a matrix line a power(n)
# ---------------------------------------------------------------------------------------
# >>> help(np.linalg.matrix_power)
# 	matrix_power(a, n)
# 		Raise a square matrix to the (integer) power 'n'.

# if n == 0 ==>Identity Matrix
# if n > 0 ==>normal power operation
# if n < 0 ==>First inverse and then power operation for absolute value

# Ex:
a = np.array([[1,2],[3,4]])
a
np.linalg.matrix_power(a,0)
np.linalg.matrix_power(a,2)
np.linalg.matrix_power(a,-2)
np.dot(np.linalg.inv(a),np.linalg.inv(a))
np.linalg.matrix_power(np.linalg.inv(a),2)

# Note:We can find matix_power only for a square matrix, otherwise we will get error.

# 3.det():To find determinant of a matrix
# ---------------------------------------------
# help(np.linalg.det)
# print(help(np.linalg.det))

a = np.array([[1,2],[3,4]])
a

# For 3x3 matrix:
# ------------------

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.arange(9).reshape(3,3)
a
np.linalg.det(a)

# Note: We can find determinant only for square matrix.

# 4.solve():To solve linear algebra equations
# -----------------------------------------------
# help(np.linalg.solve)
# print(help(np.linalg.solve))

'''
case study:
-------------
Boys + Girls = 2200
Boys = 3$   ,   Girls = 8$
Total Fees  = 10100$

x + y = 2200   ------> x = 2200 - y
3x + 8y = 10100

3(2200-y) + 8y = 10100
6600 - 3y + 8y = 10100
5y = 10100 - 6600
5y = 3500
y = 3500/5
y = 700

x = 2200 - 700
x = 1500


'''

a = np.array([[1,1],[3,8]])
a
b = np.array([2200,10100])
b
np.linalg.solve(a,b)

# Note:We can solve linear algebra equations only for square matrix, otherwise we will get an error.

# Ex: 
a = np.array([-4,7,-2],[1,-2,1],[2,-3,1])
a
b = np.array([2,3,-4])
b
np.linalg.solve(a,b)

# ----------------------------------------- I/O Operations with numpy ----------------------------------------------------------------

# We can save/write ndarray objects to a binary file for further purpose.Later point of time,whenever these objects are required, we can read from that binary file.

# save() ----> To save/write ndarray object to a file.
# load() ----> To read ndarray object from a file.

print(help(np.save()))
print(help(np.load()))

# EX - 1: Saving ndarray object to a file and read back
# ------------------------------------------------------------

import numpy as np
a = np.array([10,20,30],[40,50,60])

# save/serialize ndarray object to a file
np.save('out.npy',a)

# load ndarray objectt from a file
out_array = np.load('out.npy')
print(out_array)

# Note : 
# 1. The data will be stored in binary format.
# 2. File extension should be .npy, otherwise save() function itself will add that file extension.
# 3. By using save() function we can write only one object to the file. If we want to write multiple objects to a file then we should go for save() function. 

# Saving multiple ndarray objects to the binary file:
# --------------------------------------------------------------

import numpy as np
a = np.array([10,20,30],[40,50,60])
b = np.array([70,80],[90,100])

np.savez('out.npz',a,b)

npzfileobj = np.load('out.npz')  # returns NpzFile object

print(type(npzfileobj))
print(npzfileobj.files)
print(npzfileobj['arr_0'])
print(npzfileobj['arr_1'])

# Note: 
# 1. np.save() ---> save an array to a binary file in .npy format.
# 2. np.savez() ---> save several arrays into a single file in .npz format but in uncompressed form.
# 3. np.savez.compressed() ---> save several arrays into a single file in .npz format but in compressed form.
# 4. np.load() ---> To load/read ndarray from .npy or .npz file.

# Compressed form:
# --------------------
np.savez_compressed('out_compressed.npz',a,b)

# Analysis:
# ---------
# path of the out_compressed.npz file

# Q : we can save object in compressed form,then what is the need of uncompressed form?

# compressed form ----> Memory will be saved , but performance will be degraded.
# uncompressed form ----> Memory will be wasted, but performance will be increased.

# Save ndarray objects to the file in normal text format:
# --------------------------------------------------------------
# savetxt() and loadtxt()

print(np.savetxt())
print(np.loadtxt())

# Ex:
import numpy as np
a = np.array([10,20,30],[40,50,60])
np.savetxt('out.txt',a)

out_array = np.loadtxt('out.txt')
print(out_array)

print('output array in the format')
out_array2 = np.loadtxt('out.txt',delimiter=',')
print(out_array2)

# Ex:

import numpy as np
a = np.array([['sunny',1000],['rainy',2000],['cloudy',3000]])
np.savetxt('out.txt',a,fmt='%s %d',delimiter=',')

a2 = np.loadtxt('out.txt',delimiter=',')
print(a2)

# Writing ndarray objects to the csv file:
# --------------------------------------------
# csv - comma separated values

import numpy as np
a1 = np.array([10,20,30],[40,50,60])
np.savetxt('out.csv',a1,fmt='%d',delimiter=',')

a2 = np.loadtxt('out.csv',delimiter=',')
print(a2)