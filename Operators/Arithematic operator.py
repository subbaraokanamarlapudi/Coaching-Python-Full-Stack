'''
1.ARITHMETRIC OPERATORS:
* It is used to perform the basic mathamatics between 2 arguments.
* There are : +,-,*,/,//,%,**
* / -> when 2 arguments are perform division(/) it gives the decimal[float] value.
* // -> when 2 arguments are perform (//) it gives the integer value.
* Atleast one arguments are one float and one integer value it should return the float value.

Example:
10/2 #5.0  ,  10.0/2 #5.0 
10//2 #5   ,  10.0//2 #5.0

Note : 
* If want to use the string operator for both arguments,it should return the error  ----> Eg: 'sunny'+3 #Invalid , 'sunnu' + '3' # valid

'''

a = 40
b = 20

print("The sum is" , a+b)
print("The sub is" , a-b)
print("The mul is" , a*b)
print("The div is" , a/b)
print("The mod is" , a%b)
print("The floor div is" , a//b)
print("The power is" , a**b)