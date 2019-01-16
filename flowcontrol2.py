# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:43:17 2019

@author: Student mct
"""
name=input()
age=float(input())
if name == 'Alice':   
    print('Hi, Alice.') 
elif age < 12:    
    print('You are not Alice, kiddo.') 
elif age > 2000:   
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:    
    print('You are not Alice, grannie.')
else:    
    print('You are neither Alice nor a little kid.')
    