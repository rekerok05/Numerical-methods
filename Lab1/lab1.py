import Variables as var
from Lab1 import getAnswer
from fuctions import *


def makeExcelTable(name, A, f):
    matrix = addSumToList(np.column_stack([A, f]))
    deleteXlsx("xlsx")
    wb = Workbook()
    ws = wb.active
    ws.title = name
    ws.append(["i", "ai1", "ai2", "ai3", "ai4", "ai5", "sum(i,6)", "sum(i)"])

    # ws.append([checkio(1)])
    # for i, row in enumerate(matrix, 1):
    #     ws.append(list([i, *row]))
    # matrix = divideFirsElement(matrix)
    # ws.append(list(["", *matrix[0], np.sum(matrix[0, :5])]))
    # for row in matrix[1:, :]:
    #     row -= matrix[0]
    #
    # ws.append([checkio(2)])
    # for i, row in enumerate(matrix[1:, 1:], 2):
    #     ws.append(list([i, "", *row, np.sum(row[:-1])]))
    # matrix[1:, 1:] = divideFirsElement(matrix[1:, 1:])
    # ws.append(list(["", "", *matrix[1, 1:], np.sum(matrix[1, :5])]))
    # for row in matrix[2:, :]:
    #     row -= matrix[1]
    #
    # ws.append([checkio(3)])
    # for i, row in enumerate(matrix[2:, 2:], 3):
    #     ws.append(list([i, "", "", *row, np.sum(row[:-1])]))
    # matrix[2:, 2:] = divideFirsElement(matrix[2:, 2:])
    # ws.append(list(["", "", "", *matrix[2, 2:], np.sum(matrix[2, :5])]))
    # for row in matrix[3:, :]:
    #     row -= matrix[2]
    #
    # ws.append([checkio(4)])
    # for i, row in enumerate(matrix[3:, 3:], 4):
    #     ws.append(list([i, "", "", "", *row, np.sum(row[:-1])]))
    # matrix[3:, 3:] = divideFirsElement(matrix[3:, 3:])
    # ws.append(list(["", "", "", "", *matrix[3, 3:], np.sum(matrix[3, :5])]))
    # for row in matrix[4:, :]:
    #     row -= matrix[3]

    for i in list(range(4)):
        ws.append([checkio(i + 1)])
        for j, row in enumerate(matrix[i:, i:], (i + 1)):
            ws.append(list([j, *list([""] * i), *row, np.sum(row[:-1])]))
        matrix[i:, i:] = divideFirsElement(matrix[i:, i:])
        ws.append(list([*list([""] * (i + 1)), *matrix[i, i:], np.sum(matrix[i, :5])]))
        for row in matrix[i + 1:, :]:
            row -= matrix[i]

    ws.append([checkio(5)])
    matrix = np.around(methodGauss(matrix), decimals=znakPosleZap)
    for row in matrix:
        ws.append(list(["", *row, np.sum(row[-1])]))
    wb.save("Lab1" + ".xlsx")
    return matrix


def part2():
    # Вектор невязки
    R = np.dot(var.A, getAnswer.main()) - var.f
    print("\n\nPART 2\n")
    print("Вектор невязки\n", R, "\n\n")

    print("Октаэдрическая норма = ", np.sum(abs(R)))
    print("Кубическая норма = ", np.max(abs(R)))
    print("Сферическая норма = ", np.sqrt(np.sum(np.square(abs(R)))))


def part1():
    makeExcelTable("Lab1", var.A, var.f)


def part3():
    print("\n\nPART 2\n")
    print("Определитель матрицы = ", np.linalg.det(var.A))


def part4():
    print(var.A)
    print("Норма по строкам = ", maxLineSumInMatrix(var.A))
    print("Норма по столбцам = ", maxLineSumInMatrix(var.A.transpose()))


def main():
    part3()


if __name__ == "__main__":
    part1()
    main()
