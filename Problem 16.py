# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:13:27 2016

@author: rjohnson26

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

z = str(2**1000)

z = [int(i) for i in z]

print sum(z)
