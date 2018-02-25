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
# Assign mean values
print(np.mean(data['pregs']))
print(np.mean(data['glucose']))
print(np.mean(data['bp']))
print(np.mean(data['thickness']))
print(np.mean(data['insulin']))
print(np.mean(data['bmi']))
print(np.mean(data['dia_pedig']))
print(np.mean(data['age']))
# Assign variance
np.var(data['pregs'])
np.var(data['glucose'])
np.var(data['bp'])
np.var(data['thickness'])
np.var(data['insulin'])
np.var(data['bmi'])
np.var(data['dia_pedig'])
np.var(data['age'])
# Assign covariance
covmatrix=np.cov(data)
# Basic summary statistics
#print(data.describe())
print(covmatrix[0])
