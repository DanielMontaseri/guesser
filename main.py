# Title: Random Number Guesser1
# Author: Daniel Montaseri
# Date: 09/14/2021
# Purpose: Have the user guess what number the program is thinking of

from random import randint

print('I am thinking of an integer from 1 to 10. You have three chances to guess what integer I am thinking of.')
randNumb = randint(1, 10)
guessCounter = 0
correct = False

while guessCounter < 3:
    userGuess = int(input('What number am I thinking of? '))
    guessCounter += 1
    if userGuess == randNumb:
        print('You beat me! Congratulations.')
        correct = True
        break
    else:
        print('Wrong!')
        print('Please try again.')

if not correct:
    print('Wrong!')
    print('The number was:', randNumb)
    print('Looks like I have won, better luck next time!')


