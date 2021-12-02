import numpy as np

import Variables as var


def iterationMethod(x1, x2, x3):
    # Формула

    alpha = 0.1 - var.K
    newX1 = np.around(((-2.9 - 1 * x2 - alpha * x3) / 2), decimals=6)
    newX2 = np.around((-0.7 - alpha * x1 + 0.72 * x3) / 5, decimals=6)
    newX3 = np.around((-9.86 + 1.2 * x1 - 3 * x2) / 1.7, decimals=6)

    d1 = abs(newX1 - x1)
    d2 = abs(newX2 - x2)
    d3 = abs(newX3 - x3)

    print(f"x1 = {newX1} \tx2 = {newX2} \tx3 = {newX3} \te = {np.around(max([d1, d2, d3]), decimals=5)}")

    if (max([d1, d2, d3]) > var.eps):
        iterationMethod(newX1, newX2, newX3)


def makeMatrixB(matrixA):
    B = np.zeros((3, 3))
    for i in range(0, 3):
        for j in range(0, 3):
            if i != j:
                B[i, j] = -matrixA[i, j] / matrixA[i, i]
    return B


# x1 = (1*x2 - 0.1*x3 - 2.9)/2
# x2 = (-0.1*x1 - 0.72*x3 - 0.7)/5
# x3 = (1.2*x1 - 3*x2 - 9,86)/1.7

def part1():
    B = makeMatrixB(var.A)
    d = np.array([var.f[i] / var.A[i, i] for i in range(0, 3)])
    print(f"B = \n{B}\nd = \n{d}\n")
    iterationMethod(*d)


def main():    part1()


if __name__ == "__main__":
    main()
