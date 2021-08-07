# implement a guessing game where the computer has a secret no which we hv
# to guess

# having the computer gen a secret no
import random
# random.randint(a,b) returns a no 'n' in range (a,b) such that a<n<b


def guess(x):
    random_number = random.randint(1, x)
    # returns a random number
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry,too low.Guess again")
        if guess > random_number:
            print("Sorry,too high.Guess again")

    print(
        f"Yay! Congrats.You have guessed the number {random_number} correctly")
