# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:41:44 2019

@author: Student mct
"""

spam=['dog','cat','pooka']
spam=spam+['kutta']
print(spam)
spam.insert(3,'kodu')
print(spam)
spam.index('dog')
spam.reverse()
print( 'upateded list:',spam )
spam.remove('dog')
print('upateded list:',spam)
counter=spam.count('cat')
print(counter)
list1=spam.copy()
print(list1)
spam.clear()
print(spam)

