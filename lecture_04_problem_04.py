'''
Created on Mar 18, 2015

@author: nanci
'''
def compute_coefficient_of_variation(X):
    # first, compute standard deviation
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std_dev = (tot/len(X))**0.5
    return std_dev / mean


print compute_coefficient_of_variation([1,2,3])
print compute_coefficient_of_variation([11,12,13])
print compute_coefficient_of_variation([0.1,0.1,0.1])
print compute_coefficient_of_variation([10, 4, 12, 15, 20, 5])
    