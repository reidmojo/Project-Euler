# -*- coding: utf-8 -*-
"""
Prob 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
Created on Fri Jan 29 14:18:29 2016

@author: rjohnson26
"""

prime_list = []
i = 0
while len(prime_list) < 10002: # a bit hacky to deal with creating a 1 in the prime_list but i'm lazy
    templist = []
    for n in range (1,int(i**0.5)+1):
        if i % n == 0:
            templist.append(n)
            templist.append(i//n)
    if len(templist) == 2:
        prime_list.append(i)
    i = i+1
    
print prime_list[10001]