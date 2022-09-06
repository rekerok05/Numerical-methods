import numpy
import numpy as np

import Variables


# Функция вывода всех матриц
def print_variables(matrix, f):
    detA = np.linalg.det(matrix)
    print(f"Матрица вырожденная detA = {detA}" if detA > 0 else f"Матрица невырожденная detA = {detA}")
    print(f"Исходная матрица\n{matrix}\n")
    print(f"Единичная матрица\n{np.identity(len(matrix))}\n")
    print(f"Столбец ответов\n{f}\n")


def add_sum_colm(matrix) -> np.ndarray:
    return np.insert(arr=matrix,
                     obj=matrix.shape[1],
                     values=np.array(list(map(lambda x: np.sum(x), matrix))),
                     axis=1)


def make_triangle_matrix(matrix):
    row, colm = np.shape(matrix)
    if row > 1:
        for i in range(1, row):
            for j in range(1, colm):
                matrix[i, j] = matrix[i, j] - matrix[i, 0] * matrix[0, j]
        matrix[1] = matrix[1] / matrix[1, 1]
        if row != 2:
            little_matrix = make_triangle_matrix(matrix[1:, 1:])
            matrix = little_matrix
        return matrix


def method_Gauss(matrix, f):
    expandedMatrix = np.insert(arr=matrix, obj=4, values=f, axis=1)
    expandedMatrix = add_sum_colm(expandedMatrix)

    print(f"Этап 1")
    expandedMatrix[0] = expandedMatrix[0] / expandedMatrix[0, 0]
    print(expandedMatrix)
    print(expandedMatrix[0])
    print(f"sum' = {np.sum(expandedMatrix[0, 1:-1])}")

    expandedMatrix = make_triangle_matrix(expandedMatrix)

    print(expandedMatrix)
    # print(f"Этап 2")
    # for i in range(1, 3):
    #     for j in range(1, 5):
    #         expandedMatrix[i, j] = expandedMatrix[i, j] - expandedMatrix[i, 0] * expandedMatrix[0, j]
    # expandedMatrix[1] = expandedMatrix[1] / expandedMatrix[1, 1]
    # print(expandedMatrix)
    # print(f"sum' = {np.sum(expandedMatrix[1, 1:-1])}")
    #
    # print(f"Этап 3")
    # for i in range(2, 3):
    #     for j in range(2, 5):
    #         expandedMatrix[i, j] = expandedMatrix[i, j] - expandedMatrix[i, 1] * expandedMatrix[1, j]
    # expandedMatrix[2] = expandedMatrix[2] / expandedMatrix[2, 2]
    # print(expandedMatrix)
    # print(f"sum' = {np.sum(expandedMatrix[2, 1:-1])}")
    #
    # print(f"Этап 4")
    # for i in range(2, 3):
    #     for j in range(2, 5):
    #         expandedMatrix[i, j] = expandedMatrix[i, j] - expandedMatrix[i, 1] * expandedMatrix[1, j]
    # expandedMatrix[2] = expandedMatrix[2] / expandedMatrix[2, 2]
    # print(expandedMatrix)
    # print(f"sum' = {np.sum(expandedMatrix[3, 1:-1])}")


def main():
    print_variables(Variables.A, Variables.f)
    # print(np.linalg.solve(Variables.A, Variables.f))
    method_Gauss(Variables.A, Variables.f)


if __name__ == "__main__":
    main()
