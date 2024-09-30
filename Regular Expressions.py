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
      
# Quantifiers:
# ==========
# 	To specify the number of occyrences to match.

# a==>Exactly on 'a'
# a+==>Atleast one 'a'
# a*==>Any number of a's including zero number.
# a?==>Atmost one 'a' i.e either zero number or one number.
# a{m}==>Exactly m number os a's
# a{m,n}==>Minimum 'm' number of a's and max 'n' number of a's

# EX : 

import re   
matcher = re.finditer('a','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Ex : 2

import re   
matcher = re.finditer('a+','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Ex : 3

import re   
matcher = re.finditer('a*','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Ex : 4

import re   
matcher = re.finditer('a?','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Ex : 5

import re   
matcher = re.finditer('a{2}','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Ex : 6

import re   
matcher = re.finditer('a{2,4}','abaabaab')
for match in matcher:
	print(match.start(),'...',match.group())

# Note:
# 	^x==>It will check whether target string starts with x or not
# 	x$==>It will check whether target string ends with x or not

# Functions of re module:
# 	match(),fullmatch(),search(),findall(),finditer(),sub(),subn(),split(),compile()

# 1.match():
# 	To check the given pattern at beginning of target string.
# 	If the match is available then we will get match object, otherwise we will get None.

import re
s = input('Enter pattern to check:')
m = re.match(s,'abcdefg')
if m != None:
	print('Match is available at the beginning of the string')
	print('Start index:',m.start(),'and end index:',m.end())
else:
	print('Match is not available at the beginning of the string')

# 2.fullmatch():
# 	To match a pattern to all of target string. i.e complete string should be matched according to given pattern

import re
s = input('Enter pattern to check:')
m = re.fullmatch(s,'ababab')
if m != None:
	print('Full string matched')
else:
	print('Full string not matched')

# 3.search():
# 	To search the given pattern in the target string.
# 	If the match is available then it returns the match object which represents first occurence of the match.

import re
s = input('Enter pattern to check:')
m = re.search(s,'abaaaba')
if m != None:
	print('Match is available')
	print('First occurence of match with start indes:',m.start(),'end index:',m.end())
else:
	print('Match is not available')

# 4.findall():
# 	To find all occurences of the match in the form of list.

import re
l = re.findall('[0-9]','a7b9c5kz')
print(type(l))
print(l)

# 5.sub():
# 	sub means substitution or replacement.
# 		re.sub(regex,replacement,targetstring)
# 	In the target string every matched pattern will be replaced with provided replacement.

import re
s = re.sub('[a-z]','#','a7b9c5k8z')
print(s)

# -->Every alphabate symbol is replaced with # symbol.

# 6.subn():
# 	It is exactly same as sub except it can also returns the number of replacements.
# 	This function returns a tuple where first element is result string and second element is number of replacements.
# 							(resultstring,number of replacements)

import re
t = re.subn('[a-z]','#','a7b9c5k8z')
print(t)
print('The Result String:',t[0])
print('The number of replacements:',t[1])

# 7).split():
# 	-->If we want to split the given target strint according to a particular pattern then we should go for split() function.
# 	-->This function returns list of all tokens.

# Ex:

import re
l = re.split(',','sunny,bunny,vinny')
print(l)
for i in l:
	print(i)

# Ex:

import re
l = re.split('\.','www.nareshit.com')
print(l)
for i in l:
	print(i)

# ^ symbol:
# ---------------
# 	To check whether the given string starts with our provided pattern or not.

# Ex:

import re
s = 'Learning Python Is Very Easy'
res = re.search('^Learn',s)
if res != None:
	print('Target string starts with Learn')
else:
	print('Target string not starts with Learn')

# $ symbol:
# --------------
# 	To check whether the given string ends with our provided pattern or not.

import re
s = 'Learning Python Is Very Easy'
res = re.search('Easy$',s)
if res != None:
	print('Target string ends with Easy')
else:
	print('Target string not ends with Easy')

# Note:
# 	If we want to ignore case then we have to pass 3rd argument re.IGNORECASE for search() function.
# 	Ex:res = re.search('Easy$',s,re.IGNORECASE)

# Write a regular expression to represent all s language indetifiers(s-programmmin)
# ------------------------------------------------------------------------------------

# Rules:
# * The allowed characters are a-z,A-Z,0-9,#
# * The first character should be lower case from a-k
# * The second character should be digit divisible by 3
# * The length of identifier should be atleast 2

#    General regular expression : [a-k][0369][a-zA-Z0-9#]*

# Ex:

import re
s = input('Enter identifier:')
m = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m != None:
	print(s,'is valid identifier')
else:
	print(s,'is invalid identifier')

# Write a regular expression to represent 10-digit mobile numbers.
# ----------------------------------------------------------------------

# Rules:
# 	1.Every number should contains exzctly 10-digits.
# 	2.The first digit should be 6 or 7 or 8 or 9
			
# 			[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]

# 			[6-9][0-9]{9}

# 			[6-9]\d{9}

# Ex:

import re
s = input('Enter mobile number:')
m = re.fullmatch('[6-9]\d{9}',s)
if m != None:
	print(s,'is valid mobile number')
else:
	print(s,'is invalid mobile number')

# Ex:w.a.p to extract all mobile numbers present in input.txt where numbers are mized with normal text data.
# ------------------------------------------------------------------------------------------------------------

# Ex:

import re
f1 = open('input.txt','r')
f2 = open('output.txt','w')
for line in f1:
	list = re.findall('[6-9]\d{9}',line)
	for n in list:
		f2.write(n+'\n')

print('Extracted all mobile numbers into output.txt')
f1.close()
f2.close()

# w.a.p to check whether the given mobile number is valid or not
# (10-digit or 11-digit or 12-digit)

import re
s = input('Enter Number:')
m = re.fullmatch('(0|91)?[6-9]\d{9}',s)
if m != None:
	print(s,'is valid mobile number')
else:
	print(s,'is invalid mobile number')