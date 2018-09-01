import random

#This was my first attempt but I figured I could simplify it more. See line 20.
# def dice_roll(d, n):
#     for r in range(n):
#         if d == 20:
#             x = random.randint(1,20)
#         elif d == 12:
#             x = random.randint(1, 12)
#         elif d == 10:
#             x = random.randint(1, 10)
#         elif d == 8:
#             x = random.randint(1, 8)
#         elif d == 6:
#             x = random.randint(1, 6)
#         else:
#             x = random.randint(1, 4)
#         print(x)

#dice_roll(10,5)

def roll_dice(sides, rolls):
    for roll in range(rolls):
        score = random.randint(1,sides)
        print(score)

#roll_dice(10, 10)


dice_sides = int(input("How many sides does your dice have? "))
roll_number = int(input("How many rolls do you want to make? "))

roll_dice(dice_sides,roll_number)