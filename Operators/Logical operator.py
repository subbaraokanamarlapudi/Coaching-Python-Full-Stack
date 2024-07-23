'''
* It is used to combine multiple conditions together and evaluate them as a single boolean expression.
* There are : and , or , not
* and : It returns True if both the conditions are True, otherwise False.
* or : It returns True if any one of the conditions is True, otherwise False.
* not : It returns True if the condition is False.

Ex:
	True and False #False
	True or False #True
	not False #True

For non-boolean type behaviours:
--------------------------------------------------
-->0 means False
-->non-zero means True
-->Empty string always False.

x and y:
------------
	If x evaluates to False return x otherwise return y.
Ex:
10 and 20 #20
0 and 10 #0

-->If the first argument is zero then result is zero otherwise result y.

x or y:
----------
	If x evaluates to True then result is x otherwise result is y.
Ex:
	10 or 20 #10
	0 or 20 #20

not x:
---------
-->If x evaluates to False then the result is True otherwise False
Ex:
not 10 #False
not '' #True

Ex:
'sunny' and 'mahesh' #'mahesh'
'' and 'sunny' #''
'' or 'sunny' #'sunny'
'sunny' or '' #'sunny'
not 'radhika' #False 
10 or 10/0 #10
0 or 10/0 #ZeroDivisionError

'''

print(True and False)
print(True or False)
print(not False)

# Non-boolean Datatypes

print("Non datatypes-----------")
print(10 and 20)
print(0 and 10)
print(10 or 20) 
print(0 or 20)
print(not 10)
print(not '')
print("--------------------")

print('sunny' and 'mahesh')
print('' and 'sunny')
print('' or 'sunny')
print('sunny' or '')
print(not 'radhika')
print(10 or 10/0)
print(0 or 10/0)