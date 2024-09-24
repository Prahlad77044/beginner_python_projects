import random
def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}:"))
        if guess<random_number:
            print("Wrong guess. Your guess is too low.")
        elif guess>random_number:
            print("Wrong guess. Your guess is too high.")

    print(f"Yay you guessed the number correctly. The number was {random_number}")      
guess(10)