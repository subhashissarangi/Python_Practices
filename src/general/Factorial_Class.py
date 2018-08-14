'''
Created on Aug 14, 2018

@author: Subhashis
'''

def countFactorial(arg):
    if arg == 0:
        return 1
    else:
        return arg * countFactorial(arg - 1)
    
def inputParameter():
    arg=int(input("Please Enter a Number : "))
    return arg