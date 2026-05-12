#演習4 1.1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def true_function(x):
    x = np.asarray(x)  # スカラーでも配列でもOKにする
    y = np.sin(np.pi * x * 0.8) * 10
    return y

#演習4 1.2
def create_true_dataset(n=20, seed=0):
    np.random.seed(seed)

    x = np.random.uniform(-1, 1, n)
    y = true_function(x)

    df = pd.DataFrame({
        "観測点": x,
        "真値": y
    })

    return df

#print(df)#確認

#演習4 1.3
#ノイズ生成
def add_noise(df, variance=2.0):
    n = len(df)

    noise = np.random.normal(
        0.0,
        np.sqrt(variance),
        n
    ) / 2

    observed_y = df["真値"] + noise

    df["観測値"] = observed_y

    return df

print(df)

#演習4 1.4
#TSV保存
def save_tsv(df, filename):
    df.to_csv(filename, sep="\t", index=False)

#演習4 1.5
def load_tsv(filename):
    df = pd.read_csv(filename, sep="\t")
    return df
#確認
print(type(df2)) #出力➡️<class 'pandas.core.frame.DataFrame'>