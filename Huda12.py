# # st = 'Print only the words that start with s in this sentence'.split()
# #
# # for word in st:
# #     if word[0].lower() == 's':
# #         print(word)
# #
# #
# # for i in range(10):
# #     print(i)
# #
# # print('THis is the next one ')
# # for i in range(1,50):
# #     if i % 3 == 0:
# #         print(i)
# #
# # st = 'Print every word in this sentence that has an even number of letters'
# # st2 = st.split()
# #
# # for word in st2:
# #     if len(word) % 2 == 0:
# #         print(word)
# #         print(len(word))
# #
# # for i in range(1,100):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print('Fizz Buzz')
# #         print(i)
# #
# #     elif i % 5 == 0:
# #         print('Buzz')
# #
# #     elif i % 3 == 0:
# #         print('Fizz')
# #
# # st3 = 'Create a list of the first words in each of the words in this string'
# # st3 = st3.split()
# # final = []
# #
# # for word[0] in st3:
# #     final.append(words[0])
# #
# # print(final)
# #
# #
# # def piglatin(word):
# #     first_letter = word[0].lower()
# #     if first_letter in 'aeiou':
# #         return word + 'ay'
# #     else:
# #         return word + word[0].lower() + 'ay'
# #
# # print(piglatin('Chipmunk'))
# #
# # def bigsentence(string):
# #     string = string.split()
# #     for word in string:
# #          print(piglatin(word))
# #
# # bigsentence('The quick brown fox jumped over the lazy dog')
#
# # def myfunc(string):
# #     new = ''
# #     for i in string:
# #         if i % 2 == 0:
# #             new.push(string[i].lower())
# #         else:
# #             new.push(string[i].upper())
# #     return new
# #
# # myfunc
# #
# # def lesseroftwoevens(a,b):
# #     if a%2 == 0 and b%2 == 0:
# #         if a > b:
# #             return b
# #         else:
# #             return a
# #     else:
# #         if a > b:
# #             return a
# #         else:
# #             return b
# #
# # print(lesseroftwoevens(2,4))
# # # print(lesseroftwoevens(2,5))
# #
# # def animal_crackers(string):
# #     new = string.split()
# #     if new[0][0] == new[1][0]:
# #         print ('Works ')
# #     else:
# #         print ('Does not')
# #
# # animal_crackers('Lucky jlama')
#
# # def othersideofseven(a):
# #     diff = 7 - a
# #     return 7 + 2*diff
# #
# # print(othersideofseven(4))
#
# def makestwenty(a,b):
#     if a == 20 or b == 20:
#         return True
#     elif a + b == 20:
#         return True
#     else:
#         return  False
#
# print(makestwenty(18,1))
# # print(makestwenty(20,2))
# # print(makestwenty(18,2))
# # print(makestwenty(19,2))
# #
# # def oldmacdonald(name):
# #    first_letter = name[0]
# #    inbetween = name[1:3]
# #    fourth_letter = name[3]
# #    rest = name[4:]
# #
# #
# #    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
# #
# # print(oldmacdonald('Samarta'))
# #
# # def masteryoda(text):
# #     wordlist = text.split()
# #     reversed_wordlist = wordlist[::-1]
# #     return ' '.join(reversed_wordlist)
# # print(masteryoda('I am a god'))
# #
# # def almost_there(n):
# #     if abs(100 - n) or abs(200 - n):
# #         return True
# #     else:
# #         return False
# #
# # print(almost_there(104))
#
# # def has_33(list):
# #
# #     for i in range(0,len(list)-1):
# #         if list[i]== 3 and list[i+1] == 3:
# #             return True
# #
# #     return False
# #
# # has_33([1,2,3,3])
#
# def paperdoll(text):
#     result = ''
#     for char in text:
#         result += char*3
#     return result
#
# print(paperdoll('Samara'))
#
#
# def blackjack(a,b,c):
#     if sum([a,b,c]) <= 21:
#         return sum([a,b,c])
#     elif 11 in [a,b,c] and sum([a,b,c] <= 31):
#         return sum([a,b,c]) - 10
#     else:
#         return 'BUST'
#
# print(blackjack(18,3,4))
#
# def summerof69(arr):
#     total = 0
#     add = True
#
#     for num in arr:
#         while add:
#             if num!= 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#     return total
#
# print(summerof69([1,2,3,4,6,9,4]))
#
# def spygame(nums):
#     code = [0,0,7,'x']
#
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 1
#
# print(spygame([1,2,3,0,0,7]))
#

# def count_primes(num):
#     if num <2:
#         return 0
#     primes = [2]
#     x = 3
#
#     while x <= num:
#         for y in range(3,x,2):
#             if x%y == 0:
#                 x +=2
#                 break
#         else:
#             primes.append(x)
#             x+=2
#     print(primes)
#     return len(primes)
#


# count_primes(100)
# print(count_primes(100))
#
# def square(num):
#     return num**2
#
# my_nums = [1,2,3,4,5]
#
# for item in map(square,my_nums):
#     print(item)
#
#
# def vol(rad):
#     pi = 3.142
#     return (4/3*pi*rad**3)
#
# print(vol(10)

# def rango(num,low,high):
#     if num in range(low,high):
#         return 'Yes'
#
#
# print(rango(5,0,10))
#
# def countupperorlower(string):
#     upper = 0
#     lower = 0
#     for char in string:
#         if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             upper += 1
#         elif char in 'abdcdefghijklmnopqrstuvwxyz':
#             lower += 1
#     return upper,lower
#
# print(countupperorlower('HELLO son'))
#
# def uniquz(l):
#     x = []
#     for a in l:
#         if a not in l:
#             x.append(a)
#
#     return x
#
# print(uniquz([1,2,3,2,2,2]))

