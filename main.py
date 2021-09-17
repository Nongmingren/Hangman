from vocab import words
from visual import hangman
import random
import string

def get_valid_word(list_word):
    word = random.choice(list_word)
    while "-" in word or " " in word:
        word = random.choice(list_word)
    return word.upper()


def play_hangman():
    valid_word = get_valid_word(words)
    word_character = set(valid_word)
    set_character = set(string.ascii_uppercase)
    used_character = set()
    lives = 7
    # print(f"VALID WORD: {valid_word}")
    # print(f"SET CHARACTER: {set_character}")
    while len(word_character) > 0 and lives > 0:
        print(f"You have {lives} left. Word = {', '.join(used_character)}")

        word_list = []
        for character in valid_word:
            if character in used_character:
                word_list.append(character)
            else:
                word_list.append("-")
        print("Hangman")
        print(hangman[lives])
        print("-" * 20)
        print(f"Current Word: {', '.join(word_list)}")

        input_character = input("Letter: ").upper()
        # print(f"set Character: {set_character}")
        # print(f"User Character: {input_character}")
        # print(f"User Character: {input_character}")
        # print(f"Used Character: {set_character}")
        # print(f"set_character-user character {set_character-used_character}")

        if input_character in set_character - used_character:
            used_character.add(input_character)
            print(f"User Character: {input_character}")
            if input_character in word_character:
                word_character.remove(input_character)
            else:
                lives = lives - 1
                print(f"The letter : {input_character} is not in the word")
        elif input_character in used_character:
            print(f"You have already used {input_character}")
        else:
            print("That is not a valid letter")
    if lives == 0:
        print(hangman[lives])
        print(f"You failed the word is {valid_word}")
    else:
        print(f"Correct you guessed the word: {valid_word}")


play_hangman()
