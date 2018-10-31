''' Provides answer and autograder for Step 13 in CSE Activity 3.1.5.
'''

def how_eligible(essay):
    ''' Scores essay based on inclusion of characters ?",!

    essay is a string
    returns int from 0 to 4, inclusive '''
    
    score = 0 # Initialize an accumulator
    if '?' in essay:
        score += 1
    if '"' in essay:
        score += 1
    if ',' in essay:
        score += 1
    if '!' in essay:
        score += 1
    return score
    
def test_how_eligible(elig):
    ''' A test function
    
    elig is a function that is supposed to return an int 0 to 4 counting inclusion of ?!,"
    '''
    success = True
    def a_test(string, score):
        ''' Helper function decides if elig(string) returned score'''
        if elig(string) != score:
            print "Score returned for \'", string, "\' was ", elig(string), "and should have been ", score
        success = False
    a_test('try this', 0)
    a_test('Try this!', 1)
    a_test('Try this, and what about this?', 2)
    a_test('This one "should" work, but does it? Yes!', 4)
    
    if success:
        print elig ," did the job correctly!" 
    return success