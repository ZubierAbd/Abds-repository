import random
import time

def displayIntro():
    print ('You are on a planet full of dragons. In front of you')
    print ('you see two caves. In one cave, the dragon is friendly. The other is not')
    print ('One will share his treasure with you. One will not.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go to?')
        cave = input()
        cave = str(cave)

    return cave

def CheckCave (chosencave):
    print('You approach the cave')
    time.sleep(2)
    print('it is dark and spooky')
    time.sleep(2)
    print('A large dragon awaits in front of the cave. It opens its mouth and')
    time.sleep(2)

    Fcave = random.randint(1,2)

    if(chosencave == str(Fcave) ):
        print('Gives you his treasure')
    else:
        print('Gobbles you in one bite')

playAgain = 'yes'
while (playAgain == 'yes' or playAgain == 'y'):
    displayIntro()
    cavenumber = chooseCave()
    CheckCave(cavenumber)
    print('Do you want to play again?')
    playAgain = input()







