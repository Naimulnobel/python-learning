# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:24:11 2019

@author: DIU MCT
"""
import pandas as pd
import numpy as np
temp= np.random.randint(low=20,high=100,size=[20,])
name=np.random.choice(['murgi','goru','chagol','hati'],20)
random=np.random.choice([10,11,13,14],20)
#a=list(zip(temp,name,random))
#df=pd.DataFrame(data=a,columns=['temp','name','random'])
df=pd.DataFrame({'temp':temp,'name':name,'random':random})
print(df)
print(df.head())
print(df.iloc[[0,1]])
print(df.loc[[0,1]])

