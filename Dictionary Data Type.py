'''
DICTIONARY:
* It is a ordered and mutable collection of elements.
* It is denoted by {}.
* It represents the key value pair in the dictionary.
* Insertion order is preserved.
* Hetrogenious objects are allowed.
* Duplicate are not allowed.
* Indexing and slicing are not allowed.
-------------------------------------------------------------------------------------------------------------------------------
* When list and tuple comparison by default datatype is "TUPLE".
* When set and dictionary comparison by default datatype is "DICTIONARY".
-------------------------------------------------------------------------------------------------------------------------------

* We can use list,tuple,and set to represent a group of individual objects as a single entity.
* If we want to represent a group of objects key-value pairs then we should go for dict.

EX :     rollno -------- name
         phone number ----------- address

Note : 
* In c++ and java dict are known as 'Map'.
* Where as in perl and ruby is known as 'Hash'

'''

# Creating a dictionary

d = {}
print(d)

c = dict()
print(c)

a = {100:'laptop' , 200:'Mouse' , 300:'Keyboard'}
print(a[100])
print(a[300])
print(a[1000]) #KeyError
print(a)

# W.A.P to enter name and percentage of marks in a dict and display information on the screen.

rec = {}
n = int(input("Enter the number of students : "))
i = 1
while i <= n:
    name = input("Enter the name of the student : ")
    marks = int(input("Enter % marks: "))
    rec[name] = marks
    i = i + 1

print('Name of the Student','\t','% of Marks')
for x in rec:
    print('\t',x,'\t\t\t',rec[x])

# ----------------FUNCTIONS IN THE DICT --------------------------

'''
1.dict():  To create a dictionary.
2.len():  Returns the number of items in the dict.
3.clear(): To remove all the elements from the dict.
4.get():   To get the value associated with the key.
        d.get(key):
	    If the key is available then returns the corresponding value otherwise returns None. It wont raise any error.
	d.get(key,default value):
	If the key is available then returns the corresponding value otherwise returns default value.
	
5.pop():
	d.pop(key):
		It removes the entry associated with the specified key and returns the corresponding value.
		If the specified key is not available then we will get KeyError.
		
6.popitem():
	It removes an item(key-value) from the dict and return it.
-->If the dict is empty then we will get KeyError.

7.keys():  it returns all keys associated with dict.

8.values(): it returns all values associated with dict.
9.items(): It returns list of tuples represented key-value pairs
		   [(k,v),(k,v),(k,v)]
10).copy(): To create exactly duplicate dict(cloned copy)
11).setdefault(k,v):
	-->If the key is available then this function returns the corresponding value.
	-->If the key is not available then the specified key-value will be added as new item to the dict.
12).update(): d.update(x):
	All items in the dict x will added to dict d.
'''

# 1 Example : 

d1 = dict({100:'sunny',200:'bunny',300:'vinny'})
print(d1)
d2 = dict([(333,'katrina'),(666,'kareena'),(999,'deepika')])
print(d2)
d3 = dict((('l','lilly'),('r','radhika'),('s','sunny')))
print(d3)

# 2 Example :

d1 = dict({100:'sunny',200:'bunny',300:'vinny'})
print(len(d1))

# 3 Example :

d1 = dict({100:'sunny',200:'bunny',300:'vinny'})
print(d1.clear())

# 4 Example :

d1 = dict({100:'sunny',200:'bunny',300:'vinny'})
d = {100:'sunny',200:'bunny',300:'vinny'}
print(d[100])#sunny
print(d[400])#KeyError
print(d.get(100))#sunny
print(d.get(400))#None
print(d.get(100,'pinny'))#sunny
print(d.get(400,'pinny'))#pinny

# 5 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.pop(300))#vinny
print(d.pop(400))#KeyError

# 6 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.popitem())

d = {}
print(d.popitem())#KeyError

# 7 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.keys())
for k in d.keys():
	print(k)

# 8 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.values())
for k in d.values():
	print(k)

# 9 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.items())
for k,v in d.items():
	print(k,'--->',v)

# 10 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
d1 = d.copy()
print(id(d))
print(id(d1))

# 11 Example :

d = {100:'sunny',200:'bunny',300:'vinny'}
print(d.setdefault(100,'pinny'))
print(d.setdefault(400,'pinny'))
# print(d)

# 12 Example :

d = {100:'sunny',200:'bunny'}
d1 = {'a':'apple'}
d.update(d1)
print(d)
d.update([(333,'A')])
print(d)