# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:15:00 2018

@author: andre
"""

# Import packagaes
import sys
import os
import numpy as np
import pandas as pd
Load data
df=pd.read_csv('diadata.csv', sep=',',header=None)
df.values
print(df)
print(os.getcwd())
print(np.array([1,2,3]))
