# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:51:31 2016

@author: rjohnson26
"""

prime_list = [1,2]

check = 200000

for i in range(2,check+1):
    if i%2 == 0:
        pass
    tmp_list = []
    for j in prime_list:
        if j >= int(round(i**0.5,0)):
            break
        if i%j == 0:
            tmp_list.append(i)
    if len(tmp_list) == 1:
        prime_list.append(i)

print prime_list[-1]