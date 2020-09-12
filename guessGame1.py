# Guess the random number game
import random

# Generate a random number
r_int = random.randint(1,20)

# Inform the user what the game is
print('Please guess a random number between 1 and 20, inclusive.')

# Ask the user for a guess
guess = int(input())

num_guesses = 1

while guess != r_int:
    num_guesses += 1
    if guess > r_int:
        print('Too high')
        guess = int(input())
    else:
        print('Too low')
        guess = int(input())

# The user is correct
print('That\'s correct, the number is: {}'.format(r_int))
print('It took you {} tries to guess the number.'.format(num_guesses))
