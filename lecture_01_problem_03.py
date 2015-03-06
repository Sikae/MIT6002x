'''
Created on 6/3/2015

@author: Nanci
'''
import string
PATH_TO_FILE = 'julyTemps.txt'



def get_high_and_low_temps():
    high_temps = []
    low_temps = []
    inFile = open(PATH_TO_FILE, 'r', 0)
    for line in inFile:
        fields = string.split(line)
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high_temps.append(int(fields[1]))
            low_temps.append(int(fields[2]))
    return high_temps, low_temps

#print get_high_and_low_temps()
