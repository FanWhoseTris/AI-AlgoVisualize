import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math


def calcu_angle(x, y, z):
    u = [y[0] - x[0], y[1] - x[1]]
    v = [z[0] - y[0], z[1] - y[1]]
    length_u = math.sqrt(u[0] ** 2 + u[1] ** 2)
    length_v = math.sqrt(v[0] ** 2 + v[1] ** 2)
    dot_product = u[0] * v[0] + u[1] * v[1]
    angle = math.acos(dot_product / (length_u * length_v))
    return math.degrees(angle)
def elbow_method(data, kmax):
    sse = []
    for k in range(1, kmax + 1):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
    poses = []
    for i in range(len(sse)):
        x = sse[i] % 1
        y = sse[i] // 1
        pos = [x, y]
        poses.append(pos)
    maxk = 180
    for i in range(len(poses)):
        if i >= 3:
            angle = calcu_angle(poses[i - 2], poses[i - 1], poses[i])
            if maxk >= angle:
                maxk = angle
                posmax = i
    return posmax
# Sử dụng ví dụ dữ liệu
datas = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5], [6, 8], [7, 9]])
kmaxx = 7
poses = elbow_method(datas, kmaxx)
print(poses)
# Áp dụng thuật toán K-elbow
#x = [2,1]
#y = [1,1]
#z = [1,2]
#print(calcu_angle(x,y,z))
