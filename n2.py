# Splitting of ndarrays:
# ------------------------
# 1.split()
# 2.vsplit()
# 3.hsplit()
# 4.dsplit()
# 5.array_split()

# We will get view but not copies.

# 1.split():
# ------------
# split(ary, indices_or_sections, axis=0)
#     Split an array into multiple sub-arrays as views into `ary`.

# sections:
# 	1.Array will be splitted into sub arrtays of equal size.
# 	2.It returns list of sub arrays.


# Ex-1:To split 1-D array into 3-parts
# ----------------------------------------------------
import numpy as np

a = np.arange(1,10)
a
np.split(a,3) #[array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
sub_arrays = np.split(a,3)
sub_arrays[0] #array([1, 2, 3])
sub_arrays[1] #array([4, 5, 6])
sub_arrays[2] #array([7, 8, 9])
np.split(a,4)
# ValueError: array split does not result in an equal division

# Ex-2:Splitting of 2-D array:
# ----------------------------------------
# Splitting is based on axis-0 bydefault. i.e row wise aplit(vertical split)
# We can also split based on axis-1.column wise split(horixontal split)

# Ex:
a = np.arange(1,25).reshape(6,4)
a
np.split(a,3)
np.split(a,2)
np.split(a,6)
np.split(a,4)#Error


# Splitting based on axis-1:
# --------------------------------------
# axis-1 means column wise splitting (horizontal split)

a = np.arange(1,25).reshape(6,4)
np.split(a,2,axis=1)
np.split(a,4,axis=1)
np.split(a,3,axis=1)#Error

# Splitting based on indices:
# ----------------------------------------
# The sizes of sub arrays need not be equal.

# Ex:
a = np.arange(10,101,10)
a #array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
np.split(a,[3,7]) #[array([10, 20, 30]), array([40, 50, 60, 70]), array([ 80,  90, 100])]
np.split(a,[2,5,7]) #[array([10, 20]), array([30, 40, 50]), array([60, 70]), array([ 80,  90, 100])]

# Split 2-D array based on indices:
# ------------------------------------------------
a = np.arange(1,13).reshape(6,2)
a
np.split(a,[1,3])
np.split(a,[1,3,4])

# Ex:
a = np.arange(1,19).reshape(3,6)
np.split(a,[1,3,5],axis=1)
np.split(a,[2,4,4],axis=1)
np.split(a,[0,2,6],axis=1)
np.split(a,[1,5,3],axis=1)

# Splitting by vsplit():
# -----------------------------
# vsplit means vertical split means row wise split
# split is based on axis-0

# >>> help(np.vsplit)
# vsplit(ary, indices_or_sections)
#     Split an array into multiple sub-arrays vertically (row-wise).

# To use vsplit input array should be atleast 2-D array.
# Ex:
a = np.arange(10)
a #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.vsplit(a,2)#ValueError: vsplit only works on arrays of 2 or more dimensions

# For 2-D array:
# ---------------------
a = np.arange(1,13).reshape(6,2)
a
np.vsplit(a,2)
np.vsplit(a,3)
np.vsplit(a,6)
np.vsplit(a,[1,4])

# Splitting by hsplit():
# ------------------------------
# split horizontally(column wise)

a = np.arange(10)
a
np.hsplit(a,2)
np.hsplit(a,5)
np.hsplit(a,3)#Error

# For 2-D array:
# ---------------------
# Based on axis-1 only
a = np.arange(1,13).reshape(3,4)
a
np.hsplit(a,2)
np.hsplit(a,4)
np.hsplit(a,3)#Error

# hsplit based on indices:
# ------------------------------------
a = np.arange(10,101,10)
a
np.hsplit(a,[2,4,7])
a = np.arange(24).reshape(4,6)
a
np.hsplit(a,[2,4])

# vsplit()--->split based on axis-0(rows)
# hsplit()--->split based on axis-1(column)
# dsplit()-->split based on axis-2--->3-D array

# dsplit(ary, indices_or_sections)
#     Split array into multiple sub-arrays along the 3rd axis (depth).

a = np.arange(24).reshape(2,3,4)
a
np.dsplit(a,2)
np.dsplit(a,[1,3])

# splitting by using array_split():
# ---------------------------------------------
# split() with sections--->should be equal parts, otherwise---->error
# array_split()-->sections need not be have to have equal size.
# 4-->rows-->3 equal parts

