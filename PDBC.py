# '''
# * PDBC : Python DataBase Connection

# Python database programming:
# ------------------------------
# * Sometimes as the part of programming requirement we have to connect to the database and we have to perform several operations
#   like creating tables, inserted data, updating data, delete and select data etc....
# * We can use sql language to talk to the database and we can use python to send those sql commands to the database.

# Standard steps for python python DB programming:
# --------------------------------------------------

# * Step 1: import database sepcific module.
#     Ex:   import cx_Oracle

# * Step 2: Establish connection between python program and DB. we can create this connection object by using connect() function of the module.
#     EX:   con = cx_Oracle.connect(database info)

# * Step 3: To execute our sql queries and to hold results some special object is required, which is nothing but cursor object.
#           We can create cursor object by using cursor().
    
#     EX:  cursor = con.cursor()

# * Step 4: Execute SQL queries by using Cursor object.
# 			execute(sql quey)
# 			executescript(sql queries)
# 			executemany()

# * Step 5: commit and rollback changes based on our requirement in the case of DML Queries(insert|update|delete).
# 			commit():Saves the changes to the database.
# 			rollback():rolls all temporary changes back.

# * Step 6: Fetch the result from the Cursor object in the case of select queries.
# 			fetchone():To fetch only one record.
# 			fetchall():To fetch all rows in to a list.
# 			fetchmany(n):To fetch first n rows.

# * Step 7: Close the resources:
# 	After completing our operations it is highly recommended to close the resources in the reverse order of their opening by using close() method.
# 		cursor.close()
# 		con.close()

# * All methods which can be used for python DB programming:
#         connect(),cursor(),execute(),executescript(),executemany(),
# 	    commit(),rollback(),fetchone(),fetchall(),fetchmany(n), close()

# These methods wont be changed from DB to DB and same for all databases.


# Working with Oracle Database:
# -------------------------------
# * From the python program if we want to communicate with any database, some translator must be required to translate python calls into database specific calls
#   and database specific calls into python calls. This translator is nothing but driver/connection.

# * For Oracle database the name of driver is cx_Oracle.

# Installing cx_Oracle:
# 	go to command prompt:
# 		pip install cx_Oracle

# How to test installation:
# 	go to python shell:
# 		>>>help('modules')

# '''

# # EX - 1 : Program to connect with oracle database and print it's version
# # -----------------------------------------------------------------------------

# # SQL> select * from global_name;
# # GLOBAL_NAME
# # ----------------------
# # ORCL

# # EX: 

# import cx_Oracle
# try:
# 	con = cx_Oracle.connect('scott/tige@ORCL')
# 	print('Connection established successfully.....')
# 	print('Version:',con.version)
# except cx_Oracle.DatabaseError:
# 	print('Connection not established......')
	

# # Ex:w.a.p to create employee table in Oracle DB
# # ----------------------------------------------------------------------
# import cx_Oracle
# try:
# 	query="create table employee(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(20))"
# 	con = cx_Oracle.connect('scott/tiger@ORCL')
# 	cursor = con.cursor()
# 	cursor.execute(query)
# 	print('Table is created successfully...............')
# except cx_Oracle.DatabaseError as e:
# 	if con:
# 		con.rollback()
# 		print('There is a problem in sql:',e)
# finally:
# 	if cursor:
# 		cursor.close()
# 	if con:
# 		con.close()

# # Ex:w.a.p to drop employee table
# # -------------------------------------------------
# # query = "drop table employee"

# # Ex:To insert a single row in the employee table
# # ----------------------------------------------------------------------
# query="insert into employee values(101,'Sunny',12000,'Mumbai')"
# con = cx_Oracle.connect('scott/tiger@ORCL')
# cursor = con.cursor()
# cursor.execute(query)
# con.commit()
# print('Record inserted successfully...............')

# # Note:
# # 	while performing DML operations(insert | update | delete) we have to use commit() method, then only the result will be reflected in the database.

# # Ex:To insert multiple records to table by using executemany() method
# # ---------------------------------------------------------------------------------------------------------
# query="insert into employee values(:eno,:ename,:esal,:eaddr)"
# records = [(102,'Bunny',13000,'Hyd'),(103,'Chinny',14000,'Vja'), (104,'Vinny',15000,'Bng')]
# cursor.executemany(query,records)
# con.commit()
# print('Records are inserted successfully...............')

