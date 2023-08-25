import numpy as np
import matplotlib.pyplot as mpl

A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,12]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,5.7638152914458765]

mpl.plot(A,b,'ro')
A = np.array([A]).T
b = np.array([b]).T
ones = np.ones((A.shape[0],1),dtype = np.int8)
A = np.concatenate((A,ones),axis = 1)
#print(A)
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
x0 = np.array([1,50], dtype = np.int8).T
y0 = x0*x[0] + x[1]

mpl.plot(x0,y0)
#print(x)

mpl.show()