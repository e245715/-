import numpy as np
import matplotlib.pyplot as plt
from dataset1 import true_function


# xを生成
x = np.linspace(-1, 1, 100)

# yを計算
y = true_function(x)

# ex1.1.pngグラフ描く
plt.plot(x, y, label="y = sin(pi * x * 0.8) * 10")

plt.legend()

# 軸ラベル
plt.xlabel("x")
plt.ylabel("y")

# タイトル名
plt.title("True Function")

# 画像保存
plt.savefig("ex1.1.png")

# 表示
plt.show()

# ex1.2.pngグラフを描く
x_line = np.linspace(-1,1,1000)
y_line = true_function(x_line)

plt.figure(figsize=(8,5))

plt.plot(x_line, y_line, label="true function")

plt.scatter(x, y, color="red", label="samples")

plt.legend()
plt.grid()

plt.savefig("ex1.2.png")

plt.show()