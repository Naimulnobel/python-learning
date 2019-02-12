# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 14:19:18 2019

@author: DIU MCT
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv('market_fact.csv')

#plt.boxplot(df['Order_Quantity'])
plt.subplot(1,2,1)
plt.boxplot(df['Sales'])
plt.subplot(1,2,2)
plt.boxplot(df['Sales'])
plt.yscale('log')
plt.show()
plt.hist(df['Sales'])
plt.yscale('log')
plt.show()
plt.scatter(df['Sales'],df['Profit'])
plt.show()