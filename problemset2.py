#question: can we have a set with (int) and "18"(str) as a value in it ? ans yes.
s = set()
s.add(18)
s.add("18")
print(s)

# question: what will be length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# #question: s = {}. what is the type of "s"?
s = {}
print(type(s))
#the type of "s" is dict..

#question: create an empty dictionary . Allow 4 friends to enter their favorite language as value and use  key as their names. Assure that the name are unique
d = {}
name = input("enter friends name")
lang = input("enter language name:")
d.update({name: lang})
name = input("enter friends name")
lang = input("enter language name:")
d.update({name: lang})
name = input("enter friends name")
lang = input("enter language name:")
d.update({name: lang})
name = input("enter friends name")
lang = input("enter language name:")
d.update({name: lang})
print(d)


