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

1. CREATION OF LIST : 
---------------------
a = []
print(type(a))
print(a)

2. ACCESSING THE ELEMENTS IN THE LIST:
---------------------------------------

a = [1,2,3,4,5]
print(a[0])
print(a[1])
print(a[-1])
print(a[100])
print(type(a))

3.  DYNAMIC INPUT : 
-------------------
a = eval(input("Enter the list: "))
print(a)
print(type(a))

4. RANGE WITH LIST : 
--------------------
a = list(range(1,11))
print(a)
print(type(a))

5. SPLIT() FUNCTION : 
---------------------
a = "Hello World"
b = a.split()
print(b)
print(type(b))

NOTE : Sometimes we can create list inside another list , such type of list called as nested list.
EXAMPLE : l=[10,20,30,40,[50,60]]
'''

'''
--------------------------------------------------------------------ACCESSING ELEMENTS OF LIST--------------------------------------------------------------
1.BY USING INDEX : 
-------------------
* List follows zero based index i.e index of first element is zero
* list supports both positive and negative indexing.
'''
# Example : 

# l = [10,20,30,40]
# print(l[0])
# print(l[1])
# print(l[-1])
# print(l[100])

'''
2. BY USING SLICE OPERATOR :
----------------------------
* We can access multiple elements of list by using slice operator.
* Syntax : list[start:stop:step]
* start : It is optional. Default value is 0.
* stop : It is mandatory. We have to specify the index from where we have to stop.
* step : It is optional. Default value is 1.
'''
# Example :

# l = [10,20,30,40,50,60,70,80,90]
# print(l[2:7:2])
# print(l[4:2])
# print(l[3:7])
# print(l[8:2:-1])
# print(l[4:100])

# Mutability : Once we create a list of object,we can modify its content. Hence list objects are mutable.

# Traversing : The sequential access of each element in the list is called as traversal.
# -------------------------------------------------------------------------------------------------------------------
# BY USING THE WHILE LOOP : 

# n = [0,1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i<len(n):
#     print(n[i])
#     i += 1

#---------------------------------------------------------------------------------------------------------------------

# 2 BY USING FOR-LOOP: 

# n = [1,2,3,4,5,6,7,8,9,10]
# for i in n:
#     print(i)

# l = ['A','B','C']
# n = len(l)
# for i in range(n):
#     print(l[i],'is available at positive index: ',i, 'and negative index: ',i-n)


'''
---------------------------------------------------------------------------FUNCTIONS------------------------------------------------------------------------

1. len() : Returns no.of elements present in the list.
2. count() : It returns the no.of occurance of specified item in the list.
3. index() : It returns index of the first occurance of the specified element.
4. append() : To add item at the end of the list.
5. insert() : To insert an item at specified index position.

NOTE : 
* If the specified index is greater than max index then element will be inserted at last position.
* If the specified index is smaller than min index then element will be inserted at first position.

***** Difference between append() and insert()? ***********
* append() : It adds item at the end of the list. That will be the last element.
* insert() : It adds item at specified index position. That will be the first element.

6. extend() : To add all elements of one list to another list.
7. remove() : To remove specified item from the list. If the item present multiple times
              then only first occurance will be removed.
8. pop() : It removes and returns the last element of the list.
           If the list is empty then pop() function raises the indexError.

Note : 
* In general we can use append() and pop() function to implement stack data structure by using list , which follows LIFO[Last In First Out]
* n.pop(Index)===> To remove and return element present at specified index.
* n.pop()====> To remove and return last element of the list.

********** Difference between remove() and pop() ? ************************

POP : 
----
* To remove specified element from the list.
* It can't return any value.
* If the specified element not available we will get valueError.

REMOVE :
---------
* To remove last element from the list.
* It returned removed element
* If list is empty then we will get an error:IndexError

Note : 

* List objects dynamic, i.e based on our requirement we can increase and decrease the size.
* append(),insert(),extend()==>For increasing size/growable nature
* remove(),pop()==.For decreasing size/shrinking nature.
'''

# 1. len() : 

# n = [1,2,4,5,7,8,'sun','pen']
# print(len(n))

# 2. count() : 

# n = ['laptop' , 'python' , 100 , 10000 , True , 'laptop']
# print(n.count('laptop'))
# print(n.count(100))

# 3.index() : 

# n = ['laptop' , 'python' , 100 , 10000 , True , 'laptop']
# print(n.index('laptop'))
# print(n.index(100))

# 4.append() : 

# n = [10,20,30]
# n.append(50)
# n.append(100)
# print(n)

# To add all elements upto 100 which are divisible by 10.

# l = []
# for i in range(101):
#     if i%10 == 0:
#         l.append(i)
# print(l)

# 5.insert() : 

# n = [1,2,3,4]
# n.insert(1,100)
# n.insert(-100 , 111)
# n.insert(-10 , 111)
# print('n=',n)

# 6. extend() : 

# order1 = ['Chicken','Mutton','Fish']
# order2 = ['RC','KF','Boom Boom']
# order1.extend(order2)
# print(order1)

# Ex:
# order1 = ['Chicken','Mutton','Fish']
# order1.extend('Prawns')
# print(order1)

# 7. remove() :

# n = [10,20,30,10,20,10,20]
# n.remove(10)
# print(n)

# n = [10,20,30,10,20,10,20]
# n.remove(50)#ValueError: list.remove(x): x not in list

# l = [10,20,30,10,20]
# x = eval(input("Enter element to be removed: "))
# if x in l:
#     l.remove(x)
#     print("Removed successfully")
# else:
#     print("Element not found")

# 8. pop() : 

# l = [10,20,30,40]
# print(l.pop())#40
# print(l.pop())#30
# print(l)#[10,20]

# n = []
# print(n.pop())  # IndexError

# n = [10,20,1,2,30,40]
# print(n.pop())#40
# print(n.pop(1))#20
# print(n.pop(10))#IndexError: pop index out of range

# ------------------------------------------Ordering elements of the list ---------------------------------------------

# 1. reverse() : 
# ---------------
# n = [20,10,40,30]
# n.reverse()
# print(n)

# 2. sort() :
# ------------

'''
* For numbers ===> default sorting order is ascending order.
* For strings ===> default order is alphabatocal order.
'''

# Ex
# n = [20,10,40,30]
# n.sort()
# print(n)#[10,20,30,40]

# n = ['sunny','lilly','radhika']
# n.sort()
# print(n)#['lilly', 'radhika', 'sunny']

# n = [10,'A',20,'B']
# n.sort()  #'<' not supported between instances of 'str' and 'int'

# Descending order : 
# ------------------

# n = [10,40,30,20]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)
# n.sort(reverse=False)
# print(n)

'''
Aliasing and cloning of list objects:
-----------------------------------------------------
-->The process of giving another reference variable to the existing list is called as aliasing.
-->The problem in this approach is by using one reference variable if we are changing content, then those changes will be reflected to the other reference variable.
-->To overcome this problem we should go for cloning.
-->The process of creating exactly duplicate independent object is called as cloning.
-->We can implement cloning by using slice operator or by using copy() function.

