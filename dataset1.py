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

x_line = np.linspace(-1,1,1000)
y_line = true_function(x_line)

plt.figure(figsize=(8,5))

plt.plot(x_line, y_line, label="true function")

plt.scatter(x, y, color="red", label="samples")

plt.legend()
plt.grid()

plt.savefig("ex1.2.png")

plt.show()
