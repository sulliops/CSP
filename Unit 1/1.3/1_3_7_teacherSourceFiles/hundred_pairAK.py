''' 
Produce a histogram of the results of 
100 rolls of two 6-sided dice. 
'''
import matplotlib.pyplot as plt 
import random

def roll_pair():
    ''' Return int from 2 to 12, simulating one roll of pair of dice
    '''
    return random.choice([1,2,3,4,5,6]) + random.choice([1,2,3,4,5,6])
    
def roll_hundred_pair():
    ''' Return list of 100 ints each from 2 to 12, simulating 100 rolls of dice pair
    '''
    pairs = [] # Initialize an aggregator
    for counter in range(100):
        pairs += [roll_pair()]
    return pairs
    
many_pairs = roll_hundred_pair()
plt.ion()
plt.hist(many_pairs, bins=11, range=(1.5,12.5))
plt.show()

import numpy as np
def test_hundred_pair(roller):
    ''' A test function
    roller is a function that is supposed to return a list of 100 ints 2-12
    '''
    pairs = roller() + roller() + roller()
    success = True
    if len(pairs) != 300:
        print "List returned by ", roller, " does not contain 100 elements"
        success = False
    if min(pairs) != 2:
        print roller, "returned numbers with a min of ",min(pairs), " which should be 2"
        success = False
    if max(pairs) != 12:
        print roller, "returned numbers with a max of ", max(pairs), " which should be 12"
        success = False
    if  not (2.2<np.std(pairs)<2.6):
        print roller, "returned numbers with a standard deviation of ", np.std(pairs),\
           "which is expected to between 2.2 and 2.6 more than 99% of the time."
        success = False
    if success:
        print roller ," did the job correctly!" 
    return success
    
# At the tail end of __main, output shown for unit test.    
print test_hundred_pair(roll_hundred_pair)    