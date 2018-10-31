import random
def guess_game(options=['Amy', 'Bill', 'Cathy']):
    '''Gets user input until random choice is guessed
    
    options is a list of strings (raw_input won't match other types)
    returns number of guesses, an int equal to 1 or more.
    '''
    
    # Randomly pick an element from the list of options
    answer = random.choice(options) 
    
    ###
    # Create a string that lists the options
    ###
    option_list = ''
    for option in options[:-1]: # Leave out the last element to precede it by "or"
        option_list += option + ', '
    option_list += 'or ' + options[-1] # Append last element
    
    ###
    # Get guesses from the user until they get it
    ###
    
    # Get the first guess
    guesses = 1 
    print('Guess which one is the secret I\'ve picked: ' + option_list)
    print('Guess: ')
    guess = raw_input()
    
    # Keep getting guesses until they get it
    while guess != answer:
        print('Guess again: ')
        guess = raw_input()
        guesses += 1
    
    # Report the result on screen and as a return value
    print('You guessed in ' + str(guesses) + ' guesses!') 
    return guesses
