'''
-----------------------------------------------------------------------STRING DATA TYPE ------------------------------------------------------------------------------------------------------
-------> What is a String?
* Any sequence of characters within either single quotes or double quoutes and triple quotes are called as String.
Example:
s = 'laptop'
s = "laptop"
single triple quote --> (''' ''')
double triple quote --> (""" """) 

Note : 
* Most of the other languages like c,c++ and java. A single character within character within a single quotes is treated as char data type value.
* But in python we are not having char data type. It is treated as string only.

'''

# How to access the characters of a string.
'''
1. By using index : 
* Python supports both positive and negative index.
* +ve index means left to right [forward direction]
* -ve index means right to left [backward direction]

s = 'sunny'
		s[0] #s
		s[-1] #y
		s[10] #IndexError
'''
# Basic program

s = 'sunny'
print(s[0])
print(s[-1])
print(s[10])

# 2. W.A.P to accept some string from the keyboard and display its characters by index wise both positive and negative

s = input("Enter a string: ")
i = 0
for x in s:
    print("The character present at +ve index {} and -ve index{} is {}".format(i,i-len(s),x))
    i += 1

# 3. By using slice operator:

s = "learning python is very easy"
print(s[1:7:1])
print(s[1:7])
print(s[:7])
print(s[:])
print(s[::])
print(s[::-1])

'''
1).If step is +ve:									2).If step is -ve:	
------------------------							------------------------		
-->Forward direction(left to right)					-->Backward direction(right to left)
-->Bydefault begin index is:0						-->Bydefault begin index:-1
-->Begin to End-1								    -->Begin to End+1

Note:
--------
-->In the backward direction if end value is -1 then result is always empty.
-->In the forward direction if end value is 0 then result is always empty.

'''

n = '0123456789'
print(n[2:8:1])
print(n[2:8:-1])
print(n[-1:-6:-1])
print(n[2:-5:1])
print(n[-5:0:-1])
print(n[:0:-1])
print(n[2:4:-6])

# Case study

s = 'abcdefghij'
print(s[1:6:2])
print(s[::1])
print(s[::-1])
print(s[::-2])
print(s[3:7:-1])
print(s[7:4:-1])
print(s[0:1000:1])
print(s[0:1000:2])
print(s[-4:1:-1])
print(s[-4:1:-2])
print(s[5:0:1])
# print(s[9:0:0])
print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:-12:-1])
print(s[0:0:1])
# print(s[0:0:0])
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[9:-1:-1])

# W.A.P to access each character of string in forward direction and backward direction by using while loop.

s = input("Enter a String: ")
i = 0
n = len(s)

print("-------Forward Direction---------")
while i<n:
    print(s[i],end='')
    i += 1
print()

print("-------Backward Direction---------")
i = -1
while i>=-n:
    print(s[i],end='')
    i -= 1
print()

print("-------Backward Direction---------")
i = n-1
while i>=0:
    print(s[i],end='')
    i -= 1

# Another Method by using loop.

s = input("Enter a string: ")
print("---------Forward Direction----------")
for i in s:
    print(i,end='')
print()

print("---------Forward Direction------------")
for i in s[::]:
    print(i,end='')
print()

print("---------Backward Direction----------")
for i in s[::-1]:
    print(i,end='')

'''
Checking membership:
----------------------------------
We can check whether the character or string is the member of another string or not by using in and not in operators.    
'''

# Example

s = input('Enter main string:')
subs = input('Enter sub string:')
if subs in s:
	print(subs,'is found in main string')
else:
	print(subs,'is not found in main string')

# Comparison of strings:
# Example:

s1 = input("Enter 1st String: ")
s2 = input("Enter 2nd String: ")

if s1==s2:
    print("Both are same")
elif s1<s2:
    print("First string is less than second string")
else:
    print("First string is greater than second string")

l1 = ['A','B','C']
l2 = ['A','B','C']
l3 = l2
print(l1 is l2)#False
print(l2 is l3)#True
print(l1 == l2)#True

'''
Removing spaces from the string:
--------------------------------------------------
1.rstrip():To remove spaces at right hand side.
2.lstrip():To remove spaces at left hand side.
3.strip():To remove spaces both sides.

'''

city = input('Enter Your City:')
scity = city.strip()
if scity == 'hyderabad':
	print('Hello Hyderabadi....gud mng')
elif scity == 'chennai':
	print('Hello Madrasi....Vanakkam')
elif scity == 'bangalore':
	print('Hello Kannadiga....Subhodaya')
else:
	print('Your enetered city is invalid')

