import numpy as np
from numpy import float32

D = np.array(
    [[3.1, 1.0, 2.1], [1.0, 3.6, 2.1], [2.1, 2.1, 4.1]],
    float32)
C = np.identity(4, dtype=float32)
f = np.array([[2.1], [1.0], [1.1]], dtype=float32)
K = 1
A = np.array(D + C.dot(K), dtype=float32)
