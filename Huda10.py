#this is the test for the development of cryptography
#A-Z has ASCII numbers 65 to 90
#a-z has ASCII numbers 97-122
#chr() and Ord() are inverses of another. One takes number and gives ASCII and the other does the opposite

MAX_KEY_SIZE = 26 #remember the capitalized variables are known as global variables

def getmode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split(): #so basically the split makes this a list ['encrypt', 'e',....] so if mode in this list run this code
            return mode
        else:
            print("Either 'encrypt' or 'e' or 'decrypt' or 'd'")

def getmessage(): #this is a very simple function just takes the input - what does this input come out as?
    print('Enter the message that you want to encry'
          'pt')
    return input()

def getkey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' %(MAX_KEY_SIZE))
        key = int(input()) #key is a number that we take which shifts out cipher by that number of things
        if (key >=1 and key <= MAX_KEY_SIZE): #this function is a test making sure that we only take a logical number of steps
            return key

def gettranslatedmessage(mode, message, key):
    if mode[0] == 'd': #just checks if we are in decrypt mode or not
        key = -key
    translated = '' #we will append chars to this

    for symbol in message: #we can have any word here for symbol
        if symbol.isalpha(): #isalpha checks if the things are alphabets r not. will return True if so or False if not
            num = ord(symbol) #ord returns letter to number
            num += key #we add the key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num <ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getmode()
message = getmessage()
key = getkey()

print('Your translated message is : ')
print(gettranslatedmessage(mode,message,key))