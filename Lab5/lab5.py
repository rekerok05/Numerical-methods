import numpy as np
from numpy import set_printoptions
from sympy.solvers import solve
from sympy import Symbol
import Variables as var


def makeFrobenius(matrix):
    # n = len(matrix)
    # a = np.array(matrix)
    # At = a.transpose()  # находим Аt
    # a = np.dot(At, a)  # перемножаем А на Аt, теперь А - симметрическая
    # f = a
    # s = np.identity(n)
    # for i in range(0, n - 1):
    #     m = np.identity(n)
    #     m[n - 2 - i][:] = f[n - 1 - i][:]  # выделяем M^(-1)
    #     f = np.dot(m, f)  # умножаем A на M^(-1) слева
    #     f = np.dot(f, np.linalg.inv(m))  # умножаем A на M справа
    #     s = np.dot(s, np.linalg.inv(m))  # находим S
    # return f, s

    # -----------------------------------
    m3 = np.identity(4)
    m3[2] = -var.A[3] / var.A[3][2]
    m3[2][2] /= -var.A[3][2]
    m3minus = np.identity(4)
    m3minus[2] = var.A[3]
    A1 = np.dot(np.dot(m3minus, var.A), m3)
    printValue("m3", m3)
    printValue("m3minus", m3minus)
    printValue("A1", A1)
    print("\n")
    # -----------------------------------
    m2 = np.identity(4)
    m2[1] = -A1[2] / A1[2][1]
    m2[1][1] /= -A1[2][1]
    m2minus = np.identity(4)
    m2minus[1] = A1[2]
    A2 = np.dot(np.dot(m2minus, A1), m2)
    printValue("m2", m3)
    printValue("m3minus", m3minus)
    printValue("A2", A2)
    print("\n")
    # -----------------------------------
    m1 = np.identity(4)
    m1[0] = -A2[1] / A2[1][0]
    m1[0][0] /= -A2[1][0]
    m1minus = np.identity(4)
    m1minus[0] = A2[1]
    A3 = np.dot(np.dot(m1minus, A2), m1)
    printValue("m1", m1)
    printValue("m1minus", m1minus)
    printValue("A3", A3)
    print("\n")
    S = np.dot(np.dot(m3, m2), m1)
    printValue("S", S)
    return np.around(A3, decimals=5), S


def printValue(name, value):
    print(f"{name} = \n{value}")


def part1():
    print("part 1")
    frobenius, S = makeFrobenius(var.A)
    print(frobenius)
    p = frobenius[0, :]
    print(p)
    Lambda = np.roots([1, -p[0], -p[1], -p[2], -p[3]])
    printValue("Lambda", Lambda)
    print("\n")
    # ---------------------------
    y1 = np.array([Lambda[0] ** 3, Lambda[0] ** 2, Lambda[0], 1])
    y2 = np.array([Lambda[1] ** 3, Lambda[1] ** 2, Lambda[1], 1])
    y3 = np.array([Lambda[2] ** 3, Lambda[2] ** 2, Lambda[2], 1])
    y4 = np.array([Lambda[3] ** 3, Lambda[3] ** 2, Lambda[3], 1])
    printValue("y1", y1)
    printValue("y2", y2)
    printValue("y3", y3)
    printValue("y4", y4)
    print("\n")
    # --------------------------
    x1 = np.dot(S, y1)
    x2 = np.dot(S, y2)
    x3 = np.dot(S, y3)
    x4 = np.dot(S, y4)
    printValue("x1", x1)
    printValue("x2", x2)
    printValue("x3", x3)
    printValue("x4", x4)
    print("\n")
    # ---------------------------
    print(np.dot(frobenius, y1))
    print(Lambda[0] * y1)
    print(np.dot(frobenius, y2))
    print(Lambda[1] * y2)
    print(np.dot(frobenius, y3))
    print(Lambda[2] * y3)
    print(np.dot(frobenius, y4))
    print(Lambda[3] * y4)
    print("\n")
    # ---------------------------
    print(np.dot(var.A, x1))
    print(Lambda[0] * x1)
    print(np.dot(var.A, x2))
    print(Lambda[1] * x2)
    print(np.dot(var.A, x3))
    print(Lambda[2] * x3)
    print(np.dot(var.A, x4))
    print(Lambda[3] * x4)
    print("\n")


def main():
    part1()


if __name__ == "__main__":
    main()
