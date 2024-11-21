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