'''
* It is used to perform Bitwise calculations on integers.
* The integers are converted into binary format and then operations are performed bit by bit.
* It works on integers only and the final output is returned in the decimal format.

------------------------------
			&, |, ^, ~, <<,  >>

0 & 0==>0			0 | 0==>0			0 ^ 0==>0
0 & 1==>0			0 | 1==>1			0 ^ 1==>1
1 & 0==>0			1 | 0==>1			1 ^ 0==>1
1 & 1==>1			1 | 1==>1			1 ^ 1==>0

&==>If both bits are 1 then only result is 1 otherwise 0.
|==>If atleast one bit is 1 then the result is 1 otherwise result is 0.
^==>x-or==.If bits are differentr then only result is 1 otherwise result is 0.
~==>Bitwise complement operator

Ex:
	4 & 5 #4
	4 | 5 #5
	4 ^ 5 #1
	~4 #-5

<<(left shift operator):
---------------------------------
	10<<2 #40

>>(Right shift operator):
-----------------------------------
	10>>2 #2

~ --> -(n+1)

'''

print(0&0)
print(0&1)
print(1&0)
print(1&1)
print(~0)
print(0 | 1)
print(1 | 0)
print(1 | 1)
print(0^0)

print(True & False)
print(True | False)
print(True ^ False)
print(~True)
print(~False)
print(True << 2)
print(True >> 2)