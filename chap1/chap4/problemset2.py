marks1 = int (input("enter Marks 1 :"))
marks2 = int (input("enter Marks 2 :"))
marks3 = int (input("enter Marks 3 :"))

#now check for total percentage:
total_percentage =(100*( marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("pass", total_percentage)
else:
    print("fail",total_percentage)