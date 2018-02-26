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
#plt.plot(d_pr[class_var == 0,0], d_pr[class_var == 0,1], '.')
#plt.plot(d_pr[class_var == 1,0], d_pr[class_var == 1,1], '.')
#plt.show()
plt.figure()
plt.ylabel('Explained variance')
plt.xlabel('Principal components')
plt.axis([-0.3, 7, 0, 1.2])
plt.plot(np.cumsum(s*s)/np.sum(s*s))
plt.show()
print(np.sum(s[0:2]**2)/(np.sum(s**2)))
