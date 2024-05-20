# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Table of Contents
1. Description
1. Usage Instructions
1. File Structure of the Project
1. Licence Information

## Description
This is an implementation of the [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) game, where the computer thinks of a word and the user tries to guess it. How to play this game? In this game you have to figure out a mystery word by guessing one letter at a time. However, with each incorrect guess you lose a life, and get one step closer to death! The goal is to successfully guess the word before the man is hanged. 

The project started as a goal to learn Python and version control systems. In this simplified version of the game the computer randomly selects a word from a list of fruits and the user guesses letters one by one. Everytime an incorrect guess is made the user loses a life. If 5 lives are lost the user has lost the game. If there are no hidden letters the user has successfully won the game. 

### Usage Instructions
1. Run "python milestone_5.py"
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
