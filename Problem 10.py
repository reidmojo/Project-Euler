# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Created on Fri Jan 29 15:08:17 2016

@author: rjohnson26
"""

def is_prime(n):
    templist = []
    for i in range(1,int(round((n**0.5)+1,0))):
        if n%i == 0:
            templist.append(i)
        else:
            pass
    if len(templist) == 1:
        return 1
        
def listsum(l):
    s = 0    
    for i in l:
        s = s+ i
    return s

primelist = []

for i in range(2,2000000):
    if is_prime(i) == 1:
        primelist.append(i)
    if i%10000 == 0:
        print i
    else:
        pass

print listsum(primelist)
#        if 4%i == 0:
#            templist.append(i)