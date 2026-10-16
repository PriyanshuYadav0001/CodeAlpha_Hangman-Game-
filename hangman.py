"""
CodeAlpha Python Internship - Task 1: Hangman Game
A simple text-based Hangman game.
Concepts: random, while loop, if-else, strings, lists
"""

import random

WORDS = ["python", "internship", "computer", "keyboard", "developer"]
MAX_WRONG = 6

HANGMAN_STAGES = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("      WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG:
        print(HANGMAN_STAGES[wrong_guesses])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Win check
        if all(letter in guessed_letters for letter in word):
            print("\nWord:", display_word(word, guessed_letters))
            print(f"\nCongratulations! You guessed the word: {word.upper()}")
            return

    # Loss
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"\nGame over! The word was: {word.upper()}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
