import numpy as np
import pandas as pd
import math

Rx = -90
Ry = -27
Rz = -31

def rotM(p):
    # 回転行列を計算する
    px = p[0]
    py = p[1]
    pz = p[2]
    # 物体座標系の 1->2->3 軸で回転させる
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(px), np.sin(px)],
                   [0, -np.sin(px), np.cos(px)]])
    Ry = np.array([[np.cos(py), 0, -np.sin(py)],
                   [0, 1, 0],
                   [np.sin(py), 0, np.cos(py)]])
    Rz = np.array([[np.cos(pz), np.sin(pz), 0],
                   [-np.sin(pz), np.cos(pz), 0],
                   [0, 0, 1]])
    R = Rz.dot(Ry).dot(Rx)
    return R

p = np.array([Rx * math.pi / 180, Ry * math.pi / 180, Rz * math.pi / 180])
v = np.array([1/math.sqrt(2), 0, -1/math.sqrt(2)])
v = np.dot(rotM(p).T, v)
v_norm = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
print(v, v_norm)