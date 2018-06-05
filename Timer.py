import random

import time

def survive():
    a = random.randint(0,1)

    if ( a == 0):
        return 'have Survived'
    else:
        return 'Did not make it. Better luck next time'


print('Let us find out if you have survived the wrath of Thanos')
name = input('What is your name?')
time.sleep(1)
print('Let us see here')
time.sleep(2)
print('No, that guy is not you. He is definitely dead')
time.sleep(2)
print ('All right ' + name + ' It looks like you ' )
time.sleep(2)
print(survive())

