import random

def guessing_game():
    # Function to play the guessing game
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    guess = None

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

# Start the game
guessing_game()
