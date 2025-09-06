import random

while True:
    sides = input("Enter number of sides on the dice btw 2 and 24 (or 'q' to quit): ")
    if float(sides) < 1:
        break
    if sides.lower() == 'q':
        break
    if not sides.isdigit():
        print("Enter a valid number.")
        continue
    roll = random.randint(1, int(sides))
    print(f"You rolled a {roll}")