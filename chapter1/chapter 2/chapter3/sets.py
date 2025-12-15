#set is collection of well defined elements
# s = {1, 2, 3,} #in set the same element will never be repeated

# e = set() #empty set

# print(s)

#methods od set
# s.add(4)
# print(s)

#sets are unorderd
#sets are unindexed 
#there is no way to change items in sets
#sets cannot contain duplicate values
# s = {1, 2, 3,}
# print(s)
# s.remove(1)
# print(s)
# s = {1, 2, 3,}
# print(s)
# s.pop() #pop removes random value
# print(s)

# s = {1, 2, 3,}
# print(s)
# s.clear() #it will make empty set
# print(s)

s1 = {1, 2, 3, 78}
s2 = {90, 78, 67}
print(s1.union(s2))
print(s1.intersection(s2)) #intersection find common value