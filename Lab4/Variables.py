import numpy as np
from numpy import float32

f = np.array([[-2.9], [-0.7], [-9.86]])

K = 2
alpha = 0.1 * K
eps = 0.00005

A = np.array(
    [[2, 1, alpha], [alpha, 5, 0.72], [-1.2, 3, 1.7]],
    float32)


