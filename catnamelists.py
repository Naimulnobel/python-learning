# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:40:26 2019

@author: Student mct
"""

catNames = []
while True:    
     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')    
     name = input()   
     if name == '':       
         break    
     catNames = catNames + [name] 
for name in catNames:   
    print('  ' + name)
  