# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Table of Contents
1. Description
1. Usage Instructions
1. File Structure of the Project
1. Licence Information

## Description
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Usage Instructions
1. In the Command Line execute the command "python milestone_5.py"
1. The output will read:
    - "The mystery word has *num* characters." where *num* is the number of letters in the word.
    - "The mystery word is: [ '_' * num]."
1. When prompted input your guess as a single letter character.
    - If the entry is invalid you will receive a message stating "Invalid letter. Please, enter a single alphabetical character."
    - If you have already guessed that letter you will receive a message stating "You already tried that letter"
    - Please enter a new guess.
1. The program will check whether your guess is in the word and will respond with either:
    - "Good guess! *Your guess* is in the word." and the number of letters remaining in the mystery word will reduce by the number of correct letters.
    - "Sorry, *Your guess* is not in the word. Try again." and your number of lives remaining will reduce by 1 which will be printed.
1. The program will now print:
    - A list of the letters guessed so far.
    - The number of characters remaining in the mystery word.
    - "The mystery word is:" and a list of characters in the mystery word, either as an underscore representing mystery letters or as letters of correct guesses in their corresponding location in the mystery word. 
1. When prompted input your guess as a single letter character and follow steps 3 to 6.
1. The game ends when either you run out of lives or you correctly guess all of the letters in the mystery word.

### File Structure of the Project


### Licence Information
None
