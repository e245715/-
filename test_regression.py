import regression
import datasets
import importlib

"""
#ver.1テスト
model = regression.LinearRegression()
print(model.x)
"""

#ver.2テスト
importlib.reload(regression)
importlib.reload(datasets)

X,Y = datasets.load_linear_example1

model = regression.LinearRegression()
model.fit(X,Y)
print(model.theta)

