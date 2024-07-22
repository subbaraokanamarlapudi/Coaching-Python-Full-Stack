# Fundamental datatypes.

#  integer,float,complex,boolean,string

'''
---> Integer :

* It is a bulit-in data type.
* A whole number that can be positive,negative,zero.

Example : 
* -5,1,5,8,9,99
'''

a = 10
print(type(a))
print(a)

'''
---> Float :

* It is a bulit-in data type.
* It used to store positive and negative numbers with a decimal point. 
The float data type has two keywords: Type. Size. Range.

Example:
* 1.0,1.5,1.9,2.0,2.5,2.9,3.0
* 35.3, -2.34, or 3597.34987.

'''

b = 10.5
print(type(b))
print(b)

'''
---> String :

* It is a bulit-in data type.
* It stores a sequence of elements,typically characters,using some character encoding.
* It a sequence of characters and contain letters,numbers,symbols and even spaces.
* It can be represent by single quote and double quote.

Example : 
* "Hello" , 'sunny' , "Laptop".

'''

c = "Hello"
print(type(c))
print(c)

d = 'laptop'
print(type(d))
print(d)


'''
* String : It is a collection of characters.

* Types of declaring strings:
1. single quote ('')
2. Double quote ("")
3. Triple quote (''' ''')

Methods:

* lower()
* upper()
* endswith()
* startswith()
* replace()
* split()
* strip()
* lstrip()
* rstrip()
* count()
* removeprefix()
* remove suffix()
* find()
* index()

'''

# Declaring strings
a = 'college'
b = "university"
c = '''Home town'''

print(type(a) , type(b) , type(c))

# # K = "hi every one"
# K = "HI EVERY ONE"
# # print(K.upper())
# print(K.lower())

# v = "vijay"
# print(v.endswith('y'))
# print(v.endswith('i'))
# print(v.startswith('v'))
# print(v.startswith('j'))

# s = "vijay"
# print(s.replace("vijay" , "Thalapathy"))

# R = "Thalapathy"
# print(R.index("Thala"))
# print(R.find("Thala"))

# R = "Thalapathy vijay"
# print(R.count('j'))
# print(R.removeprefix('Thalapathy'))
# print(R.removesuffix('vijay'))

# R = "KVSR"
# print(R.split())

# R = "   KVSR"
# # print(R)
# # print(len(R))
# # print(R.strip())
# # print(R.lstrip())

# L = R.strip()
# print(L)

# L = R.lstrip()
# print(L)

# L = R.rstrip()
# print(L)



'''
---> Boolean :

* It is a bulit-in data type.
* It is a data type that can only have two values: True or False.
* It is used to represent the truth value of an expression logic and boolean algebra.

Example :
* True , False

'''

e = True
print(type(e))
print(e)

f = False
print(type(f))
print(f)

'''
---> complex:

* It is bulit in data type.
* It consits of 2 values : first value is "real part" , another value is "imaginary part".

Example:

* 3+4j , 10+2j , 4-3j---------------etc.
'''

g = 3+4j
print(type(g))
print(g)

h = 10-2j
print(type(h))
print(h)