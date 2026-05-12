import datasets

X,Y = datasets.load_linear_example1()
ex_X =datasets.polynomial2_features(X)
print(ex_X)
print(Y)