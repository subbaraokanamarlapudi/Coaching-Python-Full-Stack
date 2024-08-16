# '''
# * It is a group of statements is repeatedly required then it is not recommended to write these statements
#     everytime seperately. 
# * We have to define these statements as a single unit and we can call that unit any
#     number of times as per our requirement without re-writting. 
#     This unit is nothing but a function.
# * The main advantage of functions is code reusability.

# Note:
# * In other languages functions are known as methods,procedures,subroutines,etc..........

# ****************************** Types of Functions **********************

# 1. Built-in Functions:
# * The functions which are coming along with python software automatically,are called as bulit-in functions (or) pre-defined function.
# Example : id(),type(),input(),eval(), etc....................

# 2. User Defined Functions:
# * The functions which are developed by programmers explicitly according to business requirements,are called as user defined funcions.

# Syntax : 

# def function_name(parameter):   
#      statements
#      statements
#      statements
#     return value


# Parameters:
# -----------
# * Parameters are inputs to the function. If the function contains parameter,then at the time 
#     of calling ,compulsory we should provide values,otherwise we will get an error.

# Return statement: 
# ----------------
# * Function can take input as parameter and executes business logic , and returns output to the caller within the return statement.
# * If we are not writing return statement then default return value is None.

# Returning multiple values from a function : 
# -------------------------------------------

# * In other languages like c,c++ and java functions can return atmost one value.
# * But in python we can return multiple values from a function.
# '''

# # Example 1:

# def wish():
#     print("Hello Good Morning")
# wish()

# # Parameter example : 

# def wish(name):
#     print("Hello Good Morning",name)
# wish("Vijay")
# wish("venkata")

# def wish(name):
#     print("Hello Good Morning",name)
# print(wish("Vijay")) # None
# print(wish("venkata")) # None

# # W.A.P a function to take number as input and print its square value.

# def squareit(num):
#     print("The square of ",num,"is",num*num)
# squareit(4)
# squareit(5)

# # Return statement example : 

# def add(x,y):
#     return x+y
# result = add(10,20)
# print('The sum is:',result)
# print('The sum is:',add(100,200))

# def f1():
# 	print('Hi')
# print(f1())

# # W.A function to check whether the given number is even or odd?

# def even_odd(num):
#     if num%2==0:
#         print(num,"is even number")
#     else:
#         print(num,"is odd number")
# even_odd(10)
# even_odd(15)

# # W.A.P a function to check whether the given number is prime or not?

# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not prime number")
#             break
#     else:
#         print(num,"is prime number")

# is_prime(10)
# is_prime(3)

# # W.A.P a function to print all prime numbers between 1 to 100?

# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print('The prime numbers are:',num)
# for i in range(1,101):
#     is_prime(i)

# # W.A a function to find the factorial of a given number.

# def fact(num):
#     result = 1
#     while num>=1:
#         result = result * num
#         num = num - 1
#     return result
# # print("The factorial of 5 is:",fact(5))

# for i in range(1,6):
#     print("The factorial of",i,"is:",fact(i))

# # -------------------> Returning multiple values Example.

# def sum_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum,sub
# x,y = sum_sub(100,50)
# print("The sum is:",x)
# print("The sum is:",y)

# def calc(a,b):
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return sum,sub,mul,div

# x = calc(100,50)
# print(type(x))
# print("The results are:")
# for i in x:
#     print(i)

# '''
# --------------------------- Types of args --------------------------

# def f1(a,b):
# 	-----
# 	-----
# 	-----
# f1(10,20)

# -->a,b are formal args where as 10,20 are actual args.

# There are 4-types of actual args are allowed in python.
# 			1.positional args
# 			2.keyword args
# 			3.default args
# 			4.variable length args

# 1.positional args:
# -------------------------
# These are the args passed to function in correct positional order.
# -->The number of args and position of args must be matched. If we change the order then result may be chaned.

# -->If we change the number of args then we will get an error.
# sub(10) #sub() missing 1 required positional argument: 'b'
# sub(10,20,30)#sub() takes 2 positional arguments but 3 were given


# 2).keyword args:
# ------------------------
# We can pass argument values by keyword i.e by parameter name

# def wish(name,msg):
# 	print('Hello',name,msg)
# wish(name='sunny',msg='good evening....')
# wish(msg='good evening....',name='sunny')

