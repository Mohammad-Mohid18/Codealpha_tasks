import random


words = ['python','programming','challenge','development','coding','internship']

stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
]


rand_word = random.choice(words)
guessed_letters = set()
lives = len(stages) - 1

print("🎮 Welcome to Hangman! Let's start!")

while lives > 0:
    print(stages[len(stages) - lives])
    display_word = ''

    for letters in rand_word:
        if letters in guessed_letters:
            display_word += letters + ''
        else:
            display_word += ' - '

    print(display_word)

    if ' - ' not in display_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in rand_word:
        guessed_letters.add(guess)
        print("✅ Good guess!")
    else:
        guessed_letters.add(guess)
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")

if lives == 0:
    print(stages[-1])
    print(f"💀 Game Over! The word was '{rand_word}'.")