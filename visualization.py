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
np.mean(data['pregs'])
np.mean(data['glucose'])
np.mean(data['bp'])
np.mean(data['thickness'])
np.mean(data['insulin'])
np.mean(data['bmi'])
np.mean(data['dia_pedig'])
np.mean(data['age'])
# Basic summary statistics
