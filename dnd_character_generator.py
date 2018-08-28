#Since I want to have the choice between choices and randomizing, I'm importing random module.
import random

#I want to choose my class or have it randomized.
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

print('First - what class do you want your character to be?\n')

for cls in classes:
    print(cls)

print('\nType one of the classes listed above. \nOr Type "Random" if you want a randomized class.')

player_class = ''

while player_class == '':
    player_class = input()
    if player_class == 'Random':
        player_class = random.choice(classes)
        print(f'OK, so the class I will choose is {player_class}. Let\'s continue...')
        continue
    elif player_class in classes:
        print(f'OK, so {player_class} is the class you chose. Let\'s continue...')
        continue

print('<<<END>>>')


#Pending below--
#Alignment
#Ability Scores
#Character Details(i.e. gender, height, weight, etc.)
#IDEA: Create a NPC generator within? Something to think about.