# >>> help(np.array_split)
# 		array_split(ary, indices_or_sections, axis=0)
# 			Split an array into multiple sub-arrays.

# For an array of length x that should be split
#     into n sections, it returns x % n sub-arrays of size x//n + 1
#     and the rest of size x//n.

# 10 elements ----> 3 sections
# x = 10
# n = 3
# x % n sub-arrays of size x//n + 1===>1 sub-array of size 4
# rest of size x//n==>2 sub-arrays of size:3

# 4,3,3

a = np.arange(10,101,10)
a #array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
np.array_split(a,3) #[array([10, 20, 30, 40]), array([50, 60, 70]), array([ 80,  90, 100])]

# Ex-2:
# 		11-elements			3-sections
# x = 11
# n = 3
# x % n sub-arrays of size x//n + 1===>2 sub-array of size 4
# rest of size x//n==>1 sub-arrays of size:3
# (4,4,3)

a = np.arange(0,101,10)
a 
np.array_split(a,3)

# Summary of split methods:
# -----------------------------------------
# split():split an array into multiple sub-arrays of equal size.
# vsplit():split an array into multiple sub-arrays vertically(row wise)
# hsplit():split an array into multiple sub-arrays horizontally(column wise)
# dsplit():split an array into multiple sub-arrays along the 3rd axis(depth)
# array_split():split an array into multiple sub-arrays of equal or near-equal size.
# Does not raise an exception if an equal division cannot be made.

# Sorting of ndarrays:
# ------------------------------
np.sort(a)
	# quicksort----->merge sort,heap sort

# The default is 'quicksort'
# For numbers--->Ascending order
# For strings--->ALphabatical order

# Ex-1:1-D array
# ---------------------
a = np.array([20,10,5,40,30,50])
a #array([20, 10,  5, 40, 30, 50])
np.sort(a) #array([ 5, 10, 20, 30, 40, 50])

# To sort in descending order:
# ------------------------------------------
# 1st way:
# ------------
np.sort(a)[::-1]
# array([50, 40, 30, 20, 10,  5])

# 2nd way:
# -------------
a #array([20, 10,  5, 40, 30, 50])
-a #array([-20, -10,  -5, -40, -30, -50])
np.sort(-a) #array([-50, -40, -30, -20, -10,  -5])
-np.sort(-a) #array([50, 40, 30, 20, 10,  5])

# Ex-2:To sort string elements in alphabatical order
# --------------------------------------------------------------------------
a = np.array(['sunny','bunny','vinny','chinny','pinny'])
a
np.sort(a)

# To sert reverse of alphabatical order:
# --------------------------------------------------------
np.sort(a)[::-1]
-np.sort(-a) #Invalid


# for 2-D array:
# --------------------
a = np.array([[40,20,70],[30,20,60],[70,90,80]])
a
np.sort(a)
np.sort(a,axis=0)
np.sort(a,axis=-2)

# Searching elements of ndarray:
# ----------------------------------------------
# where() function

# where(...)
#     where(condition, [x, y], /)

# where() function wont return elements.
# It returns indices where condition is True.

# a = np.array([3,5,7,6,9,4,10,15])

# Ex-1:Find indices where the value is 7
np.where(a==7)
# (array([2], dtype=int64),)

# Ex-2:Find indices where odd numbers present in array
np.where(a%2 != 0)
# (array([0, 1, 2, 4, 7], dtype=int64),)

# To get elements directly:
indices = np.where(a%2 != 0)
a[indices]
# array([ 3,  5,  7,  9, 15])

# condition bsed selection:
a[a%2 != 0]
# array([ 3,  5,  7,  9, 1/5])

# Ex:Find indices where element divisible by 3
b = np.where(a%3==0)
b #(array([0, 3, 4, 7], dtype=int64),)
a[b] #array([ 3,  6,  9, 15])

# where(condition, [x, y]):
# 	This function can perform replace operation also

# If condition satisfied that element will be replaced from x and if the condition False that element will be replaced by y.

# Ex:Replace even numbers with 3113 and odd numbers with 9345.
a #array([ 3,  5,  7,  6,  9,  4, 10, 15])
np.where(a%2==0,3113,9345)

