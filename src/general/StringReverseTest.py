'''
Created on Aug 13, 2018

import operator

@author: Subhashis
'''
''' Reverse String 
 Given String= "hello how are you"
 Given String2= "B1D4A1" // Alphanumeric string
 
 OUTPUT:
 
 1. uoy era woh olleh             2. you are how hello
 
 3. olleh woh era uoy             4. Print charectar's at odd position and even position
 
 5. in String2 separate alphabets from numbers with sorted format
 
 '''
# 1 uoy era woh olleh 
 
# 2 you are how hello

 
# 3 olleh woh era uoy  
def reversedString():
    myString3 = input("Enter a String :")
    l = myString3.split()
    l1 = []
     
    for x in l:
        l1.append(x[::-1])
        output = " ".join(l1)
    print(output)

# 4 Print charectar's at odd position and even position
# With slice operator


def reverseStringWithSliceOperator():
    myString4 = input("Enter String to see the odd position and even position :")
    print("Characters at even position :" , myString4[::2], sep="_")
    print("Characters at odd position :" , myString4[1::2], sep="_")


# Without slice operator
myString5 = input("Enter String to see the odd position and even position :")
index = 0

print("Even positioned characters are : ")
while index < len(myString5):
    print(myString5[index], end=" ")
    index += 2

print("Odd positioned characters are : ")
while index < len(myString5):
    index = 1
    print(myString5[index], end=" ")
    index += 2

# 5 String 5: Separate alphabets from numbers with sorted format


def reverseString5():
    myString5 = input("Enter Alphanumeric String :")
    s1 = s2 = output = ""
    for x in myString5:
        if x.isalpha(myString5):
          s1 = s1 + x
        else:
          s2 = s2 + x
        
    for x in sorted(s1):
          output = output + x
    for x in sorted(s2):
          output = output + x
     
