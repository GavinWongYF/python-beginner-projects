import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Word so far: ", " ".join(word_list))
        print("You have ", lives, "lives left.")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Your letter is not in the word.")
        
        elif user_letter in used_letters:
            print("You've already guessed that letter. Guess another one!")
        
        else:
            print("Invalid character. Please enter another letter.")
    
    if len(word_letters) == 0:
        print("You win! The word was: ", word)
    else:
        print("You died, sorry. The word was: ", word)

hangman()



 


