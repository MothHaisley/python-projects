import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Guess again! Brr, ice cold!")
        elif guess > random_number:
            print("Guess again! Szzz, too hot!")

    print(f"Yay! You guessed the number {random_number} correctly. DM me Pizza Panda to get a prize!")

guess(10)


