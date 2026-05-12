import numpy as np

def true_function(x):
    x = np.asarray(x)  # スカラーでも配列でもOKにする
    y = np.sin(np.pi * x * 0.8) * 10
    return y