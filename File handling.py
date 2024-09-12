'''
* As part of the programming requirement, we have to store our data permanently for future purpose.
  For this requirement we have should go for files.

Types of files:
    1. Text files
    2. Binary files

1. Text files:
---------------
* Usally we can use use text files to store characters data.
    Ex: abc.txt

2.Binary files:
---------------
* Usally we can use binary files to store binary data like images, audio, video etc.

Opening a file:
---------------
* Before performing any operation (like read or write) on the file, we have to open that file.
    For this we should use pythons inbuilt function open().
* But at the time of open, we have to specify mode, which represents the purpose of opening a file.

Syntax:     f = open(filename,mode)

The allowed modes in python are:

1.r==>Open an existing file for read operations. The file pointer positioned at the beginning of the file. If the specified file does not exist then we will get FileNotFoundError. This is the default mode.

2.w==>Open an existing file for write operations. If the file already contains some data then it will be overridden. If the specified file not availabe then this mode will create the file.

3.a==>Open an existing file for append operations. It wont override existing data. If the specified file is not available then this mode will create a new file.

4.r+==>To read and write data into the file. The previous data in the file will not be deleted. The file pointer is placed at the beginning of the file.

5.w+==>To write and read data. It will override existing data.

6.a+==>To append and read data from the file. It wont override existing data.

7.x==>To open a file in exclusive creating mode for write operations. If the file already exist then we will get FileExistsError.

Note:
	all above modes are applicable for text files. If the above modes suffixed with 'b' then these represents for binary files.
Ex:
		rb,wb,ab,r+b,w+b,a+b,xb

Closing file:
	AFter completing our operations on the file, it is highly recommended to close the file. For this we have to use close() function.
								f.close()

Various properties of file object:
------------------------------------------------
Once we opened a file and we got file object, we can get various details related to that file by using it's properties.

1.name:Name of the opened file.
2.mode:Mode in which the file is opened.
3.closed:Returns boolean value indicates that file is closed or not.
4.readable():Returns a boolean value indicates that whether file is readable or not.
5.writable():Returns a boolean value indicates that whether file writable or not.

Writting data to text file:
-------------------------------------
	1.write(str)
	2.writelines(list of lines)


'''

# Basic example : 

f = open('abc.txt','w')
print('File Name:',f.name)
print('File Mode:',f.mode)
print('Is File Readable:',f.readable())
print('Is File Writable:',f.writable())
print('Is File Closed:',f.closed)
f.close()
print('Is file closed:',f.closed)

# Writing data to text file

f = open('abcd.txt','w')
f.write('Hello\n')
f.write('Good\n')
f.write('Morning\n')
f.write('All\n')
print('Data written to the file successfully')
f.close()

'''
Note:
	In the above program, data present in the file will be overridden every time if we run the program. 
    Instead of overriding if we want to append then we should open the file as:f = open('abcd.txt','a')
'''

f = open('abcd.txt','w')
list = ['Ravi\n','Raju\n','Ramu\n']
f.writelines(list)
print('Data written to the file successfully')
f.close()


# Reading data from text file:

# 1. read(): To  read all data from the file.
# ----------------------------------------------

f = open('abcd.txt','r')
data = f.read()
print(data)
f.close()

# 2. read(n): To read 'n' characters from the file.
# --------------------------------------------------

f = open('abcd.txt','r')
data = f.read(10)
print(data)
f.close()

# 3. readline(): To read only one line from the file.
# ------------------------------------------------------

f = open('abcd.txt','r')
line1 = f.readline()
line2 = f.readline()
print(line1,end='')
print(line2)
f.close()

# 4.readlines():To read all lines into a list
# -----------------------------------------------------------
f = open('abcd.txt','r')
lines = f.readlines()
print(type(lines))
for line in lines:
	print(line,end='')
f.close()


'''
* with statement:
-------------------
* The with statement can be used while opening a file. we can use this to group file opeartion statement with a block.
* The advantage of with statement is it will take care closing of file, after completing all operations automatically even in explicitly.

EX:
with open('abcd.txt','w') as f:
	f.write('Naresh\n')
	f.write('IT\n')
	f.write('Technologies')
	print('Is file is closed:',f.closed)
print('Is file is closed:',f.closed)

tell() and seek()
-------------------

1.tell(): To return the current position of the file pointer.

f = open('abc.txt','r')
print(f.tell())
print(f.read(3))
print(f.tell())


2.seek(offset,from): To change the position of the file pointer.It is just like string index.

data = 'All Students Are BAD'
f = open('abc.txt','w')
f.write(data)
with open('abc.txt','r+') as f:
	text = f.read()
	print(text)
	print('The current position:',f.tell())
	f.seek(17)
	print('The current position:',f.tell())
	f.write('GEMS!!!!!')
	f.seek(0)
	text = f.read()
	print('Data after modification')
	print(text)
'''

with open('abcd.txt','w') as f:
	f.write('Naresh\n')
	f.write('IT\n')
	f.write('Technologies')
	print('Is file is closed:',f.closed)
print('Is file is closed:',f.closed)

# tell():

f = open('abc.txt','r')
print(f.tell())
print(f.read(3))
print(f.tell())

# seek():

data = 'All students are Bad'
f = open('abc.txt','w')
f.write(data)

with open('abc.txt','r+') as f:
    text = f.read()
    print(text)
    print('The current position:',f.tell())
    f.seek(17)
    print('The current position:',f.tell())
    f.write('GEMS!!!!!')
    f.seek(0)
    text = f.read()
    print('Data after modification')
    print(text)

