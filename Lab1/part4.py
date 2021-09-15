import numpy as np
import Variables as var


def maxLineSumInMatrix(matrix):
    print(matrix)
    sum = 0
    for line in matrix:
        tmpSum = np.sum(abs(line))
        if tmpSum > sum:
            sum = tmpSum
    return sum


def main():
    print(var.A)
    print("Норма по строкам = ", maxLineSumInMatrix(var.A))
    print("Норма по столбцам = ", maxLineSumInMatrix(var.A.transpose()))


if __name__ == "__main__":
    main()
