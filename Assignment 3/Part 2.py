#Jason Guan
#U9893-2926
#Program intended to simulate a 1-100 guessing game with 10 attempts

import random

number = random.randint(1, 100)

guess = int(input('Enter a number between 1 and 100(inclusive):'))
while guess > 100 or guess < 1:
    guess = int(input('Very funny. Enter a number between 1 and 100 (inclusive):'))

numGuess = 1

while numGuess < 10:
    if guess == number:
        print(f'You guessed it right!! You got it in {numGuess} guesses!')
        break
    elif guess > number:
        guess = int(input('Too high. Enter another guess:'))
        numGuess += 1
    else:
        guess = int(input('Too low. Enter another guess:'))
        numGuess += 1

while numGuess == 10:
    print(f'Sorry, the number was {number}')
    break


    

