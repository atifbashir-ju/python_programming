marks = int(input("Enter students marks:"))

if(marks>=100):
    print("Grade A+", marks)
elif(marks>=90):
    print("Grade A", marks)
elif(marks>=70):
    print("Grade B", marks)
elif(marks>=60):
    print("Grade c", marks)
elif(marks>= 50):
    print("Grade B", marks)
else:
    print("Fail", marks)
