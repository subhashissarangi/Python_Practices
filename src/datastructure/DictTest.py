'''
Created on Aug 14, 2018

@author: Subhashis
'''
from builtins import int


def studentVerification():
    studentRecords = {}
    num = input("Enter Number of students :")
    
    if num != "":
        n = int(num)
    else:
        return
    
    i = 1
    try:
        while i <= n:
            name = input("Enter Student Name : ")
            marks = input("Enter % of marks : ")
            studentRecords[name] = marks
            i = i + 1
        print("Name of Student " , "\t", "% Of marks")
        
        for x in studentRecords:
            print("\t", x, "\t\t", studentRecords[x])
    except ValueError:
        print("Failure w/ value " + n)
        
    
def charOccurrence():
    word = input("Enter some word :")
    d = {}
    
    for x in word:
        d[x] = d.get(x, 0) + 1
    
    for k, v in d.items():
        print("{} occurred {} times".format(k, v))
        
     
def charOccurrenceSorted():
    word = input("Enter some word :")
    d = {}
    
    for x in word:
        d[x] = d.get(x, 0) + 1
    
    for k, v in sorted(d.sorteditems()):
        print("{} occurred {} times".format(k, v))    
    
    
def checkNumberOfVowels():
    word = input("Enter some word :")
    vowels = {"a", "e", "i", "o", "u"}
    d = {}
    
    for x in word:
        if x in vowels:
            d[x] = d.get(x, 0) + 1
    
    for k, v in sorted(d.sorteditems()):
        print("{} occurred {} times".format(k, v))  
        
        
        
def storeStudentDetails():
    n=int(input("Enter how many student details you want to store :"))
    d={}
    
    for i in range(n):
        name=input("Enter Name :")
        marks=int(input("Enter marks :"))
        d[name]=marks
        i=i+1
        
    while True:
        name=input("Enter Student Name to get marks")
        marks=d.get(name, -1)
        
        if(marks==-1):
            print("Student not found")
            
        else:
            print("the marks of {} is {}".format(name, marks))
        option=input("Do you want to find another student:[YES | NO] ")
        
        if option=="NO":
            break
    print("Thanks for using our application ")
        
    
    
    
    
    
    
    
    
