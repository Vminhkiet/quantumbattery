import numpy as np

learning_rate = 0.1
delta = 0.001
max_iterations = 100
N=2
h=1
Y = np.array([[0, -1j],[1j, 0]])
X = np.array([[0, 1],[1, 0]])
I = np.eye(2)
XX=np.kron(X,X)
YY=np.kron(Y,Y)
dw=np.array([[0],[1]])
ps0=np.kron(dw,dw)