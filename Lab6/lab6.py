import numpy as np

import Variables as var


def printValue(name, value):
    print(f"{name} = \n{value}\n")


def indexofabsmax(matrix):
    maxL = max(np.abs([matrix[0, 1], matrix[0, 2], matrix[1, 2]]))
    if maxL == 0.0:
        return [0, 0, 0]
    i, j = np.where(np.isclose(abs(matrix), maxL))[0]
    return [i, j, matrix[i, j]]


if __name__ == "__main__":
    tmpA = var.A
    change = True
    iteration = 0
    tmpT = 1
    print("ИТЕРАЦИИ\n")
    while np.abs(indexofabsmax(tmpA)[2]) > var.eps:
        print(f"Шаг {iteration}")
        iteration += 1
        i, j = indexofabsmax(tmpA)[0], indexofabsmax(tmpA)[1]
        print(i, j)
        fi = 0.5 * np.arctan(2 * tmpA[i, j] / (tmpA[i, i] - tmpA[j, j]))
        T = np.eye(3)
        T[i, i] = np.cos(fi)
        T[i, j] = -np.sin(fi)
        T[j, i] = np.sin(fi)
        T[j, j] = np.cos(fi)
        trT = np.transpose(T)
        printValue("A", tmpA)
        printValue("T", T)
        printValue("trT", trT)
        if change:
            tmpT = np.dot(tmpT, T)
        else:
            tmpT = T
            change = False
        printValue("T*trT", tmpT)
        tmpVar = np.dot(trT, tmpA)
        tmpA = np.around(np.dot(tmpVar, T), decimals=7)
        printValue("tmpA", tmpA)

    print("-------------------------------------")
    printValue("lastA", tmpA)
    printValue("lastT", T)
    print("-------------------------------------")
    lambda1 = tmpA[0, 0]
    lambda2 = tmpA[1, 1]
    lambda3 = tmpA[2, 2]
    print("НАХОДИМ СОБСТВЕННЫЕ ЗНАЧЕНИЯ МАТРИЦЫ A\n")
    printValue("lambda1", lambda1)
    printValue("lambda2", lambda2)
    printValue("lambda3", lambda3)
    print("-------------------------------------")
    y1 = tmpT[:, 0]
    y2 = tmpT[:, 1]
    y3 = tmpT[:, 2]
    print("НАХОДИМ СОБСТВЕННЫЕ ВЕКТОРЫ МАТРИЦЫ A\n")
    printValue("y1", y1)
    printValue("y2", y2)
    printValue("y3", y3)
    print("-------------------------------------")
    print("НОРМИРОВАНИЕ ВЕКТОРОВ В КУБИЧЕСКОЙ НОРМЕ\n")
    x1 = y1 / np.max(np.abs(tmpT[:, 0]))
    x2 = y2 / np.max(np.abs(tmpT[:, 1]))
    x3 = y3 / np.max(np.abs(tmpT[:, 2]))
    printValue("x1", x1)
    printValue("x2", x2)
    printValue("x3", x3)
    print("-------------------------------------")
    print("ПРОВЕРКА")
    print(f"A*x1 = {np.dot(var.A, x1)}")
    print(f"lambda1*x1 = {np.dot(lambda1, x1)}\n")
    print(f"A*x2 = {np.dot(var.A, x2)}")
    print(f"lambda2*x2 = {np.dot(lambda2, x2)}\n")
    print(f"A*x3 = {np.dot(var.A, x3)}")
    print(f"lambda3*x3 = {np.dot(lambda3, x3)}\n")
