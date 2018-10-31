from __future__ import print_function # must be first line in file 
import random

def food_id(food):
    ''' returns categorization of food
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']
    
    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

def food_id_test_AK():
    ''' Unit test for food_id
    
    returns True if good, returns False and prints error if not good
    '''
    works = True
    
    if food_id('orange') != 'Citrus, Fruit':
        works = False
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = False
        print('banana bug in food_id()')   
    # Add two more tests
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = False
        print('potato bug in food_id()')   
    if food_id('fish') != 'NOT Starchy, NOT Fruit':
        works = False
        print('fish bug in food_id()')   
    if works:
        print('food_id passed all tests!')
    return works
