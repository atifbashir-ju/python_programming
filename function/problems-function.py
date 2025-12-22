def goodday(name, endging):
    print("good day, " + name)
    print(endging)

    return 7  # this value will be returned

a = goodday("Atiif", " thank you")
print(a)


#default parameter value:
#we can have a value as default argument in a function
#if we specify name = "stranger" in the line containing def, this value is used when no longer arduments is passed 
#exmaple:

def gooday(name, ending="stranger"):
    print(f"Good day, {name} {ending}") #ending will print "stranger"

gooday("Atif")
