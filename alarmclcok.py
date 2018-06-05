#this is a credit card validator

def fact (n):
    total = 1

    while n != 1:
        total = total*n
        n = n - 1
    return total

#print(fact(5))

def fact2(n):
    if n < 1:
        return 1
    else:
        return n*fact2(n-1)

print(fact2(5))