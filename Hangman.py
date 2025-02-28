import random

# Predefined word list
word_list = ["python", "java", "ruby", "swift", "hangman", "developer", "coding", "github"]

# Function to play the game
def play_hangman():
    chosen_word = random.choice(word_list).lower()
    word_display = ["_"] * len(chosen_word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    hangman_figures = [
        """
           ------
           |    |
           |    
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        --------
        """
    ]

    print("🎮 Welcome to Hangman! Try to guess the word 🎮")

    while incorrect_guesses < max_attempts:
        print(hangman_figures[incorrect_guesses])  # Display hangman figure
        print("Word: ", " ".join(word_display))
        print(f"Incorrect Guesses: {incorrect_guesses}/{max_attempts}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed this letter. Try another one!")
            continue

        guessed_letters.add(guess)

        # Check if the letter is in the word
        if guess in chosen_word:
            print("✅ Good guess!")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess!")
            incorrect_guesses += 1

        # Check win condition
        if "_" not in word_display:
            print("\n🎉 Congratulations! You guessed the word:", chosen_word)
            break
    else:
        print(hangman_figures[incorrect_guesses])
        print("\n💀 Game Over! The correct word was:", chosen_word)

# Main loop to allow replay
while True:
    play_hangman()
    play_again = input("\nDo you want to play again? (yes/y or no/n): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye! 👋")
        break
