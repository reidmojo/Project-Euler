# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:15:38 2016

@author: rjohnson26

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def fac(n):
    p = []
    for i in range(1,n):
        p.append(i)
    z = 1
    for i in p:
        z *= i
    return z

def digsum(n):
    
    l = []
    for i in str(n):
        l.append(int(i))
    
    return sum(l)
