import os

import numpy as np

znakPosleZap = 4


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


def maxLineSumInMatrix(matrix):
    print(matrix)
    sum = 0
    for line in matrix:
        tmpSum = np.sum(abs(line))
        if tmpSum > sum:
            sum = tmpSum
    return sum


def methodGauss(matrix):
    localMatrix = matrix
    localMatrix = np.flip(localMatrix, 0)
    for i, row in enumerate(localMatrix):
        for j, column in enumerate(row):
            if j < 4 and row[j] != 1:
                row[len(row) - 2] = row[len(row) - 2] - column * localMatrix[len(localMatrix) - 1 - j][
                    len(row) - 2]
                row[j] = 0
        row[-1] = np.sum(row[:-1])
    return np.flip(localMatrix, 0)


def deleteXlsx(format):
    for file in os.listdir():
        if ".{0}".format(format) in file:
            os.remove(file)


def addSumToList(matrix):
    matrix_sum = np.array([])
    for row in matrix:
        matrix_sum = np.append(matrix_sum, [np.sum(row)])
    return np.column_stack([matrix, matrix_sum])


def divideFirsElement(matrix):
    for row in matrix:
        row /= row[0]
    return np.around(matrix, decimals=znakPosleZap)
