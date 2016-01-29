# -*- coding: utf-8 -*-
"""
Euler Problem 3

Created on Thu Jan 28 18:16:09 2016

@author: reid
"""

#what is the largest prime factor of 600851475143?

#Factors of 600851475143
prime_list  = []
factor_list = []
factoring_agent = 600851475143
    
#is it a factor?        
for i in range(1,factoring_agent):    
    if factoring_agent % i == 0:
        factor_list.append(i)
    else:
        pass

print 'done factoring!'
#doing factors is easier than primes, so do it first

#is prime?
for i in factor_list:
    templist = []
    for n in range (2,i):
        if i % n == 0:
            templist.append(i)
        else:
            pass
    if len(templist) == 0:
        prime_list.append(i)
        
print max(prime_list)