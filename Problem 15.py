# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:12:39 2016

@author: rjohnson26

Starting in the top left corner of a 2×2 grid
, and only being able to move to the right and down
, there are exactly 6 routes to the bottom right corner.

NOTE this problem has a visual cue that's hard to replicate here, probly need to skip on the plane

How many such routes are there through a 20×20 grid?
"""

#1x1: 4 unique sides, 2 unique paths. starting move options:
#    options at start (m0): R,D
#        options at m1(R):D
#        OPTIONS AT M1(D):R
#
#2x2: 12 unique sides, 6 distinct paths.
#    options at start(m0):R,D
#        options at m1(R): R,D
#            options at m2(R): D
#                m3(D): D
#            options at m2(D): R,D
#                m3(R): D
#                m3(D): R
#        m1(D): R,D
#            m2(R): R,D
#                m3(R): R
#                m3(D): D
#            m2(D): R
#                m3(R): R
#    
# Aha, so these are all 4-part paths:
#    RRDD
#    RDRD
#    RDDR
#OOOH these are mirrored along the square's diagonal. we can use n-part paths that start with R and double them to get all n-part paths.  So we can use binary math for this.
#    DRRD
#    DRDR
#    DDRR
#    
#
#3 grid
#RRR DDD
#
#RRD RDD
#RRD DRD
#RRD DDR
#
#RDR RDD
#RDR DRD
#RDR DDR
#
#RDD RRD
#RDD DRR
#RDD RDR

# I need to generate:
# - lists of 40 elements(R,D)
# - each list has count(R)==count(D) (that's how you get to the bottom)
# - how many unique lists can you make?


list = []

#i = int('1111111111111111111111111111111111111111',2) # largest 40-digit binary, checked with len()
##jbad = int('1000000000000000000000000000000000000000',2) # smallest 40-digit binary, checked with len() 
##    #optimization problem: i only need the smallest 40 digit binary where count(1)==count(0)
#j = int('1000000000000000000001111111111111111111',2)
##
i = 0b111111111111111111111111111111
j = 0b100000000000000000000000000000


list = []

for n in range(j,i):
    if bin(n).count('1') == 15:
        list.append(bin(n))
len(list)
        
