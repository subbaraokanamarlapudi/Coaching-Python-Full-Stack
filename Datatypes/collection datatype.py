'''
* It is a collection datatype.
* There are : bytes,bytesarray,list,tuple,set,frozenset,range,dict,None.
'''

'''
---> Bytes : 
* It is a immutable datatype.
* It is used to store binary data.
* It is a sequence of integers.
* Once we create bytes data type value.We can't change it values.
* It follows the range of 0 to 256.

x = [10,20,30]
b = bytes(x)
print(b)
print(type(b))

'''

# x = [10,20,30]
# b = bytes(x)
# print(b)
# print(type(b))

# y = [10,20,30,40]
# b = bytes(y)
# b[0] = 100      # Type Error

'''
---> Type casting : 
* It is used to convert one data type to another data type is called Typecasting.
* int() , float() , bool() , complex() , str().
* int() , float() or any integer we cannot convert into the string , but we can convert the string into the integer or float.

'''

a = 10.2
print(type(a))
b = int(a)
print(b)

c = 10
print(type(c))
d = float(c)
print(d)

f = 100.0
print(type(f))
g = str(f)
print(g)

h = '100'
print(type(h))
i = int(h)
print(i)

'''
----> List:

* It is a ordered mutable collection of elements.
* It is denoted by [].
* Insertion order is preserved.
* Hetrogenious objects are allowed.
* Duplicate values are allowed.
* Growable in nature.
* Indexing and slicing supported.

------------------------------------------------or---------------------------------------------------

* It is one datatype.
* It represented by "[]".
* It is a mutable datatype.      "Mutable means changeable datatype."
* It stores different types of elements.
* It allows duplicates elements.
* It allows indexing.

Methods:
* append()
* extend()
* Remove()
* pop()
* count()
* index()

For slicing:
[start:stop:skip] ------> short name as s3

Ex: 
a = [1 , 2.2 , "True" , "Python"]
---------> Positive indexing[0,1,2,3]
Negative indexing<-----------------[-1,-2,-3,-4]

'''

v = []
print(type(v))

v = [1,2.2,1545,True,"python",4,1,5,4,6]
print(v)
print(v[4])
print(v[-3])
print(v[0:4:2])

# v = [1,2.2,3,4,2,1,"True","python","False",5,4,1,2]
# v.append("KVSR")
# v.extend([7,8,9,4,5,6,1,2,300])
# print(v)
# print(v.count(1))
# v.remove(2.2)
# print(v)
# v.pop(3)
# print(v)
# print(v.index("True"))

# v.insert(0,"XYZ")
# print(v)

# for i in [1,2,3,4,4,5,1,34,2113]:
#     print(i)

'''
---> Tuple:

* It is one of the datatype.
* It is represented by "()".
* It allows different types of elements.
* It allows duplicates.
* It allows indexing and slicing.
* It is immutable. -----> Data cannot modify.
* No methods. We can use in-bulit functions.

* In-bult functions are : -----> max,min,sum,zip,len.....

Tuple operations:
* concatentaion.
* Iteration.
* Membership operation.
* Identity operation.
* Repetation. 

'''

c = ()
print(type(c))

c = (1,23,1,3,14,"Triangle")
print(c)
print(c[4])
print(c[-1])
print(c[0:4:2])

# In-bulit
# c = (1,99,100,14,50,75,44,55,60)
# print(min(c))
# print(max(c))
# print(len(c))
# print(sum(c))
# print(zip(c))         # It give the address value.

#operations.

#concatation.
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)

# # repeation
# c = (1,23,1,3,14,"Triangle")
# print(c*2)
# print(c*11)

# Iteration

# t = (1,24,1,3,4,14,15,900)
# for i in t:
#     print(i)

# # membership

# print(1 in t)
# print(11 in t)
# print(14 in t)
# print(24 not in t)

# identity operation
# t1 = (1,2,3)
# t2 = (1,2,3)
# print(t1 and t2)
# print(t1 is t2)

# t1 = (1,2,3)
# t2 = (1,2,4)

# print(t1 is t2)

'''
----> set
* It is also one datatype.
* It  represented by "{}".
* Do not allow the duplicates.
* No index and it is a unordered set.
* Do not allow mutable type as set of elements.

SET METHODS:
* add()
* update()
* pop()
* remove()

SET OPERATIONS:
* union()
* intersection()
* difference()
* issuperset()
* issubset()

'''

s = {1,2,33,789,456,1000}
print(type(s))
print(s)

# s = {2,42,25,66,900}
# s.add(1000)
# s.pop()
# s.remove(42)
# s.update({123,456,908})
# print(s)

# s1 = {1,2,3}
# s2 = {4,5,6}

# print(s1.union(s2))

# s1 = {1,2,3,4,5}
# s2 = {2,3,4,5,6,7}

# print(s1.intersection(s2))

# print(s1.difference(s2))
# print(s2.difference(s1))

# s1 = {1,2,3,4,5,6}
# s2 = {1,2,3}

# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s1))

# for i in (1,2,3,4):
#     print(i)

'''
-----> Dictionary
* It is a datatype.
* It represented by "{}".
* It represents key and values.
* Value should be mutable.
* No slicing.
* keys are unique.

a = {'a':123 , 1:"abc"}

Here,  'a' ----> represents KEY
123 -----> represents values.

Dict methods:
* get()
* update()
* values()
* keys()
* items()
'''

d = {}
print(type(d))

d = {1:'abc' , 22:'KVSR' , "python":1}
print(d)

print(d[22])

#Methods

# d = {1:'abc' , 22:'KVSR' , "python":1}
# print(d.get(1))
# print(d.keys())
# print(d.values())
# print(d.items())

# d = {1:'abc' , 22:'KVSR' , "python":1}
# d.update({1111:2222})
# print(d)

# for i in {1:'abc' , 22:'KVSR' , "python":1}:
#     print(i)

# for i in {1:'abc' , 22:'KVSR' , "python":1}.values():
#     print(i)

# for i,j in {1:'abc' , 22:'KVSR' , "python":1}.items():
#     print(i,j)

# for i in {1:'abc' , 22:'KVSR' , "python":1}.keys():
#     print(i)

'''
----> Range 

* It is a datatype.
* It is a immutable datatype.
* It is a function and sequence of number , starting from 0 by default, and
 increments by 1(by default) and stops before a specified number.
* It is represented by range().

syntax: 
range(start,stop,step)

'''

r = range(10)
print(r)
print(type(r))

for i in r:
    print(i)

r = range(1,10,2)
print(r)
print(type(r))

for i in r:
    print(i)