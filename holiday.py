import random


def play_hangman():
    # Predefined list of 5 words
    words = ['python', 'code', 'logic', 'program', 'screen']
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("--- Welcome to Hangman! ---")

    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Build current word display (e.g., "p y t _ o n")
        display_word = [
            letter if letter in guessed_letters else '_' for letter in secret_word]
        print(f"\nWord: {' '.join(display_word)}")
        print(
            f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        print(
            f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check win condition
        if '_' not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        # Input handling
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    # Loss condition
    print(f"\nGame Over! You ran out of guesses. The word was: {secret_word}")


if __name__ == '__main__':
    play_hangman()