# -->Here the order of args is not important but number of args must be matched.

# Note:
# 	We can use both positional and keyword args simultaneously. But first we have to take positional args and then keyword args, otherwise we will get an error.

# 3).default args:
# ----------------
# * Sometimes we can provide default values for our positional args.

# Ex:
# def wish(name='radhika'):
# 	print('Hello',name,'good evening.....')
# wish()
# wish('lilly')

# * If we are not passing any name then only default value will be considered.

# 4).variable length args:
# ------------------------

# * Sometimes we can pass any number of args to our function, such type of args are called as variable length of args.
# * We can declare a variable length of args with '*' symbol as:
#                             def f1(*n):
# * We can call this function by passing any number of args including zero number , internally all these values represented in the 
#   form of tuple.

# Note:
# 	After variable length argument, if we are taking any other args then we should provide values as keyword args.


# Note:
# 	We can declare keyword variable length args also. For this we have to use **
# 						def f1(**n):pass
# 	We can call this function by passing any number of keyword args. Internally these keyword args will be stored inside a dict.
# '''

# # Example : 1 -----> [positional arguments]

# def sub(a,b):
#     print(a-b)
# sub(10,20)
# sub(50,100)

# # Example : 2 -------> [keyword arguments]

# def wish(name,msg):
# 	print('Hello',name,msg)
# wish(name='sunny',msg='good evening....')
# wish(msg='good evening....',name='sunny')
# wish('sunny','good evening....')#Valid
# wish('sunny',msg='good evening....')#Valid
# # wish(name='sunny','good evening....')#Invalid

# # Example : 3 --------> [default arguments]

# def wish(name='radhika'):
#     print('Hello',name,'good evening.....')
# wish()
# wish('lilly')

# # Example : 4 --------> [variable length arguments]

# def sum(*n):
#     total = 0
#     for i in n:
#         total = total + i
#     print('The sum is:',total)

# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30)
# sum(10,20,30,40)

# # Ex : 

# def f1(n1, *s):
#     print(n1)
#     for i in s:
#         print(i)

# f1(10)
# f1(10,20)
# f1(10,20,30)
# f1(10,'A',20,'B',30)

# # Ex :

# def f1(*s,n1):
# 	for i in s:
# 		print(i)
# 	print(n1)
# f1(10,20,30,n1=40)


# # Example : 

# def f1(**kwargs):
# 	for k,v in kwargs.items():
# 		print(k,'=',v)
# f1(n1=10,n2=20,n3=30)
# f1(rno=101,name='radhika',marks=98,subject='python')

# # CASE STUDY : 

# def f(arg1,arg2,arg3=4,arg4=8):
# 	print(arg1,arg2,arg3,arg4)
# f(3,2)#3 2 4 8
# f(10,20,30,40)#10 20 30 40
# f(25,50,arg4=100)#25 50 4 100
# f(arg4=2,arg1=3,arg2=4)#3 4 4 2
# f()# f() missing 2 required positional arguments: 'arg1' and 'arg2'
# f(4,5,arg2=6)#f() got multiple values for argument 'arg2'
# # f(arg3=10,arg4=20,30,40)#positional argument follows keyword argument
# f(4,5,arg3=5,arg5=6)# f() got an unexpected keyword argument 'arg5'

# def f(*,a,b):       # Keyword only argument
#     print(a,b)
#     # print(type(a),type(b))

# f(a=10,b=20)
# f(b=20,a=10)
# f(10,20) #TypeError: f() takes 0 positional arguments but 2

# def f(a,b,/):  # Positional only arguments.

