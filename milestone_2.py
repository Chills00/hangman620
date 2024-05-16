import random

# Create list of 5 fruits:
word_list = ["Apple", "Banana", "Cherry", "Dragon fruit", "Pear"]
print(word_list)

# Select a random word from the list using the choice method from random:
word = random.choice(word_list)
print(word)

# Ask the user for an input:
guess = input("Please enter a single letter character:")
if len(guess) == 1:
    print("Good guess")
else:
    print("Oops! That is not a valid input.")