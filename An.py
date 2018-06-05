num = int(input('Please enter a number'))

def next_prime_number(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
        return True

num = num + 1

while next_prime_number(num) == False:
    num = num + 1

print (str(num) + ' is your next prime')



