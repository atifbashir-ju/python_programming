import time
import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


santa = "🎅"

for i in range(25, 0, -1):
    clear()
    print("\n" * 5)
    print(" " * i + santa * 5)
    time.sleep(0.15)

# Santa message
clear()
print("\n" * 6)
print(" " * 20 + "🎅  HO HO HO!  🎅")
time.sleep(1)
print(" " * 16 + "🎄  MERRY CHRISTMAS  🎄")
time.sleep(2)


stars = ["⭐", "✨", "💫"]
lights = ["🔴", "🟡", "🔵", "🟢", "🟣", "✨"]
snow = ["❄️", "❆", "✨"]
gifts = ["🎁", "🧸", "🍫", "🎉", "🎀"]

width = 60
height = 30

while True:
    clear()

    # STAR
    print(" " * width + random.choice(stars))

    # TREE
    for i in range(1, height):
        space = " " * (width - i)
        line = "".join(random.choice(lights) for _ in range(2 * i - 1))
        print(space + line)
        time.sleep(0.04)

    # STEM
    for _ in range(4):
        print(" " * width + "🟫🟫🟫")
        time.sleep(0.05)

    # GIFTS
    print("\n" + " " * (width - 10) + " ".join(random.choice(gifts) for _ in range(8)))
    time.sleep(0.6)

    # SNOWFALL
    for _ in range(12):
        snow_line = "".join(
            random.choice(snow) if random.random() > 0.7 else " "
            for _ in range(80)
        )
        print(snow_line)
        time.sleep(0.15)

    # BLINK MESSAGE
    for _ in range(2):
        clear()
        print("\n\n" + " " * (width - 10) + "🎄🎁  MERRY CHRISTMAS  🎁🎄")
        time.sleep(0.6)
        clear()
        time.sleep(0.3)
