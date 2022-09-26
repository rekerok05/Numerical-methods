import numpy as np

from Lab1 import Variables as Var
from Lab1 import lab1


def inverse_matrix_method_gauss(matrix: np.ndarray) -> np.ndarray:
    size_matrix = len(matrix)
    inverse_matrix = np.array([])
    for i in np.identity(4, dtype=int):
        triangleMatrix, solution = lab1.method_Gauss(matrix, i)
        inverse_matrix = np.append(inverse_matrix, solution)
    return np.matrix(inverse_matrix).reshape((size_matrix, size_matrix)).T


def main():
    inverse_matrix = inverse_matrix_method_gauss(Var.A)
    cub_norm_A, oct_norm_A = lab1.norm_matrix(Var.A)
    print(f"\nОбратная матрица Методом Гаусса:\n{inverse_matrix}\n")
    print(f"\nОбратная матрица Встроенной функцией:\n{np.linalg.inv(Var.A)}\n")
    cub_norm_inverse_matrix, oct_norm_inverse_matrix = lab1.norm_matrix(inverse_matrix)
    print(f"\nПроверка A * A^(-1) = E\n{Var.A.dot(np.linalg.inv(Var.A))}n")
    print(f"\nЧисло обусловленности (кубическое): {cub_norm_A * cub_norm_inverse_matrix}")
    print(f"\nЧисло обусловленности (октаэдрическое): {oct_norm_A * oct_norm_inverse_matrix}\n")


if __name__ == "__main__":
    main()
