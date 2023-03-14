import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

'''df = pd.read_csv('fluiding_#1.csv')
c = len(df.columns) - 1
time = 0

for i in range(c - 1):
    t1 = df.iat[0, i + 1]
    t2 = df.iat[0, i + 2]
    delta = int(t2 - t1)
    for k in range(delta):
        v1 = df.iloc[:, i + 1]
        v2 = df.iloc[:, i + 2]
        df['#' + str(int(t1 + k))] = (v2 - v1) / (t2 - t1) * k + v1
        time = int(t1 + k + 1)
df['#' + str((time))] = df.iloc[:, c]
#df.to_csv('result.csv')'''

df = pd.read_csv('result.csv')
time = 2094

fig = plt.figure()
ax = fig.add_subplot()
ims = []
def gif(j):
    ax.cla()
    ax.set_xlabel('position y [cm]', size = 15)
    ax.set_ylabel('thickness [μm]', size = 15)
    ax.tick_params(axis='y', length = 8, direction='in', labelsize=12)
    ax.tick_params(axis='x', length = 8, direction='in', labelsize=12)
    ax.set_xlim(-7, 7)
    ax.set_ylim(0, 120)
    ax.set_title('time = ' + "{:.2f}".format(j / 10) + ' [min]', size = 15)
    graph = ax.plot(df['x'], df['#' + str(6 * j)], ls = '-', color = 'darkblue', marker = 'o')
    ims.append(graph)
#anim = animation.ArtistAnimation(fig, ims, interval = 10)
anim= animation.FuncAnimation(fig, gif, frames = range(int(time / 6)), interval = 5)
plt.show()
anim.save('rez.gif')
