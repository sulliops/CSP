from __future__ import print_function

def quiz_decimal(low, high):
    '''Prints whether user's number is between low and high
    
    
    low and high are numeric types
    returns None
    '''
    # Prompt fpr the value
    print('Type a number between '+str(low)+' and '+str(high)+': ',end='' )
    user_value = float(raw_input())
    
    # Int inputs get converted to float. Revert this!
    if int(user_value) == user_value:
        user_value = int(user_value)
    
    # Test and report
    if user_value < low:
        print('No, ' + str(user_value) + ' is less than ' + str(low))
    elif user_value > high:
        print('No, ' + str(user_value) + ' is greater than ' + str(high))
    else:
        print('Good! ' + str(low) + ' < ' + str(user_value) + ' < '+ str(high))
    