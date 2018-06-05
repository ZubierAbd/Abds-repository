import random

print('Let us play hangman')

# words ='ant baboon badger bat bear beaver beetle bird camel cat clam cobra cougar coyote crab crane crow deer dog donkey duck eagle ferret fish fox frog goat goose hawk iguana jackal koala leech lemur lion lizard llama mite mole monkey moose moth mouse mule newt otter owl oyster panda parrot pigeon python quail rabbit ram rat raven rhino salmon seal shark sheep skunk sloth slug snail snake spider squid stork swan tick tiger toad trout turkey turtle wasp weasel whale wolf wombat worm zebra'.split()
words = ['ant', 'goat', 'pigeon']
guesses = 7

def getrandomword(wordlist):
    wordindex = random.randint(0,len(wordlist)-1)
    return wordlist[wordindex]

def board(missedletters,correctletters,secretword):
    print(guesses)
    print()
    print('Missed Letters')
    for letter in missedletters:
        print (letter)
    print()

    blanks = '_'*len(secretword)

    for i in range (len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]

    for letter in blanks:
        print (letter)
        print()

def GetGuess(alreadyguessed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyguessed:
            print('You have already guessed that')
            print('Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("please enter a letter faggot")
        else:
            return guess

def playagain():
    print ('Do you want to play again?')
    return input().lower().startswith('y')

print ('HANGMAN')
missedletters = ''
correctletters = ''
secretword = getrandomword(words)
gameisdone = False

while guesses != 0:
    board(missedletters,correctletters,secretword)

    guess = GetGuess(missedletters+correctletters)

    if guess in secretword:
        correctletters = correctletters + guess
        guesses = guesses - 1
        foundallletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundallletters = False
                break
            if foundallletters:
                print('Yes. the secret word is '+ secretword + 'You have won')
                gameisdone = True
                guesses = 0
            else:
                missedletters = missedletters + guess
                guesses = guesses - 1


if guesses == 0:
    print('You have failed after 7 guesses')
    print('Do you want to play again? ')