'''
Created on Aug 15, 2018

@author: Subhashis
'''


def calc(arg1, arg2):
    add = arg1 + arg2
    sub = arg1 - arg2
    mul = arg1 * arg2
    div = arg1 / arg2
    
    return add, sub, mul, div

'''def values():
    i=eval(input("enter value 1:"))
    j=eval(input("enter value 2:"))
    return i,j'''

# print(calc(arg2=10, arg1=20))
# print(calc(arg1=10, arg2=20))

# print(calc(100,arg2=10))
# calc(arg2=100,10)  positional argument followed by keyword argument exception
# calc(100,arg1=10)  multiple values for arg1 exception TypeError


def addNumbers(*n):
    for x in n:
        x = x + x
     
    print(x)
    
# print(addNumbers(10,20,30,40))


def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial((n - 1))
    return result

# print(factorial(5))

s = lambda n : n * n


l=[10,20,5,7,2,8,7,70,90,33,45]

l1=list(filter(lambda x:x%2==0,l))
print(l1)

l2=list(filter(lambda x:x%2!=0,l))
print(l2)

























