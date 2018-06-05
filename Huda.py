import random
print ("Welcome to the Game!!")
print ("We will be creating a dice rolling simulator")
print("To exit the dice roller please write no")

answer = "yes"

while (answer != "no"):
    guess = random.randrange(1,20)
    print(guess)
    answer = input("Do you want to continue?")

print("Thank you for playing this game")
