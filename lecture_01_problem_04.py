'''
Created on 6/3/2015

@author: Nanci
'''
from lecture_01_problem_03 import get_high_and_low_temps
import pylab

def produce_plot(low_temps, high_temps):
    diff_temps = []
    for i in range(len(low_temps)):
        diff_temps.append(high_temps[i] - low_temps[i])
    print diff_temps
    pylab.plot(range(1,32), diff_temps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

temps = get_high_and_low_temps()
produce_plot(temps[1], temps[0])
#print temps