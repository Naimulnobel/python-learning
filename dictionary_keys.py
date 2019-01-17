# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:07:04 2019

@author: Student mct
"""

spam = {'color': 'red', 'age': 42} 
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
spam.keys()
print(spam)
picnicItems = {'apples': 5, 'cups': 2} 
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' )
print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' apples.') 
lists = {'name': 'Pooka', 'age': 5} 
if 'color' not in lists:   
    lists['color'] = 'black'
    print(lists)
    
