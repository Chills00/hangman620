word = "apple" # Need to remove from code

def ask_for_input():
    '''
    This function asks the user for a guess and validates the response.
    '''
    # Iteratively check if the input is a valid guess. 
    while True:
        guess = input("Please enter a single letter character:")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
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

ask_for_input()