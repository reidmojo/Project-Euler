# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 09:42:44 2016
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
@author: rjohnson26
"""

def div(n):
    div_list = []
    for i in range(1,int(round(n/2+1,0))):
        if n%i == 0:
            div_list.append(i)
            
    return sum(div_list)
    
def amicable(a,b):
    if div(a) == b and div(b) == a:
        return a,b
    else:
        return 0

amicable_list = []

for i in range(0,10001):
    a = div(i)
    if div(i) == a and div(a) == i and a != i:
        print i
        if i not in amicable_list:
            amicable_list.append(i)
        if a not in amicable_list:
            amicable_list.append(a)

print amicable_list, sum(amicable_list)