# Ex:Every odd number present in a ,replace with 9999.
np.where(a%2 != 0,9999)
# ValueError: either both or neither of x and y should be given

np.where(a%2 != 0,9999,a)

# Ex:For 2-D array
# ------------------------
a = np.arange(12).reshape(4,3)
a
np.where(a%5==0)
# (array([0, 1, 3], dtype=int64), array([0, 2, 1], dtype=int64))

# The first ndarray represents row indices and second ndarray represents column indices. i.e required elements present at (0,0), (1,2) and (3,1) index places

# If we want to see the elements
# ----------------------------------------------
b = np.where(a%5==0)
a[b] #array([ 0,  5, 10])

# Even we can perform replacement operation also.
np.where(a%5==0,999,a)

# searchsorted() function:
# -----------------------------------
# Internally this function will use Binary search algorithm. Hence we can call this function only for sorted arrays.
# If the array is not sorted we will get abnormal results.

# >>>help(np.searchsorted)
# 	searchsorted(a, v, side='left', sorter=None)
# 		Find indices where elements should be inserted to maintain order.

# Ex-1:
a = np.arange(0,31,5)
a #array([ 0,  5, 10, 15, 20, 25, 30])
np.searchsorted(a,5) #1
np.searchsorted(a,13) #3

# Note:
# 	Bydefault it will always search from left hand side to identify insertion point. If we want to search from right hand side we should use side = 'right'

a = np.array([3,5,7,6,7,9,4,10,15,6])
a = np.sort(a)
a
np.searchsorted(a,6) #3
np.searchsorted(a,6,side='right') #5

# Summary:
# ---------------
# 1.sort():To sort given array
# 2.where():To perform search and replace operation
# 3.searchsorted():To identify insertion point in the given sorted array.

# How to insert elements into ndarray?
# --------------------------------------------------------
# 1.insert()
# 2.append()

# 1.insert():
# --------------
# insert(arr, obj, values, axis=None)
#     Insert values along the given axis before the given indices.

# obj-->object that defines index or indices before which the value will be inserted.

# Inserting into 1-D array:
# ------------------------------------
a = np.arange(10)
a #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.insert(a,2,999)
b
a

# Ex:Insert 333 before index 2 and 5.
b = np.insert(a,[2,5],999)
b

# Ex:To insert 333 before index 2 and 999 before index 5?
b = np.insert(a,[2,5],[333,999])
b

b = np.insert(a,[2,5],[333,666,999])#Error
b = np.insert(a,[2,5,7],[333,666])#Error
b = np.insert(a,[2,5,5],[111,222,333])
b #array([  0,   1, 111,   2,   3,   4, 222, 333,   5,   6,   7,   8,   9])
b = np.insert(a,25,333) #IndexError

# Note:
# 	Array should contain only homogenious elements. If we are trying to insert any other element, thet element will be converted to array type automatically before insertion. If the conversion not possible then we will get an error.

# Ex:
a #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.insert(a,2,123.456) #array([  0,   1, 123,   2,   3,   4,   5,   6,   7,   8,   9])
np.insert(a,2,True)#array([0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.insert(a,2,'Mahesh')
# ValueError: invalid literal for int() with base 10: 'Mahesh'

# Summary:
# ---------------
# while inserting elements into 1-D array:
# 	1.The number of indices and the number of elements should be matched.
# 	2.Out of range index is not allowed.
# 	3.Elements will be converted automatically to the array type.

# Inserting elements into 2-D array
# -------------------------------------------------
# We should provide axis.
# If we are not providing axis, then default value None, will be considered. Then the array will be flatten to 1-D array and then insertion will be happened.

a = np.array([[10,20],[30,40]])
a
np.insert(a,1,100)
# array([ 10, 100,  20,  30,  40])
np.insert(a,1,100,axis=0)
np.insert(a,1,[100,200],axis=0)
np.insert(a,1,[100,200,300],axis=0) #Error

# Ex:
np.insert(a,1,100,axis=1)
np.insert(a,1,[100,200],axis=1)

# In 2-D array axis-0 means rows(axis:-2)
# In 2-D array axis-1 means columns(axis:-1)

# Ex:
np.insert(a,0,[100,200],axis=-1)

# Appending elements to ndarray by using append():
# ---------------------------------------------------
# insert()--->To insert elements at our required position.
# append()-->To insert elements at last.

