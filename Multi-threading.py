
# Multi-threading:
# * Executing several tasks simultaneously is the concept of multi-tasking.
# * There are 2-types of multi-tasking are there:
#    1. Process Based multi-tasking
#    2. Thread Based multi-tasking

# * module : threading


# Q : Program to print name of the current excuting thread.
# --------------------------------------------------------------

import threading
print('Current executing thread:',threading.current_thread().name)

# Note : Threading module contains function current_thread() which returns the current executing thread object. 
# On this object if we call name attribute then we will get current executing thread name.

# The way of creating thread in python:
# -------------------------------------

# 1. Creating a Thread without using any class:
# ----------------------------------------------

# EX: 1

from threading import *
def display():
    print('This code(Display func) is executed by thread:',current_thread().name)

t = Thread(target=display)
t.start()
print('This code executed by thread:',current_thread().name)

# Note: Thread is a pre-defined class present in threading module which can be used to create our own threads.

# Creating multiple threads
# --------------------------------------
from threading import *
def display():
	for i in range(10):
		print('Child Thread')
t = Thread(target = display)
t.start()
for i in range(10):
	print('Main Thread')
	
# If the multiple threads present in our program, then we cannot expect execution order and hence we cannot expect exact output for multi threaded program.
# Beacause of this we cannot provide exact output for the above program. It is vared from machine to machine and run to run.


# 2.Creating a Thread by extending Thread class:
# -----------------------------------------------------------------------
# We have to create child class for Thread class. In that child class we have to override run() method with our required job. Whenever we call start() method then automatically run() method will be executed and performs our job.

from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print('Child Thread-1')
t = MyThread()
t.start()
for i in range(10):
	print('Main Thread-1')

# 3).Creating a Thread without extending Thread class
# -------------------------------------------------------------------------------
from threading import *
class Test:
	def display(self):
		for i in range(10):
			print('Child Thread')
obj = Test()
t = Thread(target = obj.display)
t.start()
for i in range(10):
	print('Main Thread')

# without multi threading
# ----------------------------------
import time
def doubles(numbers):
	for n in numbers:
		print('Doube is:',2*n)
		time.sleep(1)
def squares(numbers):
	for n in numbers:
		print('Square is:',n*n)
		time.sleep(1)
numbers = [1,2,3,4,5,6]
begintime = time.time()
doubles(numbers)
squares(numbers)
endtime = time.time()
print('The total time taken:',endtime-begintime)

# with multi threading
# -------------------------------
import time
from threading import *
def doubles(numbers):
	for n in numbers:
		print('Doube is:',2*n)
		time.sleep(1)
def squares(numbers):
	for n in numbers:
		print('Square is:',n*n)
		time.sleep(1)
numbers = [1,2,3,4,5,6]
begintime = time.time()
t1 = Thread(target = doubles,args=(numbers,))
t2 = Thread(target = squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
print('The total time taken:',endtime-begintime)