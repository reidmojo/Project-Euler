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
f_num = 600851475143
    
#is it a factor?        
for i in range(1,int(f_num**0.5)+1):    
    if f_num % i == 0:
        n = f_num // i
        factor_list.append(i)
        factor_list.append(n)
    
    
print 'done factoring!'
#doing factors is easier than primes, so do it first

#is prime?
for i in factor_list:
    templist = []
    for n in range (2,int(i**0.5)+1):
        if i % n == 0:
            templist.append(n)
            templist.append(i//n)
    if len(templist) == 0:
        prime_list.append(i)
        
print max(prime_list)