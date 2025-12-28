import random

print(" Welcome to the Number Guessing Game")

# Difficulty selection
print("\nChoose difficulty:")
print("1. Easy (1–50, 10 attempts)")
print("2. Medium (1–100, 7 attempts)")
print("3. Hard (1–200, 5 attempts)")

choice = int(input("Enter your choice: "))

if choice == 1:
    max_num = 50
    max_attempts = 10
elif choice == 2:
    max_num = 100
    max_attempts = 7
else:
    max_num = 200
    max_attempts = 5

number = random.randint(1, max_num)
attempts = 0

while attempts < max_attempts:
    guess = int(input(f"\nGuess the number (1 to {max_num}): "))
    attempts += 1

    if guess > number:
        print("Lower number please")
    elif guess < number:
        print("Higher number please")
    else:
        print(f"\n Correct! You guessed it in {attempts} attempts")
        break
else:
    print(f"\n Game Over! The number was {number}")

print("\nThanks for playing!")

