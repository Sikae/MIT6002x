'''
Created on Mar 24, 2015

@author: nanci
'''
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    yes = 0
    for i in range(numTrials):
        bucket = ["red", "green", "red", "green", "red", "green"]
        results = []
        for j in range(3):
            element = random.choice(bucket)
            results.append(element)
            bucket.remove(element)
        if results[0] == results[1] == results[2]:
            yes += 1
    return yes / float(numTrials)

print noReplacementSimulation(5000)
print noReplacementSimulation(5000)
print noReplacementSimulation(5000)
print noReplacementSimulation(5000)
print noReplacementSimulation(5000)
