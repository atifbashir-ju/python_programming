# #dictionary

# marks = {
#     "harry" : 100,
#     "atif" :  56,
#     "wasil": 12
# }

# print(marks, type(marks))

#method of dictionary
# 1st method
# marks = {
#     "harry" : 100,
#     "atif" :  56,
#     "wasil": 12
# }
# print(marks.items())

# 2nd method
# marks = {
#     "harry" : 100,
#     "atif" :  56,
#     "wasil": 12
# }
# print(marks.keys()) # keys means it will print names like atif, harry etc

#3rd method
marks = {
    "harry" : 100,
    "atif" :  56,
    "wasil": 12
}
print(marks.values()) #values means it will print 100, 50 etc..
marks.update({"harry": 99}) #now here value updated first was harry 100 now its 99
print(marks)
print(marks.get("harry")) #this will print directly harry marks which is 99

#empty dictonary
s = {}