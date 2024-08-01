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
'''