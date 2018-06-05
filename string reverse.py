def reverse(string):
    return print(string[::-1])


def palindrome(word):
    word = word.lower()
    if (word[::-1] == word[::1]):
        return True

print(palindrome('Dad'))


def vowels_count(string):
    count = 0
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count

print(vowels_count('Samara'))

def stringcount(string):
    return len(string.split())

print('the length of the string is ' + str(stringcount('THIS IS A BIG BIG SENTENCE')))