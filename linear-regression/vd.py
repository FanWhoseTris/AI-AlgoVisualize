import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = np.linspace(1, 10, 25)
y = 2 * x + np.random.normal(0, 2, 25)

model = LinearRegression()
model.fit(x.reshape(-1, 1), y.reshape(-1, 1))
y_pred = model.predict(x.reshape(-1, 1))

plt.figure(figsize=(8, 6))
plt.scatter(x, y, label="Dữ liệu thực tế")
plt.plot(x, y_pred, color='red', label="Linear Regression")
plt.xlabel("Số điểm")
plt.ylabel("Số lượng từ vựng")
plt.title("Linear Regression Visualization")
plt.legend()
plt.grid(True)
plt.show()
