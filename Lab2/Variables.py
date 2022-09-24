import numpy as np

D = np.array(
    [[6.22, 1.42, -1.72, 1.91],
     [1.44, 5.33, 1.11, -1.82],
     [-1.72, 1.11, 5.24, 1.42],
     [1.91, -1.82, 1.42, 6.55]],
    dtype=float)

first_column = np.array([1, 0, 0, 0],
             dtype=float)

second_column = np.array([0, 1, 0, 0],
             dtype=float)

third_column = np.array([0, 0, 1, 0],
             dtype=float)

fourth_column = np.array([0, 0, 0, 1],
             dtype=float)

K = 2
C = np.identity(n=4,
                dtype=float)
A = D + K * C
