import math

# def temp_converter(a):
#     x = input('Do you want to convert 1) F to C or 2) C to F?')
#     if x == '1':
#         temp = (a-32)*5/9
#         return temp
#     else:
#         temp = a*1.8 + 32
#         return temp
#
#
# print(temp_converter(30)


def goat():


    l1 = float(input('Please enter Latitude of City 1'))
    lo1 = float(input('PLease enter longitude of City 1'))
    l2 = float(input('Please enter Latitude of City 2'))
    lo2 = float(input('PLease enter longitude of City 2'))

    delx = (lo1-lo2)**2
    dely = (l1-l2)**2
    distance = (delx + dely)**0.5

    return distance

print(goat())