'''
Function vs Module vs Package vs Library:
---------------------------------------------------------------
-->A group of lines with some name is called as a function.
-->A group of functions saved to a file is called as module.
-->A group of modules is nothing but package.
-->A group of packages is nothing but library.

Types of variables:
	1.Global variables
	2.Local varisbles

1.Global variables:
------------------------
-->If the value of a variable is defined outside a function then such type of variables are called as global variables.
-->Global variables can be accessed inside as well as outside of the function.
-->If we change the value of global variable inside a function then the change will be reflected in outside of the function also.
-->If we declare a variable inside a function with same name as global variable then this local variable will be given preference.
-->If we want to modify the value of global variable inside a function then we should use global keyword.

Ex:
a = 10 #global variables
def f1():
	print('f1:',a)
def f2():
	print('f2:',a)
f1()
f2()

2.Local Variable:
------------------
-->The variable which are declared inside a function are called as local variable.
-->Local Variable are available only for the function in which we declared it. i.e from outside of function we cant access.

def f1():
	a = 10 #local variables
	print('f1:',a)
def f2():
	print('f2:',a)#NameError: name 'a' is not defined
f1()
f2()

3.Global Keyword:
------------------
-->If we want to modify the value of global variable inside a function then we should use global keyword.
-->To declare global variable inside a function.
-->To make global variable available to the function so that we can perform requirement modifications.

Ex:
a = 10 
def f1():
	global a
	a = 333 #global 
	print('f1:',a)
def f2():
	print('f2:',a)
f1()==>333						f2()==>10
f2()==>333						f1()==>333

Note : 
* If the global variable and local variable having same name then we can access global variable inside a 
  function by using globals() function.

a = 10 
def f1():
	a = 333 
	print('f1:',a)#333
	print(globals()['a'])#10
f1()
'''

# Example : ---> Global variable.

# a = 10
# def f1():
#     print("The f1 value is:",a)

# def f2():
#     print("The f2 value is:",a)

# f1()
# f2()

# Example : ---> Local variable.

# def f1():
#     a = 10
#     print("The f1 value is:",a)

# def f2():
#     print("The f2 value is:",a)

# f1()
# f2()

# Example : ---> Global keyword.

# a = 10
# def f1():
#     global a
#     a = 333
#     print("The f1 value is:",a)

# def f2():
#     print("The f2 value is:",a)

# f1()
# f2()

# # By using the globals keyword

# a = 10
# def f1():
#     global a
#     a = 333
#     print("The f1 value is:",a)
#     print(globals()['a'])

# f1()

'''
RECURSIVE FUCNTION : 
--------------------------------
* A function that calls itself is know as recursive function.
Ex:
		factorial(3):3*factorial(2)
						3*2*factorial(1)
						3*2*1*factorial(0)
		factorial(n):n*factorial(n-1)

* The main advantages are :
* We can reduce length of the code and improve readability.
* We can solve complex problems easily.

def factorial(n):
	if n == 0:
		result = 1
	else:
		result = n*factorial(n-1)
	return result
print('Factorial of 4 is:',factorial(4))
print('Factorial of 5 is:',factorial(5))
'''

# Write a program factorial in recursive function

# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     return result

# print('Factorial of 4 is:',factorial(4))
# print('Factorial of 5 is:',factorial(5))

'''
ANONYMOUS FUNCTION :
--------------------------------
* Sometimes we can declare a function without name, such type of nameless functions are called as anonymous funcitons or lambda expressions.
* The main advantage of anonymous function is just for instant use(i.e for one time useage.)

Syn:
		lambda argument_list:expression
Note:
	By using lambda functions we can write concise code so that readability of the program will be improved

Note:
	Lambda function internally returns expression value and we are not required to write retuen statement explicitly.


Some times we can pass function as argument to another function. In such case lambda functions are best choice.

We can use lambda functions very commonly with filter(), map() and reduce() functions bcoz these functions expect function as argument.
'''

# Write a program to create a lambda function to find square of given number.

# Normal func:
# --------------------
# def squareit(n):
# 	return n*n
# print(squareit(3))
# print(squareit(4))

# # lambda func:
# # --------------------
# s = lambda n:n*n
# print('The square of 3 is:',s(3))
# print('The square of 5 is:',s(5))

# Write a lambda to find sum of 2 given numbers.

# s = lambda a,b : a + b
# print('The sum of 10 and 20 is:',s(10,20))
# print('The sum of 100 and 200 is:',s(100,200)).

# Write a lambda function to find biggest of 2 numbers.

# s = lambda a,b : a if a>b else b
# print('The biggest of 10 and 20 is:',s(10,20))
# print('The biggest of 100 and 200 is:',s(100,200))

# Q.
add = lambda x,y:x+y
result = add(3,5)*(lambda x:x**2)(2)
print(result)#32

# Q.
a = {1,1,1,2,2,6,6,6,6}
b = list(a)
print(b[2])

# Q.
s = 'python'
for i in range(len(s)):
	print(s)
	s = 'a'