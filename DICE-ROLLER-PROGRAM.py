# DICE ROLLER PROGRAM :

import random

# Unicode characters :
# print('\u25cf    \u250c   \u2500   \u2510   \u2502   \u2514   \u2518')  # ●    ┌   ─   ┐   │   └   ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total=0
num_of_dice = int(input('Enter number of dices :'))

for die in range(num_of_dice):
        dice.append(random.randint(1,6))

# For horizontal dice print :
for line in range(5):
        for die in dice:
                print(dice_art.get(die)[line], end = '')
        print()

# for die in range(num_of_dice):
#         for line in dice_art.get(dice[die]):
#                 print(line)

for die in dice:
        total+=die
print(f'Total : {total}')