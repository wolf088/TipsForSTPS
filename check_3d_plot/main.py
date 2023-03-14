import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#f_i = 'input/G_validation_waseda_#2.csv'
f_j = 'input/W_Curve_convex_60deg_R250.csv'
#df = pd.read_csv(f_i)
df2 = pd.read_csv(f_j)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("x", size = 14, color = "r")
ax.set_ylabel("y", size = 14, color = "r")
ax.set_zlabel("z", size = 14, color = "r")
#ax.set_xlim(-5900, -4500)
#ax.set_ylim(0, 1400)
#ax.set_zlim(-700, 700)

#x = df['x_pg']
#y = df['y_pg']
#z = df['z_pg']
#a = df['x_pd']
#b = df['y_pd']
#c = df['z_pd']
x1 = df2['x_pw']
y1 = df2['y_pw']
z1 = df2['z_pw']

ax.scatter(x1, y1, z1, c = "black", marker=".")
#ax.scatter(x, y, z, c = "blue", marker=".")
#ax.scatter(a, b, c, c = "red", marker=".")
plt.show()