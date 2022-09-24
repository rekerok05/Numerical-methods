import numpy as np

import Variables as Var

def print_variables(matrix):
    detA = np.linalg.det(matrix)
    print(f"Матрица вырожденная detA = {detA}" if detA > 0 else f"Матрица невырожденная detA = {detA}")
    print(f"Исходная матрица\n{matrix}\n")


def add_sum_colm(matrix) -> np.ndarray:
    return np.insert(arr=matrix,
                     obj=matrix.shape[1],
                     values=np.array(list(map(lambda x: np.sum(x), matrix))),
                     axis=1)


def make_triangle_matrix(matrix):
    matrix[0] /= matrix[0, 0]
    for i in matrix[1:]:
        i -= matrix[0] * i[0]
    print(matrix)
    print(f"{np.sum(matrix[0, 0:-1])}\n")
    if np.shape(matrix)[0] > 1:
        matrix[1:, 1:] = make_triangle_matrix(matrix[1:, 1:])
    return matrix


def find_solution(matrix):
    solution = np.array([0] * len(matrix), float)
    solution[-1] = matrix[-1, -1]
    for i in range(len(matrix) - 2, -1, -1):
        tmp = 0
        for j in range(len(matrix[i, :-1])):
            tmp += matrix[i, j] * solution[j]
        solution[i] = matrix[i, -1] - tmp
    return solution


def method_Gauss(matrix, f) -> tuple:
    expandedMatrix = np.insert(arr=matrix, obj=4, values=f, axis=1)
    expandedMatrix = add_sum_colm(expandedMatrix)
    print(f"Расширенная матрица \n{expandedMatrix}\n")
    print(triangleMatrix := make_triangle_matrix(expandedMatrix))
    solution = find_solution(np.delete(triangleMatrix, -1, 1))
    solution2 = find_solution(np.delete(triangleMatrix, -2, 1))
    print(f"\nВектор ответов (столбец обратной матрицы) = {solution}\n")
    print(f"Вектор ответов (контроль) = {solution2}\n")
    return (triangleMatrix, solution)


def norm_matrix(A):
    cub_norm = np.max(list(map(lambda x: np.sum(np.abs(x)), A)))
    oct_norm = np.max(list(map(lambda x: np.sum(np.abs(x)), A.transpose())))
    print(
        f"Кубическая норма матрицы = {cub_norm}")  # Максимальная среди сумм строк
    print(
        f"Октаэдрическая норма матрицы = {oct_norm}\n")  # Максимальная среди сумм столбцов
    return cub_norm, oct_norm


def make_matrix(first_col, second_col, third_col, fourth_col):
    matr = np.array(
        [first_col,
         second_col,
         third_col,
         fourth_col])
    return matr


def main():
    print_variables(Var.A)

    print("\nТаблица для первого стобца единичной матрицы:\n")
    triangleMatrix, first_solution = method_Gauss(Var.A, Var.first_column)

    print("\nТаблица для второго стобца единичной матрицы:\n")
    triangleMatrix, second_solution = method_Gauss(Var.A, Var.second_column)

    print("\nТаблица для третьего стобца единичной матрицы:\n")
    triangleMatrix, third_solution = method_Gauss(Var.A, Var.third_column)

    print("\nТаблица для четвертого стобца единичной матрицы:\n")
    triangleMatrix, fourth_solution = method_Gauss(Var.A, Var.fourth_column)

    cub_norm_A, oct_norm_A = norm_matrix(Var.A)

    inverse_matrix = np.transpose(make_matrix(first_solution, second_solution, third_solution, fourth_solution))
    print(f"\nОбратная матрица:\n{inverse_matrix}\n")

    cub_norm_inverse_matrix, oct_norm_inverse_matrix = norm_matrix(inverse_matrix)

    print(f"\nПроверка A * A^(-1) = E\n{Var.A.dot(inverse_matrix)}\n")

    print(f"\nЧисло обусловленности (кубическое): {cub_norm_A * cub_norm_inverse_matrix}")
    print(f"\nЧисло обусловленности (октаэдрическое): {oct_norm_A * oct_norm_inverse_matrix}\n")


if __name__ == "__main__":
    main()