1).By using slice operator					
2).By using copy() function

'='---> This is meant for the alising                   'copy'--------> It is meant fot the cloning.

************************************ Difference between shallow copy and deep copy **********************************
'''

# x = [10,20,30,40]
# y = x #Aliasing
# y[1] = 333
# print('x:',x)#[10,333,30,40]
# print('y:',y)#[10,333,30,40]

# By using slice operator : 

# x = [10,20,30,40]
# y = x
# y[1] = 333
# print('x:',x)
# print('y:',y)

# By using copy operator.

# x = [10,20,30,40]
# y = x.copy()
# y[1] = 333
# print('x:',x)
# print('y:',y)

'''
Difference between shallow cloning and deep cloning.
-----------------------------------------------------

1.SHALLOE CLONING : 
-------------------
* It creates a new object,but inserts references into the objects found in the original.
* The new object is a different instance, any nested objects within it are still references to the same objects found in the original.
* Changes to nested objects affect both the original and the copy.

EX : 

import copy

original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)

print("Original:", original)
print("Shallow Copy:", shallow_copy)

shallow_copy[2][0] = 99
print("After modifying the nested list:")
print("Original:", original)
print("Shallow Copy:", shallow_copy)

2. DEEP CLONING :
-----------------
* It creates a new objects and recursively copies all objects found in the original.
* All nested objects are duplicated as well, resulting in a completely independent copy.
* Changes to nested objects do not affect the original and vice versa

EX : 

import copy

original = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original)

print("Original:", original)
print("Deep Copy:", deep_copy)

deep_copy[2][0] = 99
print("After modifying the nested list:")
print("Original:", original)
print("Deep Copy:", deep_copy)

'''

# Shallow copy

# import copy

# original = [1, 2, [3, 4]]
# shallow_copy = copy.copy(original)

# print("Original:", original)
# print("Shallow Copy:", shallow_copy)

# shallow_copy[2][0] = 99
# print("After modifying the nested list:")
# print("Original:", original)
# print("Shallow Copy:", shallow_copy)


# Deep copy

# import copy

# original = [1, 2, [3, 4]]
# deep_copy = copy.deepcopy(original)

# print("Original:", original)
# print("Deep Copy:", deep_copy)

# deep_copy[2][0] = 99
# print("After modifying the nested list:")
# print("Original:", original)
# print("Deep Copy:", deep_copy)


# using mathematical operators for list.

# 1. Concatentation : ----> We can use + to concatenate 2 list into a single list.

# a = [10,20,30]
# b = [40,50,60]
# c = a + b
# print(c)

# Ex : 

# a = [10,20,30]
# b = [40,50,60]
# c = a.extend(b)

# print('a',a)
# print('b',b)
# print('c',c)

# Note: To use + operator both args should be list objects, otherwise we will get an error.

# 2. Repetition : ----> We can use * operator to repeat elements of the list.

# x = [10,20,30]
# y = x * 3
# print(y)

# Comparing list objects:
# ----------------------------------

# Ex:
x = [50,40,30]
y = [10,20,30,40,50,60]
print(x < y)#False
print(x > y)#True

# Membership operators:
# 	-->in
# 	-->not in

# Nested Lists:
# -------------------
# * Sometimes we can take one list inside another list. Such type of lists are called as nested list.

# n = [10,20,30,[40,50]]
# print(n)
# print(n[0])
# print(n[1])
# print(n[3][0])
# print(n[3][1])

# Note : We can access nested list elements by using index just like accessing multi dimensional array of elements.

# Nested list as matrix:
# --------------------------------
# 	In python we can represent matrix by using nested list.

n = [[10,20,30],[40,50,60],[70,80,90]]
print(n)
print('Elements by row wise:')
for r in n:
	print(r)
print('Elements by matrix style:')
for i in range(len(n)):#0,1,2
	for j in range(len(n[i])):#0,1,2
		print(n[i][j],end=' ')
	print()