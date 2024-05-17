import random

word_list = ["Apple", "Banana", "Cherry", "Dragon fruit", "Pear"]

class Hangman():
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = None
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def ask_for_input():
        '''
        This function asks the user for a guess and validates the response.
        '''
        # Iteratively check if the input is a valid guess. 
        while True:
            guess = input("Please enter a single letter character:")
            if guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter")
            else:
                list_of_guesses.append(guess)
                return check_guess(guess)
                

    def check_guess(guess):
        '''
        This function checks whether the guess is in the word.
        '''
        # Check whether the guess is in the word.
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

