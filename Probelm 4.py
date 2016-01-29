# -*- coding: utf-8 -*-
"""
Euler Problem 4

Created on Fri Jan 29 11:21:52 2016

@author: rjohnson26
"""


def is_palindrome(n):
    a = []
    n = str(n)
    for ch in n:
        a.append(ch)
    rev = a[::-1]
    return rev == a
    
list = []

for i in range(100,999):
#    list.append(i)
    for n in range(100,999):
        list.append(i*n)
        
list2 = []
        
for i in list:
    if is_palindrome(i) == True:
        list2.append(i)

print max(list2)
        