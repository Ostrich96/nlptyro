import numpy as np

W1 = np.random.randn(2)
print(W1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

print(sigmoid(W1))