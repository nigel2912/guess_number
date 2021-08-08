
# implement a guessing game
# where the computer has a secret no. which we have to guess
# having the computer gen a secret no

import random
# random.randint(a,b) returns a no 'n' in range (a,b) such that a<n<b
# computer generates the random number and user guesses it


def guess(x):
    random_number = random.randint(1, x)
    # returns a random number
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry,too low.Guess again')
        if guess > random_number:
            print('Sorry,too high.Guess again')
    print(f'Yay! Congrats.You have guessed the number {random_number} correctly')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            # we can't have this condition in the while loop
            # because the whole point of the function is that we want the user to say
            # whether the number is correct(c) or not
            # so if we put the low!=high condition in the while condition
            # and for eg low == high in a case then the while loop will
            # break without executing the rest of the function
            # and therefore the statement 'Yay!...' will be printed directly,
            # but we don't want that directly, we want the user to enter 'c'
            guess = random.randint(low, high)
        else:
            guess = low  # or high, doesn't matter as low = high
        # Note: random.randint will throw an error if low and high are the same value
        # because if low and high are equal then basically the computer has
        # narrowed it down to your number
        feedback = input(f'Is {guess} too High(H), too Low(L), or Correct(C)').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'Yay! the computer guessed your number, {guess},correctly')


# guess(10) #for the user to guess a certain number
computer_guess(1000)  # for the computer to guess a certain number
