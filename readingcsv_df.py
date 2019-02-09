# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:23:39 2019

@author: DIU MCT
"""
import csv
import pandas as pd
import numpy as np
df1=pd.read_csv('weather_data.csv')
dl1=pd.DataFrame([['a',1],['b',2]],columns=['col','number'])
dl2=pd.DataFrame([['d',3,11],['e',4,10],['f',5,9]],columns=['seies','number','temp'])
dl3=pd.concat([dl1,dl2],axis=0,ignore_index=True)
dl4=pd.concat([dl1,dl2],axis=1)
print(dl3)
print(dl4)


print(dl1)
print(df1)