import random

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
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = [i.lower() for i in word_list]
        self.list_of_guesses = []
        print(f"The mystery word has {self.num_letters} characters")
        print(f"The mystery word is: {self.word_guessed}")
       

    def check_guess(self, guess):
        '''
        This method checks whether the guess is in the word.

        If the guess is in the word it replaces the "_" in the word_guessed list with the letter guessed.
        If it is not, it reduces the number of lives by 1.

        Parameters:
            guess (str): The letter to be checked.
        '''
        # Check whether the guess is in the word.
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = letter
                    self.num_letters = self.num_letters - 1          
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
        print("--------------------------------------------------")
        print(f"Letters guessed so far are: {self.list_of_guesses}")
        print(f"The mystery word has {self.num_letters} characters remaining")
        print(f"The mystery word is: {self.word_guessed}")
        
            
    def ask_for_input(self):
        '''
        This method asks the user for a guess and validates the response. It checks two things:
        1. If the character is a single character.
        2. If the letter has already been tried.
        If it passes both checks, it calls the check_guesses method. 
        '''
        # Iteratively check if the input is a valid guess. 
        while True:
            guess = input("Please enter a single letter character:")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.list_of_guesses.append(guess)
                return self.check_guess(guess)

def play_game(word_list):
    '''
    This function creates an attribute for the Hangman class and checks two things:
    1. Whether num_lives is equal to zero.
    2. Whether num_letters is equal to zero.
    If neither check is equal to zero it calls the game.ask_for_input function.

    Parameters:
        word_list (list): List of words to be used in the game.
    '''
    num_lives = 5
    num_letters = None
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            return None
        elif game.num_letters == 0:
            print("Congratulations! You won the game.")
            return None
        else:
            game.ask_for_input()

if __name__ == '__main__':
    fruits_list = ["Apple", "Banana", "Cherry", "Melon", "Pear", "Mango", "Blackberry", "Orange",
                   "Papaya", "Plum", "Fig", "Lime", "Raspberry", "Blackcurrant"]
    play_game(fruits_list)
