import random
import string
print('Welcome to the PyPassword Generator!')

# User input to adjust password parameters
num_of_letters = int(input('How many letters would you like in your password? '))
num_of_symbols = int(input('How many symbols would you like? '))
num_of_digits = int(input('How many numbers would you like? '))

# Generating available characters from string module
letters = [*string.ascii_letters]
symbols = [*string.punctuation]
digits = [*string.digits]

# Creating list of random characters

password_list = []

for _ in range(0, num_of_letters):
    password_list.append(random.choice(letters))

for _ in range(0, num_of_symbols):
    password_list.append(random.choice(symbols))

for _ in range(0, num_of_digits):
    password_list.append(random.choice(digits))

# Preparing the final password
random.shuffle(password_list)

password_string = ''.join(password_list)

print(f'Your password is: {password_string}')
