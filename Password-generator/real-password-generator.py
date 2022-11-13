# words+symbols+numbers generator

import random

wordList = ['optyzGaming', 'darXpro', 'Optyx', 'Dar', 'op',
            'Overpowered', 'GamerOptyX', 'SecurePass', 'Hardy']

Nmbrs = ['1234567890', '54321', '123', '7777', '9294', '8080', '7676', '9906']

Symb = '@#$_'

number = input('No. of passwords to generate? ')

while 1:
    number = int(number)
    for p in range(number):
        password = ''
        for c in range(1):  # 1 = 1 password eg- op@123  2 = op@123op#321
            password += random.choice(wordList) + \
                random.choice(Symb) + random.choice(Nmbrs)
        print(password)

    again = input('Generate again? (y/n) ')
    if again != 'y':
        break

#  one  word has 32 options to choose from
#  there are 9 words
# 32*9 = 288 therefore max password that can be generated is 288 ------> different passwords [not same]
# it can generate thousands of passwords but there might be same passwords generated again and again
