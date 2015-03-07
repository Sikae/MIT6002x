'''
Created on Mar 7, 2015

@author: nanci
'''
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 16

print deterministicNumber()

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 21, 2)

print stochasticNumber()
