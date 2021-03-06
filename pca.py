import numpy as np
from data_import import data

import matplotlib as mpl
#mpl.use("Qt4Agg")
import matplotlib.pyplot as plt

data_centered = data.copy()
# Delete class variables
class_var = data_centered["class"]
del data_centered["class"]
# Center around mean
data_centered -= np.mean(data_centered)

u, s, vh = np.linalg.svd(data_centered)
v = vh.T

plt.bar(np.arange(0,len(s)),(s*s)/np.sum(s*s))
plt.ylabel('Explained variance')
plt.xlabel('Principal components')
plt.show()
plt.plot(np.arange(0,len(s)),np.cumsum(s*s)/np.sum(s*s),'o-')
plt.ylabel('Explained variance')
plt.xlabel('Number of principal components')
plt.show()

d_pr = data_centered @ v
plt.plot(d_pr[class_var == 0,0], d_pr[class_var == 0,1], '.')
plt.ylabel('PC2')
plt.xlabel('PC1')
plt.plot(d_pr[class_var == 1,0], d_pr[class_var == 1,1], '.')
plt.show()

data_normalized = data_centered.copy()
data_normalized /= np.std(data_normalized)

u_n, s_n, vh_n = np.linalg.svd(data_normalized)
v_n = vh_n.T

plt.bar(np.arange(0,len(s_n)),(s_n**2)/np.sum(s_n**2))
plt.ylabel('Explained variance')
plt.xlabel('Principal components')
plt.show()
plt.plot(np.arange(0,len(s)),np.cumsum(s_n**2)/np.sum(s_n**2),'o-')
plt.ylabel('Explained variance')
plt.xlabel('Number of principal components')
plt.show()

d_pr_n = data_normalized @ v_n
plt.plot(d_pr_n[class_var == 0,0], d_pr_n[class_var == 0,1], '.')
plt.plot(d_pr_n[class_var == 1,0], d_pr_n[class_var == 1,1], '.')
plt.ylabel('PCA1')
plt.xlabel('PCA2')
plt.show()

plt.ylabel('Attribute index')
plt.xlabel('Direction')
plt.show()

line_up, = plt.plot(np.arange(8),v[:,0],label='PC1')
line_down, = plt.plot(np.arange(8),v[:,1], label='PC2')
plt.xlabel('Attribute index')
plt.ylabel('Direction')
plt.legend(handles=[line_up, line_down])
plt.show()

line_up, = plt.plot(np.arange(8),v_n[:,0],label='PC1')
line_down, = plt.plot(np.arange(8),v_n[:,1], label='PC2')
plt.xlabel('Attribute index')
plt.ylabel('Direction')
plt.legend(handles=[line_up, line_down])
plt.show()
