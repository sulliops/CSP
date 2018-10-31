'''
matches(ticket, winners) reports how well a lottery ticket did
test_matches(matches) reports whether a matches() function works as assigned.
'''

def matches(ticket, winner):
    ''' returns the number of numbers that are in both ticket and winner
    
    ticket and winner are each a list of five unique ints
    
    returns an int from 0 to 5 inclusive.
    '''
    # Could be done more effectively using the Python "set" type,
    # but that is not standard across programming languages
    # and is not introduced in the course. Could be:
    # return len(set(ticket) & set(winners))
    score = 0
    for number in ticket:
        if number in winner:
            score += 1
    return score
            
def test_matches(match_function):
    '''match_function is a function that takes two parameters, 
    each a list of five unique ints.    
    
    returns True if function works as expected;
    prints error and returns False otherwise.
    '''
    def test(ticket, winner, expected):
        if match_function(ticket, winner) == expected:
            return True
        else:
            print(match_function+' returned '+expected+' when ')
            print('      ticket = '+str(ticket) +' and ')
            print('      winner = '+str(winner))
            return False
    
    result = True
    result = result and test([1,2,3,4,5],[6,7,8,9,10],0)
    result = result and test([1,2,3,4,5],[1,6,7,8,9],1)
    result = result and test([1,2,3,4,5],[1,2,3,4,5],5)
    return result
    
            
        