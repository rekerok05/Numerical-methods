import functools

import numpy as np

import Variables as var
from Lab4.lab4 import output_matrix


def get_max_element(matrix):
    i, j, max_element = 0, 0, None
    for row in range(len(matrix)):
        for colm in list(range(len(matrix))):
            if row < colm and row != colm:
                if max_element is None:
                    max_element = np.abs(matrix[row, colm])
                    i, j = row, colm
                else:
                    if max_element < np.abs(matrix[row, colm]):
                        max_element = np.abs(matrix[row, colm])
                        i, j = row, colm
    return max_element, i, j


def rotation_method(matrix, T_ij_list: list):
    max_element, i, j = get_max_element(matrix)  # максимальный элемент и его индексы выше главной диагонали
    print(f"|max element| = {max_element}, i = {i + 1}, j = {j + 1}\n")
    if matrix[i, i] != matrix[j, j]:
        fi = np.arctan((2 * matrix[i, j]) / (matrix[i, i] - matrix[j, j])) / 2
    else:
        if matrix[i, j] >= 0:
            fi = np.pi / 4
        else:
            fi = -np.pi / 4
    T_ij = getT(i, j, fi)
    T_ij_list.append(T_ij)
    new_matrix = np.dot(np.dot(np.transpose(T_ij), matrix), T_ij)
    return new_matrix


def getT(i, j, fi):
    T_ij = np.eye(3)
    T_ij[i, i] = np.cos(fi)
    T_ij[i, j] = -np.sin(fi)
    T_ij[j, i] = np.sin(fi)
    T_ij[j, j] = np.cos(fi)
    output_matrix("T_ij", T_ij)
    return T_ij


def main():
    T_ij_list = []
    output_matrix("A", var.A)

    # matrix = rotation_method(var.A, T_ij_list)
    matrix = var.A
    max_el = get_max_element(var.A)[0]

    step = 1
    while max_el > var.eps:
        print(f"STEP = {step}")
        matrix = rotation_method(matrix, T_ij_list)
        output_matrix("new matrix", matrix)
        max_el = get_max_element(matrix)[0]
        step += 1
    T = functools.reduce(lambda x, y: np.dot(x, y), T_ij_list)
    output_matrix("T = ", T)
    D = np.dot(np.dot(np.transpose(T), var.A), T)
    output_matrix("D = ", D)
    print(f"D diagonal = {np.diagonal(D)}")
    print(f"sum diag D = {np.sum(np.diagonal(D))}")
    print(f"sum diag A = {np.sum(np.diagonal(var.A))}")
    y_1, y_2, y_3 = T[:, 0], T[:, 1], T[:, 2]

    print(f"\ny_1 = {y_1}")
    print(f"y_2 = {y_2}")
    print(f"y_3 = {y_3}")

    x_1, x_2, x_3 = y_1 / np.linalg.norm(y_1, np.inf), y_2 / np.linalg.norm(y_2, np.inf), y_3 / np.linalg.norm(y_3,
                                                                                                               np.inf)
    print(f"\nx_1 = {x_1}")
    print(f"x_2 = {x_2}")
    print(f"x_3 = {x_3}")

    print("\nA * x_1 = λ_1 * x_1")
    print(f"{np.dot(var.A, x_1)} = {np.dot(D[0, 0], x_1)}")

    print("\nA * x_2 = λ_2 * x_2")
    print(f"{np.dot(var.A, x_2)} = {np.dot(D[1, 1], x_2)}")

    print("\nA * x_3 = λ_3 * x_3")
    print(f"{np.dot(var.A, x_3)} = {np.dot(D[2, 2], x_3)}")


if __name__ == "__main__":
    main()
