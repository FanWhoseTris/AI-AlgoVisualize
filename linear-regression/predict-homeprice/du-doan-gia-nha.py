import matplotlib.pyplot as mpl
import numpy as np
from sklearn import linear_model

#Data
DT = [70,85,100,120,150,90,110,80,95,130,115,140]
C = [2.5,3.2,3.7,4.2,5.1,3.0,4.0,2.8,3.5,4.5,4.1,4.9]

mpl.plot(DT,C,'ro')
mpl.xlabel("Diện tích (m2)")
mpl.ylabel("Giá bán (trăm triệu VND)")
mpl.title("Giá bán nhà dựa trên diện tích")

DT = np.array([DT]).T
C = np.array([C]).T
ones = np.ones_like(DT,dtype=np.int8)
#print(ones)
#print(str(DT.shape) + " " + str(C.shape))

A = np.concatenate((DT, ones), axis=1)
#print(A)
lr = linear_model.LinearRegression()
lr.fit(A,C)

x0 = np.array([70,150]).T
y0 = lr.coef_[0][0]*x0 + lr.intercept_

mpl.plot(x0,y0)

#TEST
xt = 140
yt = lr.coef_[0][0]*xt + lr.intercept_
mpl.plot(xt,yt,'ro',c='black')
print(yt)
mpl.show()