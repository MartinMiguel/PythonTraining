import numpy as np

A = np.array([1, 2, 3])

N = A.size
B = np.pad(np.diag(A), ((0, N), (0, 0)), mode='constant')