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