#if else and elif statements are multiway decison by our program due hto certain conditions in our code

#IF ELSE:
a = int (input("enter a number:"))
if(a>=18):
    print("adult")
elif(a>=0):
    print("you are not born")

else:
    print("not adult")

num = int(input("enter a number :"))

if num % 2 == 0:
    print("even number ", num)
else:
    print("odd", num)


#I ELSE LEDDER:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2 and num1 >= num3):
    print("num1 is greatest:", num1)
elif (num2 >= num1 and num2 >= num3):
    print("num2 is largest:", num2)
else:
    print("num3 is largest:", num3)
    

