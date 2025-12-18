n = int (input("Enter a number:"))
for i in range(1, 20):
    print(f"{n} * {i} = {n * i}")

#problem 2:

l = ["Atif", "banana", "apple"]

for name in l:
    if name.startswith(("A", "b")):
        print(f"hello {name}")