'''
Finding substring:
----------------------------
For forward direction:
	-->find()
	-->index()

For backward direction:
	-->rfind()
	-->rindex()

1.find():
	s.find(substring):
		Returns index of the first occurence of the given substring. If it is not availbale we will get -1.

2.index():
	It is exactly same as find() method except that if the specified substring is not available then we will get ValueError.
    
Note:
	Bydefault find() method can search total string. We can also specify the boundaries to search.

'''

s = "learning python is very easy"
print(s.find('e'))
print(s.index('e'))
print(s.find('z'))
print(s.index('z'))
print(s.rfind('e'))
print(s.rindex('e'))
print(s.rfind('z'))
print(s.rindex('z'))
print(s.find('e'))#1
print(s.find('e',2,15))#-1
print(s.find('e',2,23))#20

# W.A.P to display all the positions of substring in a given string.

s = input("Enter a string: ")
subs = input("Enter a sub string: ")
pos = -1
n = len(s)

while True:
    pos = s.find(subs,pos+1,n)
    if pos == -1:
        break
    print("Found at position: ",pos)
    flag = True

if flag == False:
    print("Not Found")

'''
Counting substring in the given string
---------------------------------------------------------
We can find the number of occurances of substring present in the given string by using count() method.

1).count(substring)==>It will search through out the string.
2).s.count(substring,begin,end)==>It will search from begin index to end-1 index.
'''

s = 'abbbbbbbcbabbbcba'
print(s.count('a'))#3
print(s.count('a',1,8))#0
print(s.count('ab'))#2

'''
Splitting of string:
--------------------------
We can split the given string according to specified separator by using split() method.
Syn:
		l = s.split(separator)
Default separator is space. The return type of split() method is list.
'''

# Ex: 01
s = 'learning python is very easy'
l = s.split()
print(l)
for i in l:
	print(i)

# Ex: 02
s = '27-07-2024'
l = s.split('-')
print(l)
for i in l:
	print(i)

'''
joining of strings:
-------------------------
We can join a group of strings(list or tuple) w.r.t the given separator.
Syn:
		s = separator.join(group of strings)
'''

# Example : 

l = ('sunny' , 'bunny' , 'vinny' , 'cinny')
print('-'.join(l))
print(':'.join(l))

'''
Replacing a string with another string
---------------------------------------------------------
Syn:
		s.replace(oldstring,newstring)
-->Inside s, every occurance of old string will be replaced with new string.

s = 'learning python is difficult'
s1 = s.replace('difficult','easy')
print(s1)

Q.String objects are immutable then how we can change the content by using replace() method?
Once we creates string object, we cant change the content. This non changable behaviour is nothing but immutability. 
If we are trying to change the content by using any method, then with those changes a new object will be created and changes wont be happended in existing object.		
Hence with replace() method also a new object got created but existing object wont be changed.

'''
#  Example : 

s = 'abab'
s1 = s.replace('a','b')
print(s,'is available at:',id(s))
print(s1,'is available at:',id(s1))

# Changing cases in a string.

s = 'learning python is very easy'
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())

# Checking starting and ending part of the string.

s = 'learning python is very easy'
print(s.startswith('learning'))
print(s.endswith('learning'))
print(s.endswith('easy'))

'''
To check type of characters present in a string
----------------------------------------------------------------------
1).isalnum():Returns True if all the characters are alphanumeric(a-z,A-Z,0-9)
2).isalpha():Returns True if all the characters are only alphabate symbols(a-z,A-Z)
3).isdigit():Returns True if all the characters are digits only(0-9)
4).islower():Returns True if all the characters are lower case alphabate symbols.
5).isupper():Returns True if all the characters are upper case alphabet symbols.
6).istitle():Returns True if the string is in title case.
7).isspace():Returns True if string contains only spaces.
'''

print('sunny123'.isalnum())
print('sunny123'.isalpha())
print('sunny'.isalpha())
print('sunny'.isdigit())
print('786'.isdigit())
print('sunny'.islower())
print('sunny123'.islower())
print('SUNNY'.isupper())
print('Learning Python Is Very Easy'.istitle())
print(' '.isspace())

# Example

s = input("Enter any character: ")
if s.isalnum():
    print("It is a alpha numeric character")
    if s.isalpha():
        print("It is a alphabet character")
        if s.islower():
            print("It is a lower case alphabet character")
        else:
            print("It is a upper case alphabet character")
    else:
        print("It is a digit")
elif s.isspace():
    print("It is a space character")
else:
    print("It is a special character")