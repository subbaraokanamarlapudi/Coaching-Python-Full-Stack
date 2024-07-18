'''
2.RELATIONAL OPERATOR:
* It is used to compare the 2 arguments.
* There are: <,<=,>,>=
* we can apply the Relational operator for 'str' type also.

Example:
'sunny'<'mahesh' ---> By comparing the both string python complier observe the starting letter of both strings and give the output.
* By comparing the 's' ASCII value and 'm' ASCII value in the both arguments.   ord(s) #115 , ord(m) #109
* ASCII stands for the "American Standard Code for Information Interchange".
'''

a = 40
b = 20

print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

print('sunny'<'mahesh')

he = input("Enter a character:")
print("The ASCII value of" + he + "is" , ord(he))