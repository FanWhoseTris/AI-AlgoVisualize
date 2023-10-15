import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model

#Data
TL = [5,3,7,6,8,4,9,5,6,7]
TP = [2,1,4,3,5,2,6,3,4,5]
M = [8.5,6.0,9.0,7.5,9.5,7.0,9.2,8.0,8.8,9.4]

#Draw data in 3d
ax = mpl.figure().add_subplot(111, projection = '3d')
ax.plot(TL,TP,M,'ro')
#ax.scatter3D(TL,TP,M)
# Đặt tên cho trục x, y và z
ax.set_xlabel('Thời gian học')
ax.set_ylabel('Thời gian chơi')
ax.set_zlabel('Điểm thi')
# Đặt tiêu đề cho đồ thị
ax.set_title('Dự Đoán Điểm Thi')

#CACH 1:
'''''
TL = np.array([TL]).T
TP = np.array([TP]).T
M = np.array([M]).T
ones = np.ones_like(TL,dtype = np.int8)

A = np.concatenate((TL,TP,ones),axis = 1)
print(A)

x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(M)

#Draw mp
x = np.linspace(1, 7, 100)
y = np.linspace(1, 7, 100)
x, y = np.meshgrid(x, y)
z = x[0][0]*x+x[1][0]*y+x[2][0]
ax.plot_surface(x, y, z, cmap='viridis')

xt = 8
yt = 2
zt = x[0][0]*xt+x[1][0]*yt+x[2][0]
ax.scatter3D(xt,yt,zt,c='black')
print(zt)
'''''
#Cach 2
#'''''
TL = np.array([TL]).T
TP = np.array([TP]).T
M = np.array([M]).T
ones = np.ones_like(TL,dtype = np.int8)
A = np.concatenate((TL,TP,ones),axis = 1)
#print(A)
lr = linear_model.LinearRegression()
lr.fit(A,M)
print(lr.coef_[0][0])
print(lr.coef_[0][1])
print(lr.intercept_)

#Draw mp
x = np.linspace(1, 7, 100)
y = np.linspace(1, 7, 100)
x, y = np.meshgrid(x, y)
z = lr.coef_[0][0]*x+lr.coef_[0][1]*y+lr.intercept_
ax.plot_surface(x, y, z, cmap='viridis')

#TEST
xt = 6
yt = 4
zt = lr.coef_[0][0]*xt+lr.coef_[0][1]*yt+lr.intercept_
ax.scatter3D(xt,yt,zt,c='black')

#'''''
mpl.show()