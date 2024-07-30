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

