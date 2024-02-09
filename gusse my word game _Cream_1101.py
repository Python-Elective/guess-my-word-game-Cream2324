#  -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()


# Problem 1
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    """
    for every letter in secret_word
        if the letter is not in letter_guessed
            stop looking and return false
    return true
    """
 
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
       
 
# Testcases
print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(is_word_guessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))
print(is_word_guessed('pineapple', []))
 
# Problem 2
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    output_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output_string += letter + " "
        else:
            output_string += "_ "
    return output_string
# Testcases
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(get_guessed_word ('banana', []))
 

# Problem 3
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''  
    import string
    alphabet = list(string.ascii_lowercase)
 
    for letter in alphabet:
        if letter in letters_guessed:
            alphabet.remove(letter)
 
    return ' '.join(alphabet)
# Testcases
print(get_available_letters('apple'))
print(get_available_letters(''))

# Problem 4

def game_loop(secret_word):

    '''

    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many

      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess

      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the

      partially guessed word so far, as well as letters that the

      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.

    '''
    letters_guessed = []

    mistakes_made = 0

    print("Let the game begin!")

    print(f"I am thinking of a word with {len(secret_word)} letter")

    while True:

        print(f"You have {8-mistakes_made} guess remaining.")

        print(f"Letters available to you: {get_available_letters(letters_guessed)}")

        guess = input("Guessed a letter:")

        if guess in letters_guessed:

          print(f"You fool! You tried this letter already")

        elif guess in secret_word:

          letters_guessed.append(guess)

          print(f"Correct: {get_guessed_word(secret_word,letters_guessed)}")

        else:

          print(f"Incorrect, this letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

          letters_guessed.append(guess)

          mistakes_made += 1

        if is_word_guessed(secret_word, letters_guessed):

           print("You Win")

           break

        if mistakes_made == 8:

           print(f"Gameover, the word was {secret_word}")

           break

# Testcases
def main():

    secret_word = choose_word(word_list)

    game_loop('airplane')


if __name__ == "__main__":

    main()