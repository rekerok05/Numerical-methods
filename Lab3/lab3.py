import math
import numpy as np
import numpy.linalg
import Variables as Var
from Lab1.lab1 import *


def is_symmetric(matrix):
    if np.array_equal(matrix, np.transpose(matrix)):
        print(f"\nМатрица является симметрической:\n{matrix}\n")
        return True
    else:
        return False


def is_positive(matrix):
    if matrix[0, 0] > 0 and np.linalg.det(matrix[:-1, :-1]) > 0 and np.linalg.det(matrix) > 0:
        print("\nМатрица является положительно определенной:")
        print(f"{matrix[0, 0]} > 0\n")
        print(f"{matrix[:-1, :-1]}  = {np.linalg.det(matrix[:-1, :-1])} > 0\n")
        print(f"{matrix} = {np.linalg.det(matrix)} > 0\n")
        return True
    else:
        return False


def getL(A):
    L = np.eye(3)
    L[0, 0] = math.sqrt(A[0, 0])
    L[1, 0] = A[1, 0] / L[0, 0]
    L[2, 0] = A[2, 0] / L[0, 0]
    L[1, 1] = math.sqrt(A[1, 1] - math.pow(L[1, 0], 2))
    L[2, 1] = (A[2, 1] - L[2, 0] * L[1, 0]) / (L[1, 1])
    L[2, 2] = math.sqrt(A[2, 2] - math.pow(L[2, 0], 2) - math.pow(L[2, 1], 2))
    print(f"L = \n{L}\n")
    return L


def find_solution_y(L, f):
    solution = np.array([0] * len(L), float)
    solution[0] = f[0] / L[0, 0]
    solution[1] = (f[1] - L[1, 0] * solution[0]) / L[1, 1]
    solution[2] = (f[2] - L[2, 1] * solution[1] - L[2, 0] * solution[0]) / L[2, 2]
    return solution


def find_solution_x(L, f):
    solution = np.array([0] * len(L), float)
    solution[2] = f[2] / L[2, 2]
    solution[1] = (f[1] - L[1, 2] * solution[2]) / L[1, 1]
    solution[0] = (f[0] - L[0, 2] * solution[2] - L[0, 1] * solution[1]) / L[0, 0]
    return solution


def main():
    is_symmetric(Var.A)
    is_positive(Var.A)

    print("Разложение A = L * L^T\n")
    L = getL(Var.A)
    LT = np.transpose(L)
    print(f"L^T = \n{LT}\n")
    LLT = np.dot(L, LT)
    print(f"Проверка L * L^T = A: \n{LLT}\n")

    # обратный метод гаусса
    y = find_solution_y(L, Var.f)
    print(f"Y = {y}\n")
    x = find_solution_x(LT, y)
    print(f"X = {x}\n")

    # вычислить веторы невязки (нормы)
    R = discrepancy_vector((Var.A, Var.f, x))
    norm_discrepancy_vector(R)

if __name__ == "__main__":
    main()
