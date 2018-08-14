'''
Created on Aug 12, 2018

@author: Subhashis
'''

cart=[10,20,30,500,70,90,900,23,600]

for item in cart:
    if item>500:
        print("Sorry we can not process this item :" , item)
        continue
        
    print("Processing item :",item)
    
else:
    print("Congratulation all items are processed successfully ")