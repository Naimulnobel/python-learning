# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:03:32 2019

@author: Student mct
"""

import re
r = re.compile(r'nobel', re.I) 
m=r.search('nobel is a programmer').group()
print(m)
search1=r.search('Nobel is a programmer').group()
print(search1)