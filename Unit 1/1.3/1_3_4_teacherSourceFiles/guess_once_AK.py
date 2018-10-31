from __future__ import print_function # must be first line in file 
import random

def guess_once():
    '''Allows a single guess and prints feedback.
    
    returns None
    '''
    
    secret = random.randint(1, 4)
    print ('I have a number between 1 and 4 inclusive.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '!', sep='')
    elif guess > secret:
        print('Too high, my number was ', secret, '!', sep='')
    else:
        print('Right on! I was number ', secret, '!', sep='')

def guess_once_test():
    ''' Unit test for guess_once() 
    
    returns True is guess_once() passes
    returns string error message if guess_once() fails
    '''
    # How to direct raw_input into a script, akin to input redirection?