num1 = int (input("enter first number :"))
num2 = int (input("enter second number:"))
num3 = int (input("enter third number :"))
num4 = int (input("enter fourth number :"))

if num1>num2 and num1>3 and num1>num4:
    print("num1 is largest", num1)
elif num2>num1 and num2>num3 and num2>4:
    print("num2 is largest", num2)
elif num3>num1 and num3>2 and num3>num4:
    print("num3 is largest", num3)
elif num4>num1 and num4>num2 and num4>num3:
    print("num4 is largest", num4)
else:
    print("you entered invalid number")
