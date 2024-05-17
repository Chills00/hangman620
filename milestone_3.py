# Iteratively check if the input is a valid guess. 
while True:
    guess = input("Please enter a single letter character:")
    if guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

