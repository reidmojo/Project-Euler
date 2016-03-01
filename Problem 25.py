# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:15:01 2016

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

@author: rjohnson26
"""

def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = [1,1]
n = 1
i = 2
while len(str(n))<1000:
    n = fib[i-1]+fib[i-2]
    fib.append(n)
    i += 1    
print fib.index(n)+1