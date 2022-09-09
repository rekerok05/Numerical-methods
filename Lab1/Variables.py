import numpy as np

D = np.array(
    [[6.22, 1.42, -1.72, 1.91],
     [1.44, 5.33, 1.11, -1.82],
     [-1.72, 1.11, 5.24, 1.42],
     [1.91, -1.82, 1.42, 6.55]],
    dtype=float)
f = np.array([7.53, 6.06, 8.05, 8.06],
             dtype=float)
K = 2
C = np.identity(n=4,
                dtype=float)
A = D + K * C
