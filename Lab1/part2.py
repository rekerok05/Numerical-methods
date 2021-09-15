import math

import numpy as np

import Variables as var
import part1


def main():
    # Вектор невязки
    R = np.dot(var.A, part1.main()) - var.f
    print("\n\nPART 2\n")
    print("The residual vector\n", R, "\n\n")

    print("Октаэдрическая норма = ", np.sum(abs(R)))
    print("Сферическая норма = ", np.sqrt(np.sum(np.square(abs(R)))))
    print("Кубическая норма = ", np.max(abs(R)))


if __name__ == "__main__":
    main()
