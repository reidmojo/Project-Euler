# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:13:40 2016

@author: rjohnson26

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
l = [1,2,3,4,5,6,7,8,9]
m = ['one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']
n = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen','nineteen']
o = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


x = 0
#for i in range(1,1000):
def nameprint(i):
    q=[]       
    i = str(i)
    z = [int(i) for i in i]
    if len(z) == 3:
        q.append(m[z[0]-1])
        if z[1] == 0 and z[2] == 0:
            q.append('hundred')
            return q
        q.append('hundredand')
        if z[1] == 0:
            q.append(m[z[2]-1])
        else:
            if z[1] == 1:
                q.append(n[z[2]]) # if the second element of z = 1, use the 'teens' lookup table against the last element's value                
            else:
                if z[2] == 0:
                    q.append(o[z[1]-2])
                else:
                    q.append(o[z[1]-2]) #look up the second element against the 'ty's list
                    q.append(m[z[2]-1]) #look up the last element in the ones list
    else:
        if len(z) == 2:
            if z[0] == 1:
                q.append(n[z[1]])
            else:
                if z[1] == 0:
                    q.append(o[z[0]-2])
                else:
                    q.append(o[z[0]-2])
                    q.append(m[z[1]-1])
        else:
            q.append(m[z[0]-1])
    return q
    
for i in range(1,1000):
    x = x+ sum(len(j) for j in nameprint(i))
    print i, nameprint(i)
x=x+len('onethousand')

print x;