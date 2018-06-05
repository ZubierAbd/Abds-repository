print("CHANGE CALCULATOR")

quarter = 25
dime = 10
nickel = 5
penny = 1

moneygiven = int(input('Enter how much money you were given'))
citem = int(input('How much was the cost'))
moneygiven = int(float(moneygiven)*100)
citem = int(float(citem)*100)
moneyback = moneygiven - citem

qmb = moneyback/quarter
partialtotal = moneyback - qmb * quarter
dmb = partialtotal // dime
dpartialtotal = partialtotal - dmb * dime
nmb = dpartialtotal // nickel
npartialtotal = dpartialtotal - nmb * nickel
pmb = npartialtotal // pmb
ppartialtotal = npartialtotal - pmb * penny

print('You need %s quarters, %s dimes, %s nickels, %s pennies ' %(qmb,dmb,nmb,pmb))