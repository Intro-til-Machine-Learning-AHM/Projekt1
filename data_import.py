import pandas as pd
import numpy as np

names = ["pregs", "glucose", "bp", "thickness", "insulin", "bmi", "dia_pedig", "age", "class"]
data_raw = pd.read_csv("diadata.csv", header=None, names=names)

# Delete rows with missing data
non_zero = ["glucose", "bp", "thickness", "bmi"]
mask = np.logical_not(np.any(data_raw[non_zero] == 0,1))
data = data_raw[mask]
