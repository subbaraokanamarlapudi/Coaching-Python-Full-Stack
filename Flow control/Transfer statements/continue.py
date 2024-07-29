'''
* It is used within loops to skip the rest of the code inside the loop for the current iteration and move on to the 
  next iteration.
* This can be useful when you want to skip certain conditions or iterations without breaking the loop.
'''

#  Example - 01 ----> Basic program

for i in range(10):
    if i == 5:
        continue
    print(i)

# Example - 02 -----> We have to print the odd numbers by using continue.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Example - 03 -----> By using the for-if loop.

cart = [10,20,600,30,40,700,60,70]
for item in cart:
    if item >= 500:
        print("We cant process the item",item)
        continue
    print("We can process the item",item)

# Example - 04 -----> By using the for-if loop.

number = [10,20,0,5,0,25]
for n in number:
    if n == 0:
        print("We cant divide with zero",n)
        continue
    print('100/{}={}'.format(n,100/n))