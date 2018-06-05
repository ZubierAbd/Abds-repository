import random
import time

name = ''
hp = 100

enemies = 'troll, ogre, witch, hitler'.split()

def wait():
    time.sleep(2)

def intro():
    print('Let us go on an adventure')
    name = input('What is your name, traveller?')
    print('Ahh so your name is ' + name)
    wait()
    print('I have heard of you and your tales on the lips of those who have long passed by. I wonder if the rumors are true.')
    wait()
    print('Let me ask you a moral question traveller and perhaps we can see your mettle')
    wait()
    print('You are walking down a long and lonesome road. Ahead of you there are two forks. Which fork do you choose?')

def choice():
    choiceA = ''
    choiceA = input('Do you choose left or right?')

    if (choiceA == 'Left' or 'L'):
        print('Ahead of you there lies a small hut, inside of which you can see a light')

intro()
