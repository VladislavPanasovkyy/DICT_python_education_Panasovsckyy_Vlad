import random

def play_hangman():

    word_list = ['python', 'java', 'javascript', 'php']

    secret_word = random.choice(word_list)

    lives = 8

    guessed_word = '-' * len(secret_word)

    used_letters = []

    print("HANGMAN")
    print(guessed_word)

    while lives > 0:
        letter = input("Input a letter: > ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not letter.islower() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if letter in used_letters:
            print("You've already guessed this letter")
            continue

        used_letters.append(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed_word = guessed_word[:i] + letter + guessed_word[i + 1:]
            print(guessed_word)
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

        if guessed_word == secret_word:
            print("You guessed the word!")
            print("You survived!")
            break

    if guessed_word != secret_word:
        print("You lost!")
        print("The word was:", secret_word)

while True:
    user_choice = input("Type 'play' to play the game, 'exit' to quit: > ")
    if user_choice == 'play':
        play_hangman()
    elif user_choice == 'exit':
        break