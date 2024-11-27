import random
# Define ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
# ● ┌ ─ ┐ │ └ ┘

" ┌───────────────┐ "
" │               │ "
" │               │ "
" │               │ "
" │               │ "
" └───────────────┘ "

dice_art = {
    1: (" ┌──────────────┐ ",
        " │              │ ",
        " │       ●      │ ",
        " │              │ ",
        " └──────────────┘ "),

    2: (" ┌──────────────┐ ",
        " │   ●          │ ",
        " │              │ ",
        " │           ●  │ ",
        " └──────────────┘ "),

    3: (" ┌──────────────┐ ",
        " │   ●          │ ",
        " │       ●      │ ",
        " │           ●  │ ",
        " └──────────────┘ "),

    4: (" ┌──────────────┐ ",
        " │  ●       ●   │ ",
        " │              │ ",
        " │  ●       ●   │ ",
        " └──────────────┘ "),

    5: (" ┌──────────────┐ ",
        " │   ●       ●  │ ",
        " │       ●      │ ",
        " │   ●       ●  │ ",
        " └──────────────┘ "),

    6: (" ┌──────────────┐ ",
        " │   ●       ●  │ ",
        " │   ●       ●  │ ",
        " │   ●       ●  │ ",
        " └──────────────┘ "),

}

dice = []
total = 0
print("Hello vijay ", f"{RED}")
num_of_dice = int(input("How Many Dice:"))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], f"{YELLOW}", end="")
    print()
for die in dice:
    total += die
print(f"total: {total}")
