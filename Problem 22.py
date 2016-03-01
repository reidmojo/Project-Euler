# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 10:26:12 2016

@author: rjohnson26

"""
index = [['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z']]

f = open('p022_names.txt', 'r')
raw = f.read()

z = raw.split(',')
x = [i.translate(None, '"') for i in z]

x.sort()
y = []
z=[]

for n in x:
    y = []
    for i in n:        
        y.append(index.index(i.split())+1)
    w = sum(y)
    v =x.index(n)+1
    z.append(w*v)