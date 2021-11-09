import numpy as np
from Lab1 import fuctions, Variables as var


def part1():
    inverseMatrix = np.array([])
    eyeMatrix = np.eye(4)
    for i in list(range(4)):
        inverseMatrix = np.append(inverseMatrix,
                                  np.array(fuctions.makeExcelTable(f"lab2Table{i + 1}", var.A, np.array(eyeMatrix[i]))))
    inverseMatrix = inverseMatrix.reshape(4, 4)
    return inverseMatrix



def part2():
    print("inverse matrix\n", part1())
    print("identityMatrix\n", var.A.dot(part1()))

    print("Октаэдрическая норма = ", np.sum(abs(part1())))
    print("Сферическая норма = ", np.sqrt(np.sum(np.square(abs(part1())))))
    print("Кубическая норма = ", np.max(abs(part1())))

    print("Октаэдрическая норма исходной = ", 12.7)
    print("Кубическая норма исходной = ", 0.4782)

    print("Октаэдрическая норма обратной = ", 12.700)
    print("Кубическая норма обратной = ", 0.4794)

    print("Число обусловленностей (октаэдрическая) = ", 12.7 * 0.4794)
    print("Число обусловленностей (кубическая) = ", 12.700 * 0.4794)


def main():
    part2()


if __name__ == "__main__":
    main()