# How to check a particular file exist or not ?
# --------------------------------------------------

# --> We can use os library to get information about files in our system.
# --> os.path.isfile(filename) returns True if file exists otherwise False.
#  syntax :         os.path.isfile(filename)

# Q: W.A.P to check whether the given file exists or not. If it is available then print its

import os
import sys

fname = input("Enter File Name: ")

if os.path.isfile(fname):
    print("File Exists:", fname)
    f = open(fname, 'r')
else:
    print("File does not exist")
    sys.exit(0)

print('The content of the file is:')
data = f.read()
print(data)
f.close()  

# Q: W.A.P to print number of lines,words and characters present in given file ?

import os,sys 
fname = input("Enter File Name:")
if os.path.isfile(fname):
	print("File Exists:",fname)
	f = open(fname,'r')
else:
	print("File does not exist")
	sys.exit(0)

lcount=wcount=ccount=0
for line in f:
	lcount=lcount+1
	ccount=ccount+len(line)
	words=line.split()
	wcount=wcount+len(words)
print('The number of lines:',lcount)
print('The number of words:',wcount)
print('The number of characters:',ccount)


# Handling Binary Data:
# ---------------------------------
# w.a.p to read image file and write to a new image file.

f1 = open('sunny.jpg','rb')
f2 = open('newpic.jpg','wb')
bytes = f1.read()
f2.write(bytes)
print('New image is available with the name:newpic.jpg')

# Handling CSV files:
# =================
# 			CSV==>Comma Separated Values
# 			To handle CSV files python provides module:csv

# Writting data to csv file:
# ------------------------------------

import csv
with open('emp.csv','w',newline='') as f:
	w = csv.writer(f)#Return csv write object pointing to f
	w.writerow(['ENO','ENAME','ESAL','EADDR'])
	n = int(input('Enter number of employees:'))
	for i in range(n):
		eno = input('Enter Employee No:')
		ename = input('Enter Employee Name:')
		esal = input('Enter Employee Salary:')
		eaddr = input('Enter Employee Address:')
		w.writerow([eno,ename,esal,eaddr])
print('Total employees data written to csv file successfully.....')

# Note:Observe the difference with newline attribute and without.

# with open('emp.csv','w',newline='') as f:
# with open('emp.csv','w') as f:

# -->If we are not using newline attribute then in the csv file blank lines will be included between data. To prevent these blank lines, newline attribute is required.

# Reading data from csv file:
# ----------------------------------------

import csv
f = open('emp.csv','r')
r = csv.reader(f)#Returns csv reader object
print(type(r))
data = list(r)
for line in data:
	for word in line:
		print(word,'\t',end='')
	print()

# Zipping and Unzipping files:
# -----------------------------------------
# -->The main advantages are:
# 	1).To improve memory utilization.
# 	2).We can reduce transport time.
# 	3).We can improve performance.
# -->To perform zip and unzip operations, python contains one in-built module zipfile. This module contains ZipFile class.

# To create zip file:
# --------------------------
# -->We have to create ZipFile class object with name of the zip file, mode and constant ZIP_DEFLATED. This constant represents we are creating zip file.
# 						f = ZipFile('files.zip','w',ZIP_DEFLATED)
# -->Once we created ZipFile object, we can add files by using write() method.
# 						f.write(filename)
	
from zipfile import *
f = ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('cricketers.txt')
f.write('heroes.txt')
f.write('social.txt')
print('files.zip file created successfully.....')

# To perform unzip operation:
# ------------------------------------------
# -->We have to create ZipFile object as:
# 					f = ZipFile('files.zip','r',ZIP_STORED)
# -->ZIP_STORED represents unzip operation. This is the default value and hence we are not required to specify.
# -->Once we create ZIpFile object for unzip operation, we can get all file names present in that zip file by using namelist() method.
# 					names = f.namelist()

from zipfile import *
f = ZipFile('files.zip','r',ZIP_STORED)
f.extractall()
names = f.namelist()
print(names)
for name in names:
	print('File Name:',name)
	print('The content in the file is:')
	f1 = open(name,'r')
	print(f1.read())
	print()

# Working with directories:
# -------------------------------------
# -->To know the current working directory.
# -->To create a new directory.
# -->To remove an existing directory.
# -->To rename a directory.
# -->To list content of directory.
# etc.............

# To perform these operations python provides in-built module:os, which contains several methods to perform directory related operations.

# Q.To know the current working directory
# --------------------------------------------------------------
import os
cwd = os.getcwd()
print('Current working directory:',cwd)

# Q.To create a sub directory in the current working directory
# -----------------------------------------------------------------------------------------
import os
os.mkdir('sunny')
print('My sub dir created cwd')

# Q.To create sub dir in sunny dir
# ------------------------------------------------
import os
os.mkdir('sunny/bunny')
print('My sub dir created inside sunny')

# Q.To create multiple dirs like sub1 in that sub2 in that sub3
# -----------------------------------------------------------------------------------------
import os
os.makedirs('sub1/sub2/sub3')
print('sub1 sub2 sub3 dirs created')

# Q.To remove a directory
# -------------------------------------
import os
os.rmdir('sunny/bunny')
print('bunny was deleted')

# Q.To remove sub directories
# ------------------------------------------
import os
os.removedirs('sub1/sub2/sub3')
print('All 3- directories sub1,sub2,sub3 removed')

# Q.To rename a directory
# -------------------------------------
import os
os.rename('sunny','bunny')
print('sunny renamed as bunny')