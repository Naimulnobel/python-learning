# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:19:23 2019

@author: NOBEL
"""

text="nobel"
savetext= open('nobel.txt','w')
savetext.write(text)
savetext.close()
text1="\nhe is a programmer"
appendtext=open ('nobel.txt','a')
appendtext.write(text1)
appendtext.close()
readtext= open('nobel.txt','r').read()
print(readtext)

