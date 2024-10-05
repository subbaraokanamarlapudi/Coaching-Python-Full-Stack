# Synchronization:
# -------------------------
# -->If multiple threads are executing simultaneously then there may be a chance of data inconsistency problems.

from threading import *
import time
def wish(name):
	for i in range(10):
		print('good evening:',end='')
		time.sleep(1)
		print(name)
t1 = Thread(target=wish,args=('sunny',))
t2 = Thread(target=wish,args=('bunny',))
t1.start()
t2.start()

# -->We are getting irregular output bcoz both threads are executing simultaneously wish() function.
# -->To overcome this problem we should go for synchronization.
# -->In synchronization the threads will be executed one by one so that we can overcome data inconsistency problems.
# -->Synchronization means at a time only one thread.

# We can implement synchronization by using:
# 		1.Lock
# 		2.RLock
# 		3.Semaphore

# Synchronization by using Lock
# ----------------------------------------------
from threading import *
import time
l = Lock()
def wish(name):
	l.acquire()
	for i in range(10):
		print('good evening:',end='')
		time.sleep(1)
		print(name)
	l.release()
t1 = Thread(target=wish,args=('sunny',))
t2 = Thread(target=wish,args=('bunny',))
t1.start()
t2.start()

# problem with simple Lock:
# ----------------------------------------
# Ex:
# -----
from threading import *
l = Lock()
print('MainThread trying to acquire lock')
l.acquire()
print('MainThread trying to acquire locka gain')
l.acquire()

# -->In the above program MainThread will be blocked bcoz it is trying to acquire the lock second time.
# -->If the thread calls recursive functions, then the thread may trying to acquire the same lock again and again, which may block our thread.
# -->To overcome this problem, we should go for RLock(Reentrant Lock). Reentrant means the thread can acquire the same lock again and again.
# -->Reentrant facility is available only for owner thread but not for other threads.

# Ex:
from threading import *
import time
l = Lock()
def factorial(n):
	l.acquire()
	if n == 0:
		result = 1
	else:
		result = n*factorial(n-1)
	l.release()
	return result

def results(n):
	print('The factorial of',n,'is:',factorial(n))

t1 = Thread(target=results,args=(5,))
t2 = Thread(target=results,args=(4,))
t1.start()
t2.start()

# Synchronization byusing Semaphore:
# -------------------------------------------------------
# -->In the case of Lock, RLock at a time only one thread is allowed to execute.
# -->Semaphore can be used to limit the access to the sahred resources with limited capacity.

# Ex:
# from threading import *
# import time
# s = Semaphore(2)
# def wish(name):
# 	# -----
# 	# ------
# t1 = Thread(target=wish,args=('sunny',))
# t2 = Thread(target=wish,args=('bunny',))
# t3 = Thread(target=wish,args=('vinny',))
# t1.start()
# t2.start()
# t3.start()

# -->In the above program at a time 2-threads are allowed to access Semaphore and hence 2-threads are allowed to execute wish() function.

# BoundedSemaphore:
# 	It is exactly same as Semaphore except that the number of release() calls should not exceed the number of acquire() class, otherwise we will get error.

from threading import *
s = BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
print('End')

# ValueError: Semaphore released too many times

# Conclusion:
# -----------------
# The main advantage of synchronization is we can overcome data inconsistency problems. 
# But the main disadvantage of synchronization is it increases waiting time of threads and creates performance problems. 
# Hence if there is no specific requirement then it is not recommended to use synchronization.
