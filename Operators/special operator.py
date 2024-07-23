'''
1.Identity operators:
	We can use identity operators for address comparision. 2-identity operators are available.
							-->is
							-->is not
r1 is r2 returns True if both r1 and r2 are pointing to the same object.
r1 is not r2 returns True if both r1 and r2 are not pointing to the same object.

Ex:
	a = 10
	b = 10
	a is b #True
	a is not b #False
Ex:
	l1 = ['one','two','three']
	l2 = ['one','two','three']
	l1 is l2 #False
	l1 == l2 #True

Note:
	We can use is operator for address comparision where as == operator for content comparision.

2).Membership operator:
	We can use membership operators to check whether the given object present in the given collection.(It may be list,tuple,string....)

in==>Returns True if the given object present in the specified collection.
not in==>Returns True if the given object not present in the specified collection.

Ex:
	l = [10,20,30]
	30 in l #True
	50 in l #False
	50 not in l #True
	30 not in l #False

'''

#  Identity operator

print("----------Identity operator---------")
a = 10
b = 10
print(a is b)
print(a is not b)

l1 = ['one','two','three']
l2 = ['one','two','three']

print(l1 is l2)
print(l1 == l2)

# Membership operator

print("-------------Membership operator----------------")
l = [10,20,30]
print(30 in l)
print(50 in l)
print(50 not in l)
print(30 not in l)