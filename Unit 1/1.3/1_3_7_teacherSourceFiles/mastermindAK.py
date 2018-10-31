def report(guess, secret):
    #Copy the lists that were passed
    guess_copy = guess[:]
    secret_copy = secret[:]
    
    #Check for reasonable input
    if len(guess) != len(secret):
        return "Error in report(): lengths don't match"
    
    # Initialize the accumulators
    right_place = 0
    right_color = 0
    
    # Find the "right place" pegs
    # Go through the positions one at a time
    for peg in range(len(secret_copy)):
        # If guessed correctly
        if guess_copy[peg] == secret_copy[peg]:    
            right_place += 1            
            guess_copy[peg] = 'g-used'    # don't allow a guess color to count twice
            secret_copy[peg] = 's-used'   # don't allow a secret color count twice
    
    # Find the "right color" pegs
    # Go through every combo once
    for secret_peg in range(len(secret_copy)):
        for guess_peg in range(len(guess_copy)):
            if guess_copy[guess_peg] == secret_copy[secret_peg]:
                right_color += 1
                # Don't allow either peg to be counted again
                guess_copy[guess_peg] = 'g-used'
                secret_copy[secret_peg] = 's-used'
                
    return [right_place, right_color]
                    
def test_mastermind(report_function):
    ''' Tests mastermind using 3 test cases.
    report_function is a function 
    returns True if function passes test, False otherwise.'''
    secret1 = ['r','g','b','g','r']
    guess1 = ['r', 'r', 'r', 'r', 'r'] # excess matches beyond right positions: 2, 0
    guess2 = ['g','f','g', 'f', 'g'] # excess in wrong locations: 0,2
    guess3 = ['r','w','w','w','g'] # excess in secret: 1, 1
    
    def report(guess, secret, answer):
        print "Guessing ", guess, " against ", secret, ": ",
        result = report_function(guess, secret)
        if result == answer:
            print " worked!"
            return True
        else:
            print "failed, \n\t\t returned ",result, "instead of ",answer        
            return False
    
    
    worked = True
    worked = worked and report(guess1, secret1, [2,0])
    worked = worked and report(guess2, secret1, [0,2])
    worked = worked and report(guess3, secret1, [1,1])
    return worked
    
test_mastermind(report) #  Truth value returned is not returned to iPython