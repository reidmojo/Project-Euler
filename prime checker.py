# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:51:31 2016

@author: rjohnson26
"""

list = [1,2,3,4,0]


def list_zero(l):
    for i in l:
        if i == 0:
            return 1
            break
    return 0    
            
prime_list = [2]

check = 100

for i in range(2,check):
    if [i%j != 0 for j in prime_list]:
        prime_list.append(i)                
    else:
        pass;
        
        