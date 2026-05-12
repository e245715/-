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

#演習4 1.4
#TSV保存
df.to_csv("ex1.3.tsv", sep="\t", index=False)

#演習4 1.5
#DataFrame型で読み込む
df2 = pd.read_csv("ex1.3.tsv", sep="\t")
#確認
print(type(df2)) #出力➡️<class 'pandas.core.frame.DataFrame'>