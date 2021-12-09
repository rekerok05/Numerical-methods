import numpy as np
from numpy import inf

import Variables as var


# x1 = (-1*x2 - 0.1*x3 - 2.9)/2
# x2 = (-0.1*x1 - 0.72*x3 - 0.7)/5
# x3 = (0.5*x1 - 2*x2 - 21.92)/2.78

def iterationMethod(x1, x2, x3):
    # Формула

    alpha = 0.1 * var.K
    newX1 = np.around(((-2.9 - 1 * x2 - alpha * x3) / 2), decimals=6)
    newX2 = np.around((-0.7 - alpha * x1 + 0.72 * x3) / 5, decimals=6)
    newX3 = np.around((-21.92 + 0.5 * x1 - 2 * x2) / 2.78, decimals=6)

    d1 = np.linalg.norm([x1, x2, x3], ord=inf)
    d2 = np.linalg.norm([newX1, newX2, newX3], ord=inf)

    print(f"x1 = {newX1} \tx2 = {newX2} \tx3 = {newX3} \te = {np.around(abs(d1 - d2), decimals=5)}")

    if (abs(d1 - d2) > var.eps):
        iterationMethod(newX1, newX2, newX3)


def printValue(name, value):
    print(f"{name} = \n{value}\n")


def makeMatrixB(matrixA):
    B = np.zeros((3, 3))
    for i in range(0, 3):
        for j in range(0, 3):
            if i != j:
                B[i, j] = -matrixA[i, j] / matrixA[i, i]
    return B


def part1():
    printValue("A", var.A)
    printValue("f", var.f)
    var.A[2] = var.A[2] * 2 + var.A[0] - var.A[1]
    var.f[2] = var.f[2] * 2 + var.f[0] - var.f[1]
    printValue("new A", var.A)
    printValue("new f", var.f)

    # B = makeMatrixB(var.A)
    # printValue("B", B)
    # d = np.array([var.f[i] / var.A[i, i] for i in range(0, 3)])
    # printValue("d", d)
    iterationMethod(*var.f)


def main():
    part1()


if __name__ == "__main__":
    main()