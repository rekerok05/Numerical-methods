import numpy as np
import Variables as var


def func(matrix):
    M = np.eye(4)
    revM = np.eye(4)
    unitE = np.eye(4)
    print(M)
    tempA = matrix
    for i in range(2, -1, -1):
        for j in range(0, 4):
            if j == i:
                M[i, j] = 1 / tempA[i + 1, i]
            else:
                M[i, j] = -tempA[i + 1, j] / tempA[i + 1, i]
            revM[i, j] = tempA[i + 1, j]
        print(f"revM = \n{revM}\n")
        tempA = np.dot(np.dot(revM, tempA), M)
        revM = unitE
        M = unitE

        # while i >= 0:
    #     j = 0
    #     while j <= 3:
    #         if i == j:
    #             M[i, j] = 1 / tempA[i + 1, i]
    #         else:
    #             M[i, j] = -tempA[i + 1, j] / tempA[i + 1, i]
    #         revM[i, j] = tempA[i + 1, j]
    #         j += 1
    #     tmp = np.dot(revM, tempA)
    #     tempA = np.dot(tmp, M)


def printValue(name, value):
    print(f"{name} = \n{value}")


def part1():
    print("part")
    # a0
    a0 = var.A
    # m3
    m3 = np.eye(4)
    m3[2, :2] = -a0[3, :2] / a0[3, 2]
    m3[2, 2] /= a0[3, 2]
    m3[2, -1] = -a0[-1, -1] / a0[3, 2]
    # m3^-1
    m3minus1 = np.eye(4)


def main():
    part1()


if __name__ == "__main__":
    main()
