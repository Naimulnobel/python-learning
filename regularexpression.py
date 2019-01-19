# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:00:42 2019

@author: Student mct
"""

import re
text=input()
phonNum=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
mo=phonNum.search(text)
print('phon number is:'+mo.group())

