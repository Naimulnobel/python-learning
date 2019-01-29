# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:00:18 2019

@author: Student Mct
"""
import statistics
import matplotlib.pyplot as plt
number_of_chocolate=[2,3,4,5,5,6,7,10,12,15,20,22,25,30]
age_range=[0,5,10,15,20,25,30]
plt.hist(number_of_chocolate,age_range,histtype='bar')
plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram')
plt.legend()
plt.show()
mean1=statistics.mean(number_of_chocolate)
print(mean1)
median1=statistics.median(number_of_chocolate)
print(median1)
mode1=statistics.mode(number_of_chocolate)
print(mode1)