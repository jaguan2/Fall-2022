#Jason Guan
#U9893-2926

#Code intended to emulate the game "The Price is Right" where four contestants
#bid prices to try matching or get closest the randomized number generated.

import random

RandomNumber = random.randint(1000,5000)
print(RandomNumber)

Player1 = int(input('Player 1, what is your bid? '))
Player2 = int(input('Player 2, what is your bid? '))
Player3 = int(input('Player 3, what is your bid? '))
Player4 = int(input('Player 4, what is your bid? '))

#If every player overbids
if Player1 > RandomNumber and Player2 > RandomNumber and Player3 > RandomNumber and Player4 > RandomNumber:
    print('Buzz! Aww... everyone has overbid!')
    exit()

#If a player guessed the generated number
elif Player1 == RandomNumber or Player2 == RandomNumber or Player3 == RandomNumber or Player4 == RandomNumber:

    if Player1 == RandomNumber: 
        print('Ding Ding Ding! One player got it exactly right and gets $500.')
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print('Player 1, come on up.')
        print()
        exit()
    
    elif Player2 == RandomNumber:
        print('Ding Ding Ding! One player got it exactly right and gets $500.')
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print('Player 2, come on up.')
        print()
        exit()

    elif Player3 == RandomNumber:
        print('Ding Ding Ding! One player got it exactly right and gets $500.')
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print('Player 3, come on up.')
        print()
        exit()

    else:
        print('Ding Ding Ding! One player got it exactly right and gets $500.')
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print('Player 4, come on up.')
        print()
        exit()

#Choose player with closest value wins
        
elif Player1 < RandomNumber or Player2 < RandomNumber or Player3 < RandomNumber or Player4 < RandomNumber:

    if (Player1 - RandomNumber) < (Player2 - RandomNumber) and (Player1 - RandomNumber) < (Player3 - RandomNumber) and (Player1 - RandomNumber) < (Player4- RandomNumber):
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print(f'Congratulations, Player 1 wins.')
        print()
        exit()
    
  
    elif (Player2 - RandomNumber) < (Player1 - RandomNumber) and (Player2 - RandomNumber) < (Player3 - RandomNumber) and (Player2 - RandomNumber) < (Player4 - RandomNumber):
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print(f'Congratulations, Player 2 wins.')
        print()
        exit()
    
    elif (Player3 - RandomNumber) < (Player1 - RandomNumber) and (Player3 - RandomNumber) < (Player2 - RandomNumber) and (Player3 - RandomNumber) < (Player4 - RandomNumber):
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print(f'Congratulations, Player 3 wins.')
        print()
        exit()

    else:
        print('Actual price is ${:.0f}.'.format(RandomNumber))
        print(f'Congratulations, Player 4 wins.')
        print()
        exit()

