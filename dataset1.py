#演習4 1.1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def true_function(x):
    x = np.asarray(x)  # スカラーでも配列でもOKにする
    y = np.sin(np.pi * x * 0.8) * 10
    return y

#演習4 1.2
np.random.seed(0)
x = np.random.uniform(-1,1,20)

y = true_function(x)

df = pd.DataFrame({
    "観測点": x,
    "真値": y
})

#print(df)#確認

#演習4 1.3
#ノイズ生成
noise = np.random.normal(0.0, np.sqrt(2.0), 20) / 2

#観測値
observed_y = y + noise

#新しい列追加
df["観測値"] = observed_y

print(df)

#グラフ描画
x_line = np.linspace(-1, 1, 1000)
y_line = true_function(x_line)

# 描画
plt.figure(figsize=(8, 5))

# 真の関数
plt.plot(x_line, y_line, label="true function")

# 真値
plt.scatter(x, y, color="red", label="true value")

# 観測値（ノイズ付き）
plt.scatter(x, observed_y, color="green", label="observed value")

plt.legend()
plt.grid()

# 保存
plt.savefig("ex1.3.png")

plt.show()