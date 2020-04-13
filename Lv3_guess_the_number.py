secret_number = 381
n = input('Guess a number beetween 1 and 1000: ')
n = int(n)

while not (n == secret_number):
    if n > secret_number:
        print('Your guess was too high.')
    else:
        print('Your guess was too low.')
    n = input('Make another guess between 1 and 1000: ')
    n = int(n)
print('You got it!')