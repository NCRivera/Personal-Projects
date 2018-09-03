#Since I want to have the choice between choices and randomizing, I'm importing
##random module.
import random

#I want to choose my class or have it randomized.
CLASSES = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

print('First - what class do you want your character to be?\n')

for cls in CLASSES:
    print(cls)

print('\nType one of the classes listed above. \nOr Type "Random" if you want '
      'a randomized class.')

playerClass = ''

# This while loop is killing me, I don't know how to continue if a person 
# enter an invalid string of text.
#while playerClass not in CLASSES:
while playerClass == '':
    playerClass = input()
    if playerClass == 'Random':
        playerClass = random.choice(CLASSES)
        print(f'OK, so the class I will choose is {playerClass}. Let\'s '
              'continue...')
        continue
    elif playerClass in CLASSES:
        print(f'OK, so {playerClass} is the class you chose. Let\'s '
              'continue...')
        continue
 #   elif playerClass not in CLASSES:
 #       playerClass = input('Try again: ')

print('<<<END>>>')


#Pending below--
#Alignment
#Ability Scores
#Character Details(i.e. gender, height, weight, etc.)
#IDEA: Create a NPC generator within? Something to think about.
