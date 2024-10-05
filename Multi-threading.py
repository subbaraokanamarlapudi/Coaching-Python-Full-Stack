
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


# Setting and getting name of the thread
# ----------------------------------------------------------
from threading import *
print(current_thread().name)
current_thread().name = 'Radhika'
print(current_thread().name)

# Thread identification number:
# ---------------------------------------------
# For every thread internally a unique identification number is available. We can access this id by using implicit variable ident.

from threading import *
def test():
	print('Child Thread')
	print('Child Thread identification number:',current_thread().ident)
t = Thread(target=test)
t.start()
print('Main Thread identification number:',current_thread().ident)
print('Child Thread identification number:',t.ident)

# active_count():
# 	It returns the number of active threads currently running.

from threading import *
import time
def display():
	print(current_thread().name,'....started')
	time.sleep(3)
	print(current_thread().name,'....ended')
print('The number of active threads:',active_count())
t1 = Thread(target=display,name='ChildThread-1')
t2 = Thread(target=display,name='ChildThread-2')
t3 = Thread(target=display,name='ChildThread-3')
t1.start()
t2.start()
t3.start()
print('The number of active threads:',active_count())
time.sleep(5)
print('The number of active threads:',active_count())

# enumerate() function:
# --------------------------------
# 	It returns a list of all active threads currently running

l = enumerate()
for t in l:
	print('Thread Name:',t.name)
time.sleep(5)
l = enumerate()
for t in l:
	print('Thread Name:',t.name)

# is_alive():
# 	It is to check whether a thread is still executing or not.

print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())
time.sleep(5)
print(t1.name,'is Alive:',t1.is_alive())
print(t2.name,'is Alive:',t2.is_alive())

# join() method:
# ---------------------
# -->If a thread wants to wait until completing some other thread then we should go for join() method.

from threading import *
import time
def display():
	for i in range(10):
		print('Seetha Thread')
		time.sleep(2)
t = Thread(target=display)
t.start()
t.join()#This line executed by MainThread
for i in range(10):
	print('Rama Thread')

# Note:we can call join() method with time period also.
# 				t.join(seconds)
# -->In this case thread will wait only specified amount of time.		
# 				t.join(5)

# Daemon Threads:
# --------------------------
# -->The threads which are running in the background are called as Daemon Threads.

# -->The main objective of Daemon threads is to provide support for non-daemon threads(line Main Thread)

# Ex:Garbage Collector

# -->We can check whether thread is Daemon or not by using daemon property.

# from threading import *
# print(current_thread().daemon) #False

# we can change dameon nature:
# 		current_thread().daemon = True

# -->But we can use this one before starting of Thread. i.e once thread started, we cannot change its daemon nature. If we try to change we will get an error.
		
# 		RuntimeError: cannot set daemon status of active thread

# Default Nature:
# -----------------------
# -->Bydefault MainThread is always non-daemon. But for the remaining threads daemon nature will be inherited from parent to child.
# -->If the parent thread is daemon then child thread is also daemon.
# -->If the parent thread is non-daemon then child thread is also non-daemon.

# Case-1:parent non-daemon===>child is non-daemon
# ------------------------------------------------------------------------------
from threading import *
def job():
	print('Child Thread')
t = Thread(target = job)
print(t.daemon)

# Case-2:parent is daemon===>child is also daemon
# ---------------------------------------------------------------------------
from threading import *
import time
def job1():
	print('job-1 execution')
	print(current_thread().name,'is Daemon:',current_thread().daemon)
	ct = Thread(target = job2,name='Child Thread-2')
	print('ct is daemon:',ct.daemon)
def job2():
	print('Job2 execution...')
t = Thread(target = job1,name='Child Thread')
t.daemon = True
t.start()
time.sleep(10)

# -->Whenever the last non-daemon thread terminates automatically all daemon threads will be terminated.

from threading import *
import time
def job():
	for i in range(10):
		print('Lazy Thread')
		time.sleep(1)
t = Thread(target = job)
t.daemon = True
t.start()
time.sleep(5)
print('End of MainThread')