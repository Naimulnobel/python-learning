# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:58:57 2019

@author: Student mct
"""

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:  
    print('Enter a name: (blank to quit)')   
    name = input()    
    if name == '':       
        break
    if name in birthdays:         
        print(birthdays[name] + ' is the birthday of ' + name)   
    else:       
        print('I do not have birthday information for ' + name)        
        print('What is their birthday?')       
        bday = input()         
        birthdays[name] = bday        
        print('Birthday database updated.')
