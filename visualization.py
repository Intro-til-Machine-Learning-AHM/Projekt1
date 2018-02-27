# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:15:00 2018

@author: andre
"""

# Import packagaes and data
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_import import data
from scipy.stats import norm
from scipy import stats
# Load data
df=pd.read_csv('diadata.csv', sep=',',header=None)
df.values
 #Assign mean values
print(np.var(data['pregs']))
print(np.var(data['glucose']))
print(np.var(data['bp']))
print(np.var(data['thickness']))
print(np.var(data['insulin']))
print(np.var(data['bmi']))
print(np.var(data['dia_pedig']))
print(np.var(data['age']))
 #Assign variance
np.var(data['pregs'])
np.var(data['glucose'])
np.var(data['bp'])
np.var(data['thickness'])
np.var(data['insulin'])
np.var(data['bmi'])
np.var(data['dia_pedig'])
np.var(data['age'])
# Assign covariance
Covariance=data.corr().round(2)
#print(Covariance)
#print(type(Covariance))
#print(Covariance.to_latex())
# Basic summary statistics
#print(data.mean())

# Boxplots code
data_copy = data.copy()
del data_copy["class"]
#plt.boxplot(data_copy.as_matrix())
range_data = data.max()-data.min()
#print(range_data)
#fig = plt.figure()
#plt.hist(data_copy["pregs"],bins=fig = plt.figure())

for c in data.columns:
    ax = plt.figure()
    plt.title(c)
    plt.hist(data[c], normed=True)
    (mu,sigma) = norm.fit(data[c])
    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(data[c]))
    pdf_g = stats.norm.pdf(lnspc, mu, sigma)
    plt.plot(lnspc, pdf_g, label="Norm")
plt.show()

plt.show()
