from __future__ import print_function
import random 
    
def goguess(low=1, high=20):
    ''' Picks a number at random and then accepts guesses.
    Prints feedback "too high" or "too low".
    Prints number of guesses.
    
    Returns number of guesses.
    '''
    secret = random.randint(low, high)
    guesses = 0
    print ("I have a number between", low, "and", high, "inclusive.")
    user_input = 'a' # Initialize to something that is not the the secret
    while user_input != secret:
        user_input = int(raw_input("Guess: "))
        guesses += 1
        if user_input > secret:
            print (user_input, "is too high.")
        if user_input < secret:
            print (user_input, "is too low.")
    print("Right! My number is ",secret,"! You guessed in ", guesses, " guesses!", sep="")
    
