import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (S, W, G): ").upper()

youdict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youdict[youstr]

print("You chose:", reverseDict[you])
print("Computer chose:", reverseDict[computer])

if computer == you:
    print("It's a draw!")
elif (computer - you) in (-1, 2):
    print("You win!")
else:
    print("You lose!")
