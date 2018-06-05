#this program will try to find the prime factors of a number

from itertools import count

def primefact(n):

    factors = []
    for i in count(2):
        while n % i == 0:
            factors.append(i)
            n //= i
        if 2*i > n:
            return factors

print(primefact(119))
