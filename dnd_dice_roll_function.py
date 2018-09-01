import random

def roll_dice(sides, rolls):
    for roll in range(rolls):
        score = random.randint(1,sides)
        print(score)

dice_sides = int(input("How many sides does your dice have? "))
roll_number = int(input("How many rolls do you want to make? "))

roll_dice(dice_sides,roll_number)
