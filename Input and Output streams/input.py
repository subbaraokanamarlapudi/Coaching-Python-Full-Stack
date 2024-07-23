'''
INPUT:
* There are 2 functions are:
	1.raw_input()
	2.input()

1. Raw_input():
* This function always read the data from the keyword in the form of string format. 
* we have to convert that string type to our required type by using type casting methods.

2. Input():
* It is a function can be used to read data directly in our required format.
* we are not required to perform the type casting.

Note:
* But in python-3 version we have only input() method and raw_input() method is not available.
* python-3 input() function behaviour exactly same as raw_input() method in python-2 i.e every input value is treated as str type only.

'''

# w.a.p to read 2 numbers from the keyboard and print the sum.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("The sum is:" , n1+n2)

# w.a.p to read employee data from the keyboard and print the table.

eno = int(input("Enter employee number: "))
ename = input("Enter employee name: ")
esal = float(input("Enter employee salary: "))
eaddr = input("Enter employee address: ")
married = input("Employee married? (True/False): ")

print("----------------------------------------------------------------Employee information is ----------------------------------------------------")
print("Employee number: ", eno)
print("Employee name: ", ename)
print("Employee salary: ", esal)
print("Employee address: ", eaddr)
print("Employee married: ", married)

'''
COMMAND LINE ARGUMENTS:
* The arguments which are passing at the time of execution are called as command line arguments.
 Example : D:\Coaching-Python-Full-Stack\input and Output> py.input.py 

* withinn the python program this command line args are available in "argv". which is present in "sys" module.
* The type of arg is not an array it is a list.

Note:
* argv[0] represents name of the program,but not the first command line argument.
* argv[1] represents first command line argument.
* argv[2] represents second command line argument.

Example:
* from sys import argv
print(type(argv))

'''

# basic program

from sys import argv
print(type(argv))

# w.a.p to display the command line arguments

from sys import argv
print('The number of command line args: ', len(argv))
print('The list of command line args: ', argv)
print("command line args one by one:")

for i in argv:
    print(i)

# sum of the command line arguments.

from sys import argv
sum = 0
args = argv[1:]
for i in args:
	sum += eval(i)
print('The sum is:',sum)


'''
NOTE :
* Usally space is separator between command line arguments.
* If your command line args itself contains space then we should enclose within double quotes[but not in single quote].
'''

from sys import argv
print(argv[1])