def ishappy(n):
    list = []
    while True:
        str_number = str(n)
        r = 0
        for i in str_number:
            r += (int(i)*int(i))
        if r == 1:
            return print('This is a happy number')
            list.append(n)
        else:
            return print('This is not a happy number')
        n = r

ishappy(1)
ishappy(7)
ishappy(8)
ishappy(10)
