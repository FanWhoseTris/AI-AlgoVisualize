import numpy as np
import matplotlib.pyplot as plt

#Data collection
# height (cm)
X = [147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]
# weight (kg)
y = [ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]
plt.plot(X,y,'ro')
#Static
#plt.figure(1)
#plt.bar(X,y)
#plt.xlabel('Height (cm)')
#plt.ylabel('Weight (kg)')
#plt.title('Thống Kê data')

#Preprocessing data
# height (cm)
X = np.array([X]).T
# weight (kg)
y = np.array([y]).T

#Visualization
#plt.plot(X, y, 'ro')
#plt.axis([140, 190, 45, 75])
#plt.xlabel('Height (cm)')
#plt.ylabel('Weight (kg)')
#plt.title('Predict Weight')
#plt.show()

#Build model#
#print(X.shape)
#print(y.shape)
ones = np.ones_like(X)
MA = np.concatenate((X,ones),axis = 1)
print(MA)
x = np.linalg.inv(MA.T.dot(MA)).dot(MA.T).dot(y)
print(x)
x0 = x[0][0]
x1 = x[1][0]
print(x0," ",x1)

xd = np.array([145,185]).T
yd = x0*xd + x1
print(xd," ",yd)
plt.plot(xd,yd)

#TEST MODEL
xt = 160
yt = x0*xt + x1
print(yt)

plt.show()



