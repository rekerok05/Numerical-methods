import numpy as np
from numpy import float32

A = np.array(
    [[1, 1.2, 2, 0.5],
     [1.2, 1, 0.4, 1.2],
     [0, 0.4, 2, 1.5],
     [0.5, 1.2, 1.5, 1]],
    float32)
eps = 0.5 * 10 ** -3
