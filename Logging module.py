'''
****Logging Module
-------------------

* It is highly recommend to store complete application flow and exceptions information to a file. This process is called as logging.
* The main advantage of logging are:
   1. We can use log files while performing debugging.
   2. We can provide statistics like number of requests per day etc....
* To implement logging, python provides one inbulit module:logging

* Logging Levels:
------------------

Depending on type of information, logging data is devided according to 6-levels.

1.CRITICAL==>50
2.ERROR==>40
3.WARNING==>30
4.INFO==>20
5.DEBUG==>10
6.NOTSET==>0

How to implement logging:
----------------------------------------
-->To perform logging, first we required to create a file to store messages and we have to specify which level messages we have to store.
-->We can do this by using basicConfig() function of logging module.
			logging.basicConfig(filename='log.txt',level=logiing.WARNING)
-->The above line will create a dile log.txt and we can store either WARNING or higher level messages to thet file.
-->After creating log file, we can write messages to that file by using methods.
					logging.debug(message)
					logging.info(message)
					logging.warning(message)
					logging.error(message)
					logging.critical(message)

Note:
	In the above program only WARNING and higher level messages will be written to log file. If we set level as DEBUG then all the messages will be written to log file.

How to write python program exceptions to log file
----------------------------------------------------------------------------
-->We can write exceptions information to the file by using exception() function.

Assertions:
------------

Debugging python program by using assert keyword
-----------------------------------------------------------------------------
-->The process of identifying and fixing the bugs is called as debugging. Very common way of debugging is to use print() statement. But the problem with the print() statement is after fixing the bug, compulsory we have to delete the extra added print() statements, otherwise these will be executed at the runtime which creates performance problems and distrubs console output.

-->To overcome this problem we should go for assert statement. The main advantage of assert statement over print() statement is after fixing bugs we are not required to delete assert statements. based on our requirement we can enable and disable assert statements.

-->Hence the main purpose of assertion to perform debugging, usually we can perform debugging either in development or in test environments but not in production environment.

Types of assert statements:
			1.Simple version
			2.Augmented version

1.Simple version:
								assert condition_expression

2.Augmented version:
								assert condition_expression,message

-->conditional_expression will be evaluated and it is True then the program will be continued.
-->If it is False then the program will be terminated by raising AssertionError.
-->By seeing AssertionError, programmer can analyze the code and fix the problem.

Note:To disable assert statements py -O test.py

Exception Handling vs Assertions:
---------------------------------------------------
-->Assertions concept can be used to alert the programmer to resolve development time errors.
-->Exception handling can be used to handle runtime errors.

'''

# Q : W.A.P to create a log file and write WARNING and higher level messages.

import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')

# write a program by using the exceptions to log file.

import logging
logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info("A new request came")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("The result:",x/y)
except ZeroDivisionError as msg:
    print("Cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Please provide int values only")
    logging.exception(msg)
logging.info("Request processing completed")

# Assertions examples:
# ---------------------

def squareit(x):
    return x**x

assert squareit(2)==4,'The square of 2 should be 4'
assert squareit(3)==9,"The square of 3 should be 9"
assert squareit(4)==16,'The square of 4 should be 16'

print(squareit(2))
print(squareit(3))
print(squareit(4))