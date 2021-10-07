import os
import numpy as np
import Variables as var
from openpyxl import Workbook, load_workbook


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
    return matrix


def main():
    deleteXlsx("xlsx")
    matrix = addSumToList(np.column_stack([var.A, var.f]))
    print(matrix)
    wb = Workbook()
    ws = wb.active
    ws.title = "matrix"
    ws.append(["i", "ai1", "ai2", "ai3", "ai4", "ai5", "sum(i,6)", "sum(i)"])

    ws.append([checkio(1)])
    for i, row in enumerate(matrix, 1):
        ws.append(list([i, *row]))
    matrix = divideFirsElement(matrix)
    ws.append(list(["", *matrix[0], np.sum(matrix[0, :5])]))
    for row in matrix[1:, :]:
        row -= matrix[0]

    ws.append([checkio(2)])
    for i, row in enumerate(matrix[1:, 1:], 2):
        ws.append(list([i, " ", *row, np.sum(row[:-1])]))
    matrix[1:, 1:] = divideFirsElement(matrix[1:, 1:])
    ws.append(list(["", "", *matrix[1, 1:], np.sum(matrix[1, :5])]))
    for row in matrix[2:, :]:
        row -= matrix[1]

    ws.append([checkio(3)])
    for i, row in enumerate(matrix[2:, 2:], 3):
        ws.append(list([i, " ", "", *row, np.sum(row[:-1])]))
    matrix[2:, 2:] = divideFirsElement(matrix[2:, 2:])
    ws.append(list(["", "", "", *matrix[2, 2:], np.sum(matrix[2, :5])]))
    for row in matrix[3:, :]:
        row -= matrix[2]

    ws.append([checkio(4)])
    for i, row in enumerate(matrix[3:, 3:], 4):
        ws.append(list([i, " ", "", "", *row, np.sum(row[:-1])]))
    matrix[3:, 3:] = divideFirsElement(matrix[3:, 3:])
    ws.append(list(["", "", "", "", *matrix[3, 3:], np.sum(matrix[3, :5])]))
    for row in matrix[4:, :]:
        row -= matrix[3]

    ws.append([checkio(5)])
    matrix = methodGauss(matrix)
    for row in matrix:
        ws.append(list(["", *row, np.sum(row[-1])]))

    wb.save("matrix.xlsx")


if __name__ == "__main__":
    main()
