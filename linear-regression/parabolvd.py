import numpy as np
import matplotlib
import matplotlib.pyplot as mpl

# random data
b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
mpl.plot(A,b,'ro')
A = np.array([A]).T
b = np.array([b]).T
ones = np.ones_like(A, dtype=np.int8)
A2 = A**2

A = np.concatenate((A2,A,ones), axis = 1)
#print(A)

x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)

x0 = np.linspace(1,25,10000)
y0 = (x0**2)*x[0][0]+x[1][0]*x0+x[2][0]


mpl.plot(x0,y0)

x_test = 12
y_test = x_test*x[0][0] + x[1][0]
print(y_test)
mpl.show()