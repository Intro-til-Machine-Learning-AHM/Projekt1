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
