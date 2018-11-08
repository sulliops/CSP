from __future__ import print_function # use Python 3.0 printing

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13    # convention: use CAPS for constants
    if age < AGE_LIMIT:
      print (age, 'is below the age limit.')
    else:
      print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
def report_grade(percent):
    '''Step 6b if-else'''
    minimum = 79
    if percent > minimum:
      print ('A grade of', percent, 'percent indicates mastery.')
      print ('Keep up the good work!')
    else:
      print ('A grade of', percent, 'percent does not indicate mastery.')
      print ('Seek extra practice or help.')