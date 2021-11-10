import numpy as np
import numpy.linalg
from Lab1 import fuctions

import Variables as var


def part1():
    minor = [var.A[:2, :2], var.A[:2, 1:], var.A[1:, :2], var.A[1:, 1:]]
    print("A = \n", var.A)
    for i in list(range(4)):
        print(f"\nminor{i + 1}\n{minor[i]}\ndet = {np.linalg.det(minor[i])}".format(i))

    # print(f"\n---------\n{var.A}\n---------\n{np.transpose(var.A)}\n---------\n")
    print(f"\n---\nA\n{var.A}\n---\nA.transpose\n{var.A.transpose()}\n---\n")
    print(f"det A = {np.linalg.det(var.A)}")

def part2():
    matrix = var.A
    for i in list(range(3)):
        matrix[i:, i:] = fuctions.divideFirsElement(matrix[i:, i:])
        for row in matrix[i + 1:, :]:
            row -= matrix[i]
    print(matrix)


def main():
    part2()


if __name__ == "__main__":
    main()
