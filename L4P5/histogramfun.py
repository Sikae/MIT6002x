import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = [0, 0, 0, 0, 0]
    for word in wordList:
        for letter in word:
            if letter == 'A':
                vowels[0] += 1
            elif letter == 'E':
                vowels[1] += 1
            elif letter == 'I':
                vowels[2] += 1
            elif letter == 'O':
                vowels[3] += 1
            elif letter == 'U':
                vowels[4] += 1
    pylab.hist(vowels, bins=15)
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
