"""
Number Guessing Game
Author: Sabeer

Computer ek random number sochta hai, aur player ko usse guess karna hota hai.
Features: 3 difficulty levels, hints, attempts limit, aur high score save hota hai.
"""

import random
import os

HIGH_SCORE_FILE = "highscore.txt"

# Difficulty: (naam, max number, total attempts)
LEVELS = {
    "1": ("Easy", 50, 10),
    "2": ("Medium", 100, 7),
    "3": ("Hard", 500, 9),
}


def load_high_score():
    """File se best score padhta hai. Agar file nahi hai to None return karta hai."""
    if not os.path.exists(HIGH_SCORE_FILE):
        return None
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return None


def save_high_score(score):
    """Naya best score file me save karta hai."""
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))


def choose_level():
    """Player se difficulty level puchta hai."""
    print("\nSelect difficulty:")
    for key, (name, limit, attempts) in LEVELS.items():
        print(f"  {key}. {name}  (1 to {limit}, {attempts} attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in LEVELS:
            return LEVELS[choice]
        print("Invalid choice! Please enter 1, 2 or 3.")


def get_guess(limit):
    """Valid number input leta hai (error handling ke saath)."""
    while True:
        value = input("Your guess: ").strip()
        if not value.isdigit():
            print("Please enter a valid number!")
            continue
        guess = int(value)
        if guess < 1 or guess > limit:
            print(f"Number must be between 1 and {limit}.")
            continue
        return guess


def play_round():
    """Ek poora game round khelta hai."""
    name, limit, max_attempts = choose_level()
    secret = random.randint(1, limit)
    print(f"\nI'm thinking of a number between 1 and {limit}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}/{max_attempts}")
        guess = get_guess(limit)

        if guess == secret:
            print(f"\nCorrect! You guessed it in {attempt} attempt(s)!")
            # Kam attempts = zyada score
            score = (max_attempts - attempt + 1) * 10
            print(f"Your score: {score}")
            return score

        if guess < secret:
            print("Too low! Try a bigger number.\n")
        else:
            print("Too high! Try a smaller number.\n")

        # Last 2 attempts me hint do
        if max_attempts - attempt == 1:
            hint = "even" if secret % 2 == 0 else "odd"
            print(f"Hint: the number is {hint}.\n")

    print(f"Game over! The number was {secret}.")
    return 0


def main():
    print("=" * 40)
    print("   WELCOME TO NUMBER GUESSING GAME")
    print("=" * 40)

    high_score = load_high_score()

    while True:
        if high_score is not None:
            print(f"\nHigh score: {high_score}")

        score = play_round()

        if score > 0 and (high_score is None or score > high_score):
            high_score = score
            save_high_score(high_score)
            print("New high score! Saved.")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Bye!")
            break


if __name__ == "__main__":
    main()
