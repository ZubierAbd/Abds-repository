print('Welcome to the mortgage calculator')
print('We will require the following things from you 1. Principal (P) 2. Number of monthly payments (N) 3. rate of monthly interest ')

P = int(input('Please enter the principal amount'))
#P = 200000
N = int(input('Please enter the number of monthly payments'))
#N = 360
r = (int(input('Please enter the rate per annum')))/(12*100)
#r = (6.5/12)/100

print(P)
print(N)
print(r)

print('Now we will calculate the mortgage')

def mortgage(P,N,r):

    mort = (r*P*(1+r)**N)/(((1+r)**N)-1)

    return mort

print('Your monthly payment is ' + str(mortgage(P,N,r)))
