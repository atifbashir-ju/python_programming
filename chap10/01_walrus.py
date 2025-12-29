#using walrus operator
if (n := len([1,2,3,4,5])) > 3:
    print(f"list is too long ({n} elements, expected <= 3)") #list is too long (5 elements, expected <= 3)
    

    #without walrus operator
    n = len([1,2,3,4,5])
if n > 10:
    print(n)
#with walrus operator
if (n := len([1,2,3,4,5])) > 10:
    print(n)

