import random

def play_game():
    generated_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty choice. Please choose 'easy' or ' hard'.")
        return

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == generated_number:
            print(f"You got it! The answer was {generated_number}.")
            break
        elif guess > generated_number:
            print("Too high.")
        elif guess < generated_number:
            print("Too low.")
        
        print("Guess again")
        attempts -= 1

    if attempts == 0:
        print(f"You've run out of guesses, you lose! The number I was thinking about is {generated_number}")

play_game()
