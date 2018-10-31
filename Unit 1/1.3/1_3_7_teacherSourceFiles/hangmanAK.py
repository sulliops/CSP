''' Hangman.py plays hangman against a single user.
'''
from __future__ import print_function
import random

def play():
    ''' Calling this function should run the game
    '''
    chances_remaining = 10

    secret = pick_a_word()[:-1] #remove newline character
    print('secret=', secret)

    letters_guessed=''
    display='' # make loop happen first time
    while chances_remaining>1 and secret!=display:
        display = create_display(secret,letters_guessed)
        if display!=secret:
            print('What is my word: ',display)
            chances_remaining -= 1
            print(chances_remaining, ' guesses left.')
            print('The letters that you have already guessed are: ', letters_guessed)
            guess = raw_input('Guess a letter please: ')
            letters_guessed += guess
            if guess in secret:
                # Player guessed right!
                pass # replace this to add a message for right and wrong? 
               
    print('Your word was', secret)
    display = create_display(secret,letters_guessed) # regenerate display word in case player guessed on last letter
    if display==secret: 
        print('You won!! You are amazing!')
    
    
def create_display(secret, guessed):
    ''' Returns the combination of revealed letters that have been guessed and 
    underscore characters where letter have not been guessed.
    Example: create_display('this test','te') returns 't___ te_t'
    '''
    revealed = ''
    for letter in secret:
        if letter == ' ': 
            revealed += ' '          # just transfer the spaces
        elif letter in guessed:
            revealed += letter       # show letters correctly guessed
        else:
            revealed += '_'          # show blanks for letters not yet guessed
    return revealed
            
def pick_a_word():
    ''' The file 'words.txt' must be in the same folder from which this
    python script is executed. A random word from it is returned
    '''
    import os.path
    directory = os.path.dirname(os.path.abspath(__file__))  
    wordlist = os.path.join(directory, 'wordsGSL2.txt')
    # General Service word list 1995 revision from http://jbauman.com/gsl.html
    wordfile = open(wordlist,'r')
    # Creates a list, one element for each line from file
    words = wordfile.readlines()
    wordfile.close()
    # Pick one of the words
    word = random.choice(words)
    return word
