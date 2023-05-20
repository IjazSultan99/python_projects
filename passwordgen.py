import random

print('Welcome to your Password Generator')

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@£$%^&*()0123456789'

number = input('How many passwords do you want to generate?: ')
number = int(number)

length = input('How many character do you want the password to be?: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)