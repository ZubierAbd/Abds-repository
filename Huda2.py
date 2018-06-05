import random

print("Guess the number game")

print("In this game we will be trying to guess a number between 1 and 20")

number = random.randrange(1,20)

guess=input("Please type a number")
print("Your guess is " + guess)

# print(type(guess))
# print(type(int(guess)))
# print(type(number))
# print(number)


guessi = int(guess)

while(guessi != number):
    if(guessi<number):
        print("your guess is too low")
        guess = input("Guess again")
        guessi = int(guess)
    if (guessi > number):
        print("your guess is too high")
        guess = input("Guess again")
        guessi = int(guess)

if(guessi == number):
    print("Yes you got it right")