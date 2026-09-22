import numpy as np

X = np.array([2, 1, -1])

W = np.array([
    [1, 0],
    [0, 2],
    [3, 1]
])

Y = np.dot(X, W)

print(Y)