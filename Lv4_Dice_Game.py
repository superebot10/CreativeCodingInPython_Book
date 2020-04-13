import time
number_dice = input('Enter number of dice: ')
number_dice = int(number_dice)
username = input('Enter username: ')
ready = input('Press any button to begin. ')
import random
def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice
user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls)
user_choices = input('Enter - to hold or r to roll again: ')
while len(user_choices) != number_dice:
    print('You must enter', number_dice, 'choices')
    user_choices = input('Enter - to hold or r to roll again: ')
def roll_again(choices, dice_list):
    print('Rolling again...')
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
roll_again(user_choices, user_rolls)
print(username, '\'s new roll: ', user_rolls)
print( username, '\'s first roll: ', user_rolls)
print('Computer\'s turn')
computer_rolls = roll_dice(number_dice)
print('Computer first roll: ', computer_rolls)
def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print('Computer\'s total: ', computer_total)
    print(username, '\'s total: ', user_total)
    if user_total > computer_total:
        print(username, ' wins')
    elif user_total < computer_total:
        print('Computer wins')
    else:
        print('Tie')
find_winner(computer_rolls, user_rolls)