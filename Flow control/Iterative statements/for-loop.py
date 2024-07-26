'''
2).Iterative Statements:
-----------------------------------
-->If we want to execute a group of statements multiple times then we should go for iterative statements.
-->Python supports 2-types of iterative statements.
					-->for loop
					-->while loop
1.for loop:
---------------
-->If we want to execute some action for every element present in some sequence(It may be list,tuple or string or collection) then we should go for 'for loop'.

Syn:
	for x in sequence:
		body
		------
		------

Ex:To print the characters present in the given string.
----------------------------------------------------------------------------------
s = 'sunny leone'
for x in s:
	print(x)

'''

# Ex-1: To print the characters present in the given string.

s = 'radhikha'
for i in s:
    print(i)

# Ex-2: To print chharacters present in string index wise.
t = 'tillu square'
i=0
for x in t:
    print('The character present at',i,'index:',x)
    i=i+1

# Ex-3: To print hello world 10-times.

for i in range(10):
    print('Hello world')

# Ex-4: To print 1 to 10 numbers.

for i in range(10):
    print(i)


# Ex-5: To print odd numbers from 0-20
for i in range(21):
    if i%2!=0:
        print("The odd numbers are:",i)
        

# Ex-6: To print even numbers from 0-20
for i in range(21):
    if i%2==0:
        print("The even numbers are:",i)

# Ex-7: To display numbers from 10-1

for i in range(10,0,-1):
    print(i)

# Ex-8: To display the multiplication table.

n = eval(input("Enter a number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#  This program is very important.

a = [0,1,2,3]
for a[-1] in a:
    print(a[-1])

b = [0,1,2,3]
for b[-2] in b:
    print(b[-2])

c = [0,1,2,3]
for c[-2] in c:
    print(c[-3])