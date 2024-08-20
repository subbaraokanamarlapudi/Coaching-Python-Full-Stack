x = 333

def add(a,b):
    return a+b
def product(a,b):
    return a*b

def f1():
    if __name__ == '__main__':
        print('The code executed directly as a program')
        print('The value of __name__:',__name__)
    else:
        print('The code executed indirectly as a module from some other module')
        print('The value of __name__:',__name__)
f1()