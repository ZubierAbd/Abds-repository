from math import factorial

from decimal import Decimal, getcontext

n = int(input("How many digits of pi do you want to find?"))
getcontext().prec = n + 1

def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0

    t= (1)*(factorial(1))*(13591409 + 545140134*k)
    deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
    pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi

print(calc(n))

