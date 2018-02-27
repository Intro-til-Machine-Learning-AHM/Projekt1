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
fig = plt.figure()
#plt.hist(data_copy["pregs"],bins=fig = plt.figure())

ax1 = fig.add_subplot(421)
ax1.set_title("pregs")
plt.hist(data_copy["pregs"],bins=17)

ax2 = fig.add_subplot(422)
ax2.set_title("glucose")
plt.hist(data_copy["glucose"])

ax3 = fig.add_subplot(423)
ax3.set_title("bp")
plt.hist(data_copy["bp"])

ax4 = fig.add_subplot(424)
ax4.set_title("thickness")
plt.hist(data_copy["thickness"])

ax5 = fig.add_subplot(425)
ax5.set_title("insulin")
plt.hist(data_copy["insulin"])

ax6 = fig.add_subplot(426)
ax6.set_title("bmi")
plt.hist(data_copy["bmi"])

ax7 = fig.add_subplot(427)
ax7.set_title("dia_pedig")
plt.hist(data_copy["dia_pedig"])

ax8 = fig.add_subplot(428)
ax8.set_title("age")
plt.hist(data_copy["age"])

plt.show()
