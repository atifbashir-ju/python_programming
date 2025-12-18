# #while loop: in while loop condition is checked first. if it evalutes to true, the body of the loop is excuted otherwise not.


i = 1
while(i<6):
    print(i)
    i+=1
# #problem: WAP to print your name 50 time
i = 0
while(i<51):
    print("Atif")
    i+=1

#content of list using while loop:
l = ["atif", "orange", "ayan", "chapter", "banana"]
i = 0
while(i<len(l)):
    print(l[i])
    i += 1

    #for loop: is used to iterate through a sequence like list, tuple or string..

#iterate in list:
l = [1, 2, 34, 56, 778]
for i in l:
    print(i)

    #iterate in tuple:
t = (1, 23 ,45, 56, 65)
for i in t:
    print(i)

    #iterate in string:
    s = ("atif", "ayan", "orange", "apple", "banana")
for i in s:
    print(i)

#for loop with else:
i = [1, 2, 3, 4]
for item in i:
    print(item)
else:
    print("done") # this is printed when the loop exhausts

#break statement is used to come out of the loop.

for i in range (100):
    if(i == 2):
        break #exit the loop it will stop at 2
    print(i)

#continue statment:
for i in range (100):
    if(i==56):
        continue #skip this iteration
    print(i)

    #pass statment: pass is a null statment in python
    