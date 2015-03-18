'''
Created on Mar 17, 2015

@author: nanci
'''
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n = len(L)
    mean = 0
    summ = 0
    if n == 0:
        return float('NaN')
    else:
        for word in L:
            mean = mean + len(word)
        mean = mean / float(n)
        for word in L:
            summ += (len(word) - mean) ** 2
        return (summ / float(n))**0.5


MyList = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(MyList)
