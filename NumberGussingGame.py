import random

def number_guessing_game():
    # 1. Pick a random secret number
    secret = random.randint(1, 100)
    max_tries = 10
    tries_left = max_tries

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_tries} tries. Good luck!\n")

    while tries_left > 0:
        # 2. Get the player's guess
        try:
            guess = int(input(f"Tries left: {tries_left} → Your guess: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        # 3. Validate the range
        if guess < 1 or guess > 100:
            print("Please guess between 1 and 100.\n")
            continue

        tries_left -= 1

        # 4. Check the guess
        if guess == secret:
            guesses_used = max_tries - tries_left
            print(f"🎉 Correct! The number was {secret}.")
            print(f"You got it in {guesses_used} guess(es)!")
            break
        elif guess < secret:
            print(f"Too low! Try higher. ({tries_left} tries left)\n")
        else:
            print(f"Too high! Try lower. ({tries_left} tries left)\n")

    else:
        # This runs when tries_left hits 0
        print(f"Game over! The number was {secret}. Better luck next time!")

# --- Play the game ---
while True:
    number_guessing_game()
    again = input("Play again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Thanks for playing! Bye ")
        break