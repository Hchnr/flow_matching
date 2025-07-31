# moons_plotext.py
import plotext as plt
from sklearn.datasets import make_moons

# 生成数据
X, y = make_moons(n_samples=500, noise=0.1, random_state=42)

# 分离两类数据
x0, y0 = X[y == 0, 0], X[y == 0, 1]
x1, y1 = X[y == 1, 0], X[y == 1, 1]

# 终端绘图
plt.clf()  # 清除上一次绘图
plt.scatter(x0, y0, label='Class 0', marker='o', color='blue')
plt.scatter(x1, y1, label='Class 1', marker='●', color='red')
plt.title("sklearn make_moons - Terminal Visualization")
plt.xlabel("X1")
plt.ylabel("X2")
# plt.legend()
plt.plot_size(100, 80)  # 设置终端绘图大小
plt.show()
