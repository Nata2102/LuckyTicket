# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:25:38 2019

@author: Nataly
"""

def numberSum(number):
    sum=0
    while(number>0):
        sum+=number%10
        number = number//10
    return sum;



def isLuckyTicket(number):
    left = number // 1000
    right = number%1000
    if (left == right):
        return True;
    if (numberSum(left) == numberSum(right)):
        return True;
    else:
        return False;
    
    
    

count=0;
for i in range(1,1000000):
    if (isLuckyTicket(i)):
        print(i)
        count+=1
print('Lucky tickets number is',count)