# help(np.append)
# 		append(arr, values, axis=None)
# 			Append values to the end of an array.

# Ex-1:
# -------

a = np.arange(10)
a
np.append(a,333)
np.append(a,[10,20,30])

# Note : If we are trying to append hetrogenious elements, then array elements and new element will be converted to some common type and then append will be happend. 


np.append(a,10.5)
np.append(a,'mahesh')
np.append(a,True)
np.append(a,10+3j)

# Appending elements to 2-D array:
# -----------------------------------
a = np.array([[10,20],[30,40]])
a
np.append(a,70) #array([10, 20, 30, 40, 70])
np.append(a,70,axis=0) #Invalid
np.append(a,[70,80],axis=0) #Invalid
np.append(a,[[70,80]],axis=0)
np.append(a,[[70,80],[50,60]],axis=0)


# Ex:
# ----
np.append(a,[[70,80]],axis=1)#Invalid
np.append(a,[[70],[80]],axis=1)
np.append(a,[[70,80],[50,60]],axis=1)
 

# Q.Consider the query?
a = np.arange(12).reshape(4,3)
a

# Which of the following operations will be performed successfully?
# A. np.append(a,[[10,20,30]],axis=0)#Valid
# B. np.append(a,[[10,20,30]],axis=1)#Invalid
# C. np.append(a,[[10],[20],[30]],axis=0)#Invalid
# D. np.append(a,[[10],[20],[30],[40]],axis=1)#Valid
# E. np.append(a,[[10,20,30],[40,50,60]],axis=0)#Valid
# F. np.append(a,[[10,20],[30,40],[50,60],[70,80]],axis=1) #Valid

# Q.What is the difference between insert() and append() function?
# -----------------------------------------------------------------------------------------------
# By using insert() function we can insert element at our required index position.
# By using append() function, we can add elements always at the end of the ndarray.

# Deletion of elements from ndarray:
# ----------------------------------------------------
# delete(arr, obj, axis=None)

# To delete elements of 1-D array
# -----------------------------------------------
a = np.arange(10,101,10)
a #array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
np.delete(a,3) #array([ 10,  20,  30,  50,  60,  70,  80,  90, 100])
np.delete(a,[0,4,6]) #array([ 20,  30,  40,  60,  80,  90, 100])
np.delete(a,np.s_[2:6]) #array([ 10,  20,  70,  80,  90, 100])
np.delete(a,np.s_[:]) #array([], dtype=int32)
np.delete(a,range(2,6)) #array([ 10,  20,  70,  80,  90, 100])


# To delete elements of 2-D array:
# ------------------------------------------------
# We should provide axis. If we are not providing axis, then array will be flatten to 1-D array and then delete will be happened.

# Ex:
a = np.arange(1,13).reshape(3,4)
a
np.delete(a,1)
np.delete(a,1,axis=0)
np.delete(a,[0,2],axis=0)
np.delete(a,np.s_[:2],axis=0)

# Ex:Delete column wise
# -----------------------------------
a
np.delete(a,0,axis=1)
np.delete(a,[0,2],axis=1)
np.delete(a,np.s_[::2],axis=1)
np.delete(a,np.s_[1::3],axis=1)
np.delete(a,np.s_[1:],axis=1)

# Delete elements from 3-D array:
# ------------------------------------------------
a = np.arange(24).reshape(2,3,4)
a
# axis-0--->index of 2-D array
# axis-1-->Rows in every 2-D array
# axis-2-->COlumns in every 2-D array

# Ex:
np.delete(a,3)#flatten to 1-D array and delete 3rd index element
np.delete(a,0,axis=0)#1st 2-D array deleted
np.delete(a,1,axis=0)#2nd 2-D array deleted
np.delete(a,1,axis=1)#To delete 1st indexed row in every 2-D array
np.delete(a,2,axis=2)#To delete 2nd indexed column in every 2-D array
np.delete(a,[0,2],axis=2)
np.delete(a,np.s_[1:],axis=2)

# Case study:
# ----------------
a = np.arange(12).reshape(4,3)
a

# Replace last row with the following row:[70,80,90]
# 		delete last row and insert the required row

b = np.delete(a,3,axis=0)
b
np.append(b,[[70,80,90]],axis=0)