# # Ex:To insert multiple rows to the table with dynamic input from the keyboard
# # --------------------------------------------------------------------------------------------------------------------
# con = cx_Oracle.connect('scott/tiger@ORCL')
# cursor = con.cursor()
# while True:
# 	eno = int(input('Enter Employee Number:'))
# 	ename = input('Enter Employee Name:')
# 	esal = float(input('Enter Employee Salary:'))
# 	eaddr = input('Enter Employee Address:')
# 	sql = "insert into employee values(%d,'%s',%f,'%s')"
# 	cursor.execute(sql%(eno,ename,esal,eaddr))
# 	print('Record inserted successfully......')
# 	option = input('Do you want to insert one more record[Yes | No]:')
# 	if option == 'No':
# 		con.commit()
# 		break


# # W.A.P to update employee salaries with increment for the certain range with dynamic input
# # EX: Increment all employee salaries by 1200 whose salary < 15000

# con = cx_Oracle.connect('scott/tiger@ORCL')
# cursor = con.cursor()
# increment = float(input("Enter increment salary:"))
# salrange = float(input("Enter salary range:"))
# sql = 'update employee set esal = esal + %f where esal < %f'
# cursor.execute(sql%(increment,salrange))
# con.commit()

# # W.A.P to select all employees info by using fetchone() method?
# # ----------------------------------------------------------------

# con = cx_Oracle.connect('scott/tiger@ORCL')
# cursor = con.cursor()
# cursor.execute('select * from employee')
# row = cursor.fetchone()
# while row:
# 	print(row)
# 	row = cursor.fetchone()

# # w.a.p to select all employees info by using fetchall() method
# # ------------------------------------------------------------------------------------------
# cursor.execute("select * from employee")
# data = cursor.fetchall()
# for row in data:
# 	print('Employee Number:',row[0])
# 	print('Employee Name:',row[1])
# 	print('Employee Salary:',row[2])
# 	print('Employee Address:',row[3])
# 	print()

# # w.a.p to select employees info by using fetchmany() method and the required number of rows will be provided as dynamic input?
# # -------------------------------------------------------------------------------------------------------------------------------
# cursor.execute("select * from employee")
# n = int(input('Enter the number of required rows:'))
# data = cursor.fetchmany(n)
# for row in data:
# 	print(row)



# ---------------------------------------------------------------------------------Working With MYSQL ---------------------------------------------------------------------------

# Working with Mysql Database:
# ==========================
# Current version:8.0......
# Vendor:SUn Microsystems/Oracle corp
# Opensource and freeware
# Default port:3306
# Default user:root

# Note:
# 	In Mysql everything we have to wotk with our own databases, which are also known as logical databases.

# Commonly used commands in Mysql:
# --------------------------------------------------------
# 1.To know available databases:
# 		mysql>show databases;

# 2.To create our own logical database:
# 		mysql>create database maheshdb;

# 3.To drop database:
# 		mysql>drop database maheshdb;

# 4.To use a particular database:
# 		mysql>use maheshdb		or		mysql>connect maheshbd;

# Driver / connector information:
# ------------------------------------------------
# For Mysql database the name of driver is pymysql.

# How to install:
# 	pip install pymysql

# How to check installation:
# 	go to shell:
# 		>>>help('modules')

# w.a.p to create table,insert data and display data by using Mysql Database
# --------------------------------------------------------------------------------------------------------------
import pymysql
try:
	con = pymysql.connect(host='localhost', database='maheshdb', user='root', password='root')
	cursor = con.cursor()
	cursor.execute("create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
	print('Table is created.......')
	query = "insert into employees (eno,ename,esal,eaddr) values (%s,%s,%s,%s)"
	records = [(111,'Katrina',12000,'Mumbai'),(222,'Kareena',14000,'Hyd'),(333,'Deepika',18000,'Bng')]
	cursor.executemany(query,records)
	con.commit()
	print('Records are inserted successfully......')
	cursor.execute("select * from employees")
	data = cursor.fetchall()
	print(type(data))
	for row in data:
		print('Employee Number:',row[0])
		print('Employee Name:',row[1])
		print('Employee Salary:',row[2])
		print('Employee Address:',row[3])
		print()
except pymysql.DatabaseError as e:
	if con:
		con.rollback()
		print('There is a problem in sql:',e)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()

# Q.w.a.p to copy data present in employees table of Mysql DB into Oracle DB
# ------------------------------------------------------------------------------------------------------------------
# try:
# 	con = pymysql.connect(host='localhost', database='maheshdb', user='root', password='root')
# 	cursor = con.cursor()
# 	cursor.execute("select * from employees")
# 	data = cursor.fetchall()
# 	print(type(data))
# 	list = list(data)
# 	print(type(list))

# try:
# 	con = cx_Oracle.connect('scott/tiger@ORCL')
# 	cursor = con.cursor()
# 	query = "insert into employee values(:eno,:ename,:esal,:eaddr)"
# 	cursor.executemany(query,list)
# 	con.commit()
# 	print('Records copied from Mysql to Oracle DB successfully....')