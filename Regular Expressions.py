'''
Regular Expressions:
----------------------

* If we want represent a group of strings according to a particular then we should go for regular expression.
* i.e regular expression is a declarative mechanism to represent a group of strings according to a pattern.

Ex-1:We can write a regular expression to represent all mobile numbers.
Ex-2:We can write a regular expression to represent all mail id's.

* We can develop regular expression based applications by using python module:re

1.compile():
	To comiple a patternt into RegexObject.
				pattern = re.compile('ab')

2.finditer():
	Returns an iterator object which yields match object for every match.
				matcher = pattern.finditer('abaababa')
	
On match object we can call the methods:
	1.start():Returns start index of the match
	2.end():Returns end+1 index of the match
	3.group():Returns the matched string


'''

# Example : 

import re
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('abaababa')
for match in matcher:
    count += 1

print(match.start(),'......',match.end(),'......',match.group())
print('The number of occurences:',count)

# Note : We can pass pattern directly as argument to finditer() function.

# matcher = re.finditer('aba','abaababa')
# for match in matcher:

# print(match.start(),'......',match.end(),'......',match.group())


# Character Classes:
# ---------------------------
# We can use character classes to search a group of characters.

# 1.[abc]==>Either a or b or c
# 2.[^abc]==>Except a and b and c
# 3.[a-z]==>Any lower case alphabate symbol
# 4.[A-Z]==>Any upper case alphabate symbol
# 5.[0-9]==>Any digit from 0 to 9
# 6.[a-zA-Z]==>Any alphabate symbol
# 7.[a-zA-Z0-9]==>Any alphanumeric character
# 8.[^a-zA-Z0-9]==>Except alphanumeric characters(special characters)

# EX : 1

import re 
matcher = re.finditer('[abc]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())


# EX : 2

import re 
matcher = re.finditer('[^abc]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())

# EX : 3
import re 
matcher = re.finditer('[a-z]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())

# Ex : 4
import re 
matcher = re.finditer('[0-9]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())

# Ex : 5
import re 
matcher = re.finditer('[a-z0-9]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())

# Ex : 6

import re 
matcher = re.finditer('[^a-z0-9]','a7b@k9zc')
for match in matcher:
    print(match.start(),'......',match.group())


# 2).Pre-defined character classes
# -----------------------------------------------
# \s==>Space character
# \S==>Any character except space character
# \d==>Any digit from 0 to 9
# \D==>Any char except digit
# \w==>Any word char[a-zA-Z0-9]
# \W==>Any character except word character[special chars]
# . ==>Any character including special chars

# Ex: 1
# -----
import re
matcher = re.finditer('\s','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
    
# Ex: 2
import re
matcher = re.finditer('\S','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
     
# EX: 3

import re
matcher = re.finditer('\d','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
     
# Ex: 4

import re
matcher = re.finditer('\D','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
     
# Ex: 5

import re
matcher = re.finditer('\w','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
      
# EX: 6

import re
matcher = re.finditer('\W','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())
      
# Ex: 7

import re
matcher = re.finditer('.','a7b k@9z')
for match in matcher:
	print(match.start(),'...',match.group())