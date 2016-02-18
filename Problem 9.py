# -*- coding: utf-8 -*-
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 
9 + 16 = 25 
= 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Created on Fri Jan 29 15:06:52 2016

@author: rjohnson26
"""
def list_prod(l):
    r = 1    
    for i in l:
        r = r*i
    return r

pythag_trip = []

#HULK SMASH!!!!

for i in range(1,500):
    a = i
    if a > b:
        pass
    else:
        for j in range(2,999):
            b = j
            if b > c:
                pass
            else:
                for k in range (3,1000):
                    c = k
                    if a + b + c == 1000:
                        pythag_trip.append([a,b,c])
                        print [a,b,c]
                    else:
                        pass
                
for i in pythag_trip:
    if i[0]**2 + i[1]**2 == i[2]**2:
        print i[0]*i[1]*i[2]
        exit
                