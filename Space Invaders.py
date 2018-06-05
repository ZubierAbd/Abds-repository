choice = input('Do you want to convert a number to binary or hex?').lower()
number = int(input('Please enter a number'))
if choice == 'h':
    print(hex(number))
elif choice == 'b':
    print(bin(number))
else:
    print('Please enter a proper number')
