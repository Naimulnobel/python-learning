# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:56:20 2019

@author: DIU MCT
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
x=np.linspace(0,10,20)
y=(x*2)
plt.xlabel('Current')
plt.ylabel('Voltage')
plt.title("yo")
#plt.xlim([20,80])
#plt.ylim([200,800])
plt.plot(x,y,'b+')
plt.show()