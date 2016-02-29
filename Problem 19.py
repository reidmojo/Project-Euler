# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:15:18 2016

@author: rjohnson26

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""


weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
monthdaysleap = [31,29,31,30,31,30,31,31,30,31,30,31]

#total days of interest

#days = 0
#for i in range(1901,2000):
#    if i%4==0:
#        days = days+366
#    else:
#        days = days+365
#print days
#
#date = [1,1,1900]
#counter = 0
#sundays = []
#for i in range(1,days):
#    
#    if i%7 <> 0:
#        pass #not a sunday
#    else 
#        
#    if (i%months[counter])==1 and i%7 == 0:
#        sundays.append(i)
#
#print sundays[0:4]
#

date = [2000,1,1] #year, month, day

while date[0] < 2001:
    i = 1
    date[2] = date[i%7]
    date[1] = date[i%monthdays[date[1]]]   
    date[0] = date    
    i = i+1