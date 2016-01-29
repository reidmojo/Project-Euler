# -*- coding: utf-8 -*-

"""
Project Euler: Problem 2

Created on Thu Jan 28 17:36:43 2016

@author: reid
"""

fib = []
a = 0
b = 1
c=1

while c <= 4000000:

    c = a+b
    if c % 2 == 0:
        fib.append(c)
    a = b
    b = c
    
print sum(fib) 
    