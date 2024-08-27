'''
EXCEPTION HANDLING:
--------------------

* In any programming language there are 2-types of error are possible.
   1.Syntax Errors
   2.Runtime Errors

1. Syntax Error:
-----------------

* The errors which occurs because of invalid syntax are called syntax errors or parsing errors.
EX:
  x = 10
  if x == 10
    print("Hello")  # SyntaxError: expected ':'

Ex:
	print 'Hi'
SyntaxError: Missing parentheses in call to 'print'.

Note:
* Programmer is responsible to correct these errors. Once all syntax errors are corrected then only program execution will be started.

2. Runtime Errors:
-------------------
* It is also called as exceptions.
* While executing the program if something goes wrong because of end user input or programming logic or memory problems etc then we will get runtime errors.

Ex:
	print(10/0)==>ZeroDivisionError
	print(10/'ten')==>TypeError
	int('ten')==>ValueError

Note:
* Exception handling concept is applicable for runtime errors not for syntax errors.

What is an Exception?
---------------------------------
	An unwanted and unexpected event that distrubs normal flow of the program is called as an exception.
Ex:
	ZeroDivisionError
	ValueError
	TyrePuncheredError
	SleepingError

* It is highly recommended to handle exceptions. 
The main objective of exception handling is Graceful Termination of the program(i.e we should not block our resources and we should not miss anything).
* Exception handling does not mean repairing exception. 
We have to define alternative way to continue rest of the program normally.

Q.What is an Exception?
Q.What is the purpose of Exception Handling?
Q.What is the meaning of Exception Handling?

Default exception handling in python
--------------------------------------------------------
* Every exception in python is an object. For every exception type the corresponding classes are available.
* Whenever an exception occurs PVM will create the corresponding exception object and will check for handling code. 
    If the handling code is not available then python interprter terminates the program abnormally and prints corresponding ex ception information to the console.
* The rest of the program wont be executed.

Ex:
	print('Hello')
	print(10/0)
	print('Hi')

Customized exception handling by using try-except:
------------------------------------------------------------------------------
* The code which may raise exception is called as risky code and we have to take risky code inside try block. 
    The corresponding handling code we have to take inside except block.
* Syn:
	try:
		Risky code
	except XXX:
		Handling code/Alternative code

Ex:
print('stmt-1')
try:
	print(10/0)
except ZeroDivisionError:
	print(10/2)
print('stmt-3')

Control flow in try-except block:
-------------------------------------------------
Ex:
	try:
		stmt-1
		stmt-2
		stmt-3
	except XXX:
		stmt-4
	stmt-5

Case-1:If there is no exception.
			1,2,3,5 Normal Termination.

Case-2:If an exception raised at stmt-2 and corresponding except block is matched.
			1,4,5 Graceful Termination.

Case-3:If an exception raised at stmt-2 and corresponding except block is not matched.
			1 Abnormal Termination.

Case-4:If an exception raised at stmt-4 or stmt-5 then it always abnormal termination.

Conclusions:
-------------------
1).Within the try block if anywhere exception raised then rest of the try block wont be executed eventhough we handled that exception. Hence we have to take only risky code inside the try block and length of the try block should be as less as possible.

2).In addition to try block, there may be chance of raising exception inside except block also.

3).If any statement which is not part of try block raises an exception then it is always abnormal termination.

How to print exception information?
------------------------------------------------------
try:
	print(10/0)
except ZeroDivisionError as msg:
	print("Exception raised and it's description is:",msg)

try with multiple except blocks:
---------------------------------
--> The way of handling exception is varied exception to exception. Hence for every exception type a separate except block we have to provide. i.e
	try with multiple except block is possible and recommended.
--> If try with multiple except blocks are available then based on raised exception the corresponding except block will be executed.

try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except ZeroDivisionError:
	print("Can't devide with zero")
except ValueError:
	print('Pls provide int values')

-->If try with multiple except blocks available then the order of these except blocks is important. Python interpreter will always consider top to bottom until matched except block identified.

try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except ArithmeticError:
	print('ArithmeticError')
except ZeroDivisionError:
	print("ZeroDivisionError")
    
Single except block that can handle multiple exceptions:
----------------------------------------------------------

try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except (ZeroDivisionError,ValueError) as msg:
	print("Pls provide valid numbers only problem is:",msg)
    
-->We can use default except block to handle any type of exception.
-->In default except block generally we can print normal error messages.

Syn:
		except:
			statements

try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except ZeroDivisionError:
	print("ZeroDivisionError:Can't devide with zero")
except :
	print('DefaultExcept:Pls provide valid input')

Note:
	If try with multiple except blocks available then the default except block should be last, otherwise we will get SyntaxError.
						SyntaxError: default 'except:' must be last

Various combinations of except block
--------------------------------------------------------
1.except ZeroDivisionError:
2.except ZeroDivisionError as msg:
3.except (ZeroDivisionError,ValueError):
4.except (ZeroDivisionError,ValueError) as msg:
5.except:


finally block:
----------------
--> It is not recommend to maintain clean up code(Resource deallocation core or resource releasing code) inside try block because there is no guarantee for the execution of every statement inside try block always.
--> It is not recommend to maintain clean up code inside except block, because if there is no exception then except block wont be executed.
--> Hence we required some place to maintain clean up code which should be executed always irrespective of whether exception raised or not raised and whether exception handled or not handled.
	such type of best place is nothing but finally block.
--> Hence the main purpose of finally block is to maintain clean up code.

Syn:
	try:
		Rsiky code
	except :
		Handling code
	finally:
		Clean up code

Note:
	There is only one situation where finally block wont be executed i.e whenever we are using os._exit(0) function.

	Whenever we are using os._exit(0) function then PVM itself will be shutdown. In this particular case finally block won't be executed.

import os
try:
	print('try')
	os._exit(0)
except NameError:
	print('except')
finally:
	print('finally')

os._exit(0):0 represents status code and it indicates normal termination.

* Control floe of try-except -finally
-------------------------------------------------
try:
	stmt-1
	stmt-2
	stmt-3
except:
	stmt-4
finally:
	stmt-5
stmt-6

Case-1:If there is no exception
			1,2,3,5,6 Normal Termination

Case-2:If an exception raised in stmt-2 and the corresponding except block matched.
			1,4,5,6 Graceful termination

Case-3:If an exception raised in stmt-2 and the corresponding except block not matched.
			1,5 Abnormal termination

Case-4:An exception raised at stmt-5 or stmt-6 then it is always abnormal termination.

Case-5:An exception raised at stmt-4 then it always abnormal termination but before that finally block will be executed.

Nested try-except-finally block:
----------------------------------------------
* Generally risky code we have to take inside outer try block and too much risky code we have to take inner try block.
* Inside inner try block if any exception raised then inner except block is responsible to handle.
* If unable to handle then outer except block is responsible to handle.

try:
	print('Outer try block')
	try:
		print('Inner try block')
		print(10/0)
	except NameError:
		print('Inner except block')
	finally:
		print('Inner finally block')
except:
	print('Outer except block')
finally:
	print('Outer finally block')

else block with try-except-finally:
-------------------------------------------------
-->We can use else block with try-except-finally block
-->else block will be executed if and only if there are no exceptions inside try block.

Syn:
-------
try:
	Risky code
except:
	will be executed if exception inside try
else:
	will be executed if there is no exception inside try
finally:
	will be executed whether exception raised or notraised handled or not handled.

Ex:
-----
try:
	print('try')
	print(10/0)===>Line-1
except:
	print('except')
else:
	print('else')
finally:
	print('finally')

-->If we comment Line-1 then else block will be executed bcoz there is no exception inside try. In this case the output is:try	else	finally

-->If we are not commenting Line-1 then else block wont be executed bcoz there is an exception inside try block. In this case output is:try		except		finally
'''

