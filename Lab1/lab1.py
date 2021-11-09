import VariablesLab1 as var
from Lab1 import getAnswer
from fuctions import *


def part2():
    # Вектор невязки
    R = np.dot(var.A, getAnswer.main()) - var.f
    print("\n\nPART 2\n")
    print("Вектор невязки\n", R, "\n\n")

    print("Октаэдрическая норма = ", np.sum(abs(R)))
    print("Кубическая норма = ", np.max(abs(R)))
    print("Сферическая норма = ", np.sqrt(np.sum(np.square(abs(R)))))



def part1():
    makeExcelTable("lab1", var.A, var.f)


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
    main()
