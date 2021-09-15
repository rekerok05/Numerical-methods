import numpy as np
import Variables as var


# Функция вывода Римских чисел
def checkio(data):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]

    return t + h + te + o


# Функция для создания нулей плод главной диаглналью
def makeTrianglMatrix(matrix):
    for row in matrix:
        row /= row[0]
    for row in matrix[1:]:
        row -= matrix[0]

    if matrix.shape[0] > 1:
        makeTrianglMatrix(matrix[1:, 1:])
    return matrix


# Создание колонки суммы
def columnSum(matrix):
    matrix_sum = np.array([])
    for row in matrix:
        matrix_sum = np.append(matrix_sum, [np.sum(row)])
    return matrix_sum


def methodGauss(matrix):
    localMatrix = matrix
    localMatrix = np.flip(localMatrix, 0)
    for i, row in enumerate(localMatrix):
        for j, column in enumerate(row):
            if j < 4 and row[j] != 1:
                row[len(row) - 2] = np.around(row[len(row) - 2] - column * localMatrix[len(localMatrix) - 1 - j][
                    len(row) - 2], decimals=5)
                row[j] = 0
        row[-1] = np.sum(row[:-1])
        print("----------------\n%s\n" % (checkio(i + 1)), localMatrix, "\n----------------")

    return np.flip(localMatrix, 0)


def main():
    print("\n\nPART 1\n\n")

    print("Matrix A\n", var.A, "\n")

    matrix_with_free_elements = np.column_stack([var.A, var.f])

    print("Matrix A with free elements\n", matrix_with_free_elements, "\n")

    matrix_sum = np.array([])
    for row in matrix_with_free_elements:
        matrix_sum = np.append(matrix_sum, [np.sum(row)])
    matrix_with_sum_elements = np.column_stack([matrix_with_free_elements, matrix_sum])

    # Округление матрицы
    matrix_with_sum_elements = np.around(makeTrianglMatrix(matrix_with_sum_elements), decimals=5)

    print("Matrix A with sum elements\n", matrix_with_sum_elements, "\n\n\n")

    matrix_with_sum_elements = methodGauss(matrix_with_sum_elements)

    print("\nRESULT\n", matrix_with_sum_elements, "\n\n\n")
    print(matrix_with_sum_elements[:, -2])
    return np.matrix(matrix_with_sum_elements[:, -2]).T


if __name__ == "__main__":
    main()
