print('Let us play with the Fibonacci rules')

#Fibonacci - next number is sum of preceding 2 numbers 1,1,2,3,5,8,13,21 ...

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


print(fib(5))