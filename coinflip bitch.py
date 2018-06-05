import random

n = 10000
heads = 0
tails = 0
i = 0
while i < n:
    if random.randint(0,1) == 1:
        heads += 1
        i +=1
    else:
        tails += 1
        i += 1

print('The number of heads is {}'.format(heads))
print('The number of tails is {}'.format(tails))



