from __future__ import print_function
import random
 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
     
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Summarize the following section of code here
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
def goguess(numbers=('1', '2', '3', '4')):
    correct_answer = random.choice(numbers)
    print('Guess a number from these guesses: ',end='')
    for p in numbers[:len(numbers)-1]:
        print(p+', ', end='')
    print(numbers[len(numbers)-1])
    guesses = 1
    while raw_input() != correct_answer:
        print('Try again!')
        guesses += 1
    print('It took you', guesses, 'tries to guess the correct answer!')
    return guesses