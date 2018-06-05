# try:
#     f = open('testfile','w')
#     f.write = ("Write a test line")
# except TypeError:
#     print("There was a type error")
# except OSError:
#     print("Hey you have an OS error ")
# finally:
#     print('I always run')

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('You have an error')

try:
    x = 5
    y = 0
    z = x/y
except:
    print("you cannot divide by zero")


def ask():

    while True:
        try:
            n = int(input('Enter a number'))
        except:
            print('Please try again \n')
            continue
        else:
            break

    print("Y")
    print(n**2)