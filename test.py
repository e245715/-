import datasets
import regression

""""
X,Y = datasets.load_linear_example1()
ex_X =datasets.polynomial2_features(X)
print(ex_X)
print(Y)
"""

X,Y = datasets.load_linear_example1()
ex_X =datasets.polynomial3_features(X)
print(ex_X)
print(Y)

model = regression.RidgeRegression(alpha=0.5)
model = regression.RidgeRegression() #default:alpha=0.1
model.fit(ex_X,Y)
print(model.theta)
print(model.predict(ex_X))
print(model.score(ex_X,Y)) #RSS

