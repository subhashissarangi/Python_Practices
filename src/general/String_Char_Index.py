stng = input("Please enter String")
i=0
for x in stng:
    print("positive index of the character {} and negative index of character {} and the character is {}  ". format(i,i-len(stng), x))
    i=i+1