# x = 10
# if x == 10
#     print("Hi")

# print 'Hi'

print(10/0)  #==>ZeroDivisionError
print(10/'ten')  #==>TypeError
int('ten')  #==>ValueError

print('statement-1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('statement-3')

try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception raised and it's description is:", msg)

# Ex:

try:
    x = int(input('Enter first number:'))
    y = int(input('Enter second number:'))
    print(x/y)
except ZeroDivisionError:
    print("Can't devide with zero")
except ValueError:
    print('Pls provide int values')

try:
    x = int(input('Enter first number:'))
    y = int(input('Enter second number:'))
    print(x/y)
except ArithmeticError:
    print("Can't devide with zero")
except ZeroDivisionError:
    print('Pls provide int values')

# Single except block that can handle multiple exceptions

try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except (ZeroDivisionError,ValueError) as msg:
	print("Pls provide valid numbers only problem is:",msg)

# Default except block:
# ----------------------

try:
    x = int(input('Enter first number:'))
    y = int(input('Enter second number:'))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError:Can't devide with zero")
except :
    print('DefaultExcept:Pls provide valid input')

# finally block
# ---------------

# Case-1:If there is no exception
# ----------------------------------------------
try:
	print('try')
except:
	print('except')
finally:
	print('finally')

# o/p:try		finally

# Case-2:If there is an exception raised but handled
# ---------------------------------------------------------------------------
try:
	print('try')
	print(10/0)
except ZeroDivisionError:
	print('except')
finally:
	print('finally')

# o/p:try		except		finally

# Case-3:If there is an exception raised but not handled
# ---------------------------------------------------------------------------------
try:
	print('try')
	print(10/0)
except NameError:
	print('except')
finally:
	print('finally')

# o/p:try		finally		Abnormal termination.

# Nested try-except-finally block
# ----------------------------------------------
try:
	print('Outer try block')
	try:
		print('Inner try block')
		print(10/0)
	except NameError:
		print('Inner except block')
	finally:
		print('Inner finally block')
except:
	print('Outer except block')
finally:
	print('Outer finally block')

# else block with try-except-finally:
# ----------------------------------------------

try:
	print('try')
	print(10/0)
	# print(10/0)===>Line-1
except:
	print('except')
else:
	print('else')
finally:
	print('finally')