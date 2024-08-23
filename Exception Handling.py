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

'''

x = 10
if x == 10
    print("Hi")

print 'Hi'

print(10/0)  #==>ZeroDivisionError
print(10/'ten')  #==>TypeError
int('ten')  #==>ValueError

print('statement-1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('statement-3')