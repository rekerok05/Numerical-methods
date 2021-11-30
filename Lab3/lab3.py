import math
import numpy as np
import numpy.linalg
from Lab1 import fuctions

import Variables as var


def make_identity(matrix):
    # перебор строк в обратном порядке
    for nrow in range(len(matrix) - 1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix


def gaussPivotFunc(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow]  # диагональный элемент
        if abs(divider) < 1e-10:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            raise ValueError(f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}")
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]  # элемент строки в колонке nrow
            lower_row -= factor * row  # вычитаем, чтобы получить ноль в колонке nrow
    # приводим к диагональному виду
    make_identity(matrix)
    return matrix


def getL():
    L = np.eye(3)
    L[0, 0] = math.sqrt(var.A[0, 0])
    L[1, 0] = var.A[1, 0] / L[0, 0]
    L[2, 0] = var.A[2, 0] / L[0, 0]
    L[1, 1] = math.sqrt(var.A[1, 1] - math.pow(L[1, 0], 2))
    L[2, 1] = (var.A[2, 1] - L[2, 0] * L[1, 0]) / (L[1, 1])
    L[2, 2] = math.sqrt(var.A[2, 2] - math.pow(L[2, 0], 2) - math.pow(L[2, 1], 2))
    return L


def part1():
    print("--------1)Проверить матрицу на а) определенно положительная; б) симметричная.--------")
    minor = [var.A[:2, :2], var.A[:2, 1:], var.A[1:, :2], var.A[1:, 1:]]
    print("A = \n", var.A)
    for i in list(range(4)):
        print(f"\nminor{i + 1}\n{minor[i]}\ndet = {np.linalg.det(minor[i])}".format(i))

    # print(f"\n---------\n{var.A}\n---------\n{np.transpose(var.A)}\n---------\n")
    print(f"\n---\nA\n{var.A}\n---\nA.transpose\n{var.A.transpose()}\n---\n")
    print(f"det A = {np.linalg.det(var.A)}")


def part2():
    print("\n--------А = L * LT--------")
    L = getL()
    LT = np.transpose(L)
    print(f"L = \n{L}\n\nLT = \n{LT}\n")
    LLT = np.dot(L, LT)
    print(f"LLT = \n{LLT}")
    print(True) if np.allclose(var.A, LLT) else print(False)


def part3():
    print("\n--------Найти х обратным ходом метода Гаусса.--------")
    L = getL()
    LT = np.transpose(L)
    y = gaussPivotFunc(np.column_stack([L, var.f]))[:, -1]
    x = np.dot(y, np.linalg.inv(L))
    print(f"y = {y}\n")
    print(f"x = {x}")


def part4():
    print("\n--------Найти ||r||inf,1,2.--------")
    L = getL()
    LT = np.transpose(L)
    y = gaussPivotFunc(np.column_stack([L, var.f]))[:, -1]
    x = np.dot(y, np.linalg.inv(L))
    r = np.dot(var.A, x) - var.f
    print(r)


def main():
    part2()
    part3()
    part4()


if __name__ == "__main__":
    main()
