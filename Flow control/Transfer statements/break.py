'''
* We can break statements inside loops to break loop execution based on some condition.
* It is used to control the sequence of the loop. Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that. 
* A typical scenario of using the Break in Python is when an external condition triggers the loop's termination.
'''

# Example 1: Break statement 

for i in range(10):
    if i == 5:
        break
    print(i)

# Example 2: Break statement in for loop

cart = [10,20,30,40,600,70,80]
for item in cart:
    if item > 500:
        print('To place this order insurance is required')
        break
    print(f'Processing item {item}')


# Example 3: Break statement in while loop

cart = [10,30,44,50,300,1000,60,70]
count = 0
i = 0
while i < len(cart):
    count += cart[i]
    if count > 500:
        print('To place this order insurance is required')
        break
    i += 1

if count <= 500:
    print('Order can be placed')


