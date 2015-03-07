'''
Created on Mar 7, 2015

@author: nanci
'''
import random
mylist = []
 
for i in xrange(random.randint(1, 10)):
    print i
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist
    
# Code Sample A
mylist = []
  
for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist
  
# Code Sample B
mylist = []

random.seed(0)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print mylist
