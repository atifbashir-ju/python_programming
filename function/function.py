# # #A function is a group of statments performing a specific task.
# # when a program gets bigger in size and its complexity grows, it gets diifcult for a program to keeep track on which piece of code is doiing what
# # a function can be reused by the program ina given program any number of:

a = int (input("enter a number"))
b = int (input("enter a number"))
c = int (input("enter a number"))

avg = (a+b+c)/3
print(avg)



a = int (input("enter a number"))
b = int (input("enter a number"))
c = int (input("enter a number"))


avg = (a+b+c)/3
print(avg)

#now doing this using function:


def avg(): #function defination:

    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    c = int(input("enter a number: "))
    
    average = (a + b + c) / 3
    print(average)

avg() #function call:
avg()
avg()
avg()
avg()

# #quiz: WAP to greet a user with "Good day" using function:

def goodday():
    print("good day")

goodday()



def goodday(name):
    print("Good day, " + name)

goodday("Atif")

