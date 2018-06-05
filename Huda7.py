import random

def getsecretnum(numdigits):
    secretnum = ''
    for i in range(numdigits):
        secretnum += random.choice('0 1 2 3 4 5 6 7 8 9'.split())

    return secretnum

def getclues(guess,secretnum):
    if (guess == secretnum):
        print('Congrats. You have done it.')


    clue = []

    for i in range(len(guess)):
        if (guess[i] == secretnum[i]):
            clue.append('Fermi')
        elif (guess[i] in secretnum):
            clue.append('Pico')
        if(len(clue)==0):
            return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isonlydigits(num):
    if num == '':
        return False

    for i in num:
        if (i not in '0 1 2 3 4 5 6 7 8 9'.split()):
            return False

        return True

def playagain():
    print ('Do you want to play again?')
    return input().lower().startswith('y')

Numdigits = 3
Maxguess = 10

print('I am thinking of a %s-digit number. Try to guess what it is' %(Numdigits))
print ('Here are some clues')
print('When I say:             That means ')
print(' Pico     :           one digit is correct but in the wrong position')
print('Fermi      : One digit is correct and in the right position')
print('Bagels :      No digits are correct')

while True:
    secretnum = getsecretnum(Numdigits)

    Numguesses = 1
    print('I have thought up a number. You have %s tries to get it' %(Maxguess))

    while(Numguesses <= Maxguess):
        guess = ''
        while (len(guess) != Numdigits or not isonlydigits(guess)):
            print('Guess #%s: ' %(Numguesses))
            guess = input()

        clue = getclues(guess,secretnum)
        print (clue)
        Numguesses += 1

        if (guess == secretnum):
            break
        if (Numguesses > Maxguess):
            print('You ran out of guesses')
        if (not playagain()):
            break
