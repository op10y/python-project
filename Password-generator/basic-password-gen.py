import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

while 1:
    password_len = int(input('Password length? '))
    password_count = int(input('Number of passwords? '))
    for x in range(0, password_count):
        password = ''
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print('Here is your password: ', password)
