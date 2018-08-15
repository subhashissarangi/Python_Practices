'''
Created on Aug 14, 2018

@author: Subhashis
'''


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
    
