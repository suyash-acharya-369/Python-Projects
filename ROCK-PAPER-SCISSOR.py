# ROCK PAPER SCISSOR GAME IN PYTHON :

import random

options = ('rock', 'paper', 'scissors')
player = None

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options :
        player = input('Choose between rock, paper, scissors : ')
    print(f'Computer chose : {computer}')

    if player==computer:
        print('It\'s a tie')
    elif player=='rock' and computer=='scissors':
        print('You Win!')
    elif player=='scissors' and computer=='paper':
        print('You Win!')    
    elif player=='paper' and computer=='rock':
        print('You Win!')
    else :
        print('You Lose!')  

        if not input('Select y to play agaian or else n :')  == 'y' :
            running = False

print('Thanks for Playing!')        

     


