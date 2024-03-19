import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# data = pd.read_csv('e_field.csv')
 
# Transform it to a long format
# df=data.unstack().reset_index()
# df.columns=["X","Y","Z"]

# And transform the old column name in something numeric
# df['X']=pd.Categorical(df['X'])
# df['X']=df['X'].cat.codes
# print(df['Z'])
x = np.linspace(-2,2,500)
y = np.linspace(-2,2,500)
X, Y = np.meshgrid(x,y)
Z = np.sin(X) + np.cos(Y)
plt.ion()
plt.figure()
plt.contour(X,Y,Z)
plt.colorbar()
plt.clf()
plt.contourf(X,Y,Z)
plt.colorbar()
plt.clf()
plt.contourf(X,Y,Z,levels=30)
plt.contourf(X,Y,Z,levels=30, vmin=-1, vmax=0.5)
plt.show(block=True)
