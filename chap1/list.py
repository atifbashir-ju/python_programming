# A list is an ordered, changeable collection of elements. Lists allow duplicate values.
numbers = [10, 20, 30, 40]
names = ["orange", "apple", "Atif"]

# Accessing List Elements
print(numbers[0])
print(names[-1])

# Changing List Elements
numbers[1] = 25
print(numbers)

# List Methods
numbers.append(50)
numbers.insert(1, 15)
numbers.remove(30)
numbers.pop()
numbers.sort()
print(numbers)