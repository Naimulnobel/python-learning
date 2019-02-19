# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:44:21 2019

@author: DIU MCT
"""
#from sklearn.preprocessing import OneHotEncoder
#from sklearn.preprocessing import LabelEncoder
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
dataset= pd.read_csv(r'Iris.csv', encoding='utf-8')
print(dataset.head())
print(dataset["Species"].value_counts())
x=dataset.groupby('Species').count()
print(x)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
cols = dataset.columns
features = cols[0:4]
labels = cols[4]
print(features)
print(labels)
data_norm = pd.DataFrame(dataset)

for feature in features:
    dataset[feature] = (dataset[feature] - dataset[feature].mean())/dataset[feature].std()


print("Averages")
print(dataset.mean())

print("\n Deviations")

print(pow(dataset.std(),2))