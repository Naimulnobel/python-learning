# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:08:23 2019

@author: Student mct
"""

def spam(divideBy):    
    try:       
        return 42 / divideBy    
    except ZeroDivisionError:        
        print('Error: Invalid argument.')
print(spam(2)) 
print(spam(12)) 
print(spam(0)) 
print(spam(1))
