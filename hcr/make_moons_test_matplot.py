import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

# 生成数据（100个样本，添加少量噪声）
X, y = make_moons(n_samples=100, noise=0.1, random_state=42)

# 可视化
plt.figure(figsize=(8, 6))
# 用不同颜色绘制两个类别的样本
plt.scatter(X[y==0, 0], X[y==0, 1], color='red', marker='o', label='类别 0')
plt.scatter(X[y==1, 0], X[y==1, 1], color='blue', marker='s', label='类别 1')
plt.xlabel('特征 1')
plt.ylabel('特征 2')
plt.legend()
plt.title('make_moons 生成的数据集')
plt.show()
