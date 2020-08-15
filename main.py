import random

password = ''

y = 1
n = 2

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?'
nosym = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def start_pass():
    global pass_length, password, sym_choice
    pass_length = input('How long should the password be? ')
    pass_length = int(pass_length)
    if pass_length < 8:
        careful_input = input('Passwords under 8 characters are more susceptible to being hacked. Would you like to proceed? (y/n): ')
        if careful_input == "y":
            symbol_choice()
        elif careful_input == "n":
            start_pass()
    else:
        symbol_choice()
    if pass_length <= 0:
        start_pass()

def symbol_choice():
    while True:
        sym_choice = input("Do you want any symbols in the password? (y/n): ")
        if sym_choice == "y":
            all_chars()
        elif sym_choice == "n":
            no_more_sym()
        else:
            print('Please type a valid selection (y = yes, n = no)')
            symbol_choice()

def all_chars():
    global pass_length, password
    for x in range(pass_length):
        password += random.choice(chars)
    print(password)
    more_passwords()

def no_more_sym():
    global pass_length, password
    for x in range(pass_length):
        password += random.choice(nosym)
    print(password)
    more_passwords()

def more_passwords():
    global password
    answer = input('Would you like to make another password? (y/n): ')
    if answer == "y":
        password = ''
        start_pass()
    elif answer == "n":
        password = ''
        exit()
    else:
        print('Please type a valid selection (y = yes, n = no)')
        more_passwords()

start_pass()
