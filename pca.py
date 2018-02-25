import numpy as np
from data_import import data as data_cleaned

import matplotlib as mpl
#mpl.use("Qt4Agg")
import matplotlib.pyplot as plt
#plt.ion()

# Delete class variables
class_var = data_cleaned["class"]
del data_cleaned["class"]

# Center around mean
data_cleaned -= np.mean(data_cleaned)

u, s, vh = np.linalg.svd(data_cleaned)
v = vh.T

d_pr = data_cleaned @ v
plt.plot(d_pr[class_var == 0,0], d_pr[class_var == 0,1], '.')
plt.plot(d_pr[class_var == 1,0], d_pr[class_var == 1,1], '.')
plt.show()
