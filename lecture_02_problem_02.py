'''
Created on Mar 7, 2015

@author: nanci
'''
import random

print random.randint(1, 5)
print random.choice(['apple', 'banana', 'cat'])

def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    return random.randrange(0, 100, 2)

print genEven()
