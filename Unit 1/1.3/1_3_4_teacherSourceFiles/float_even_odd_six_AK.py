def f(n):
    '''
    Returns a fact: n is non-int, odd, even (and not a multiple of 6), or a multiple of 6.
    
    n is a numeric type''' 
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                return 'The number is a multiple of 6.'
            else:
                return 'The number is even.'
        else:
            return 'The number is odd.'
    else:
        return 'The number is not an integer.'
        
def f_test():
    ''' Unit tests for f(n)
    ''' 
    print ('Not integer:', f(1.5))
    print ('Multiple of 6:', f(12))
    print ('Odd:', f(15))
    print ('Even:', f(10))
        
