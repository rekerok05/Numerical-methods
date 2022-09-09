import numpy as np

import Variables as Var


# Функция вывода всех матриц
def print_variables(matrix, f):
    detA = np.linalg.det(matrix)
    print(f"Матрица вырожденная detA = {detA}" if detA > 0 else f"Матрица невырожденная detA = {detA}")
    print(f"Исходная матрица\n{matrix}\n")
    print(f"Единичная матрица\n{np.identity(len(matrix))}\n")
    print(f"Столбец ответов\n{f}\n")


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
    print(f"{np.sum(matrix[0, 1:-1])}\n")
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
    print(f"\nВектор ответов = {solution}\n")
    print(f"\nВектор ответов2 = {solution2}\n")
    return (triangleMatrix, solution)


def discrepancy_vector(variables: tuple):  # (A, f, solution, triangleMatrix)
    R = np.dot(variables[0], variables[2]) - variables[1]
    print(f"Вектор невязки {R}\n")
    return R


def norm_discrepancy_vector(R):
    print(
        f"Кубическая норма вектора невязки = {np.max(np.abs(R))}")  # Максимальный по модулу элемент вектора невзяки (знак бесконечности)
    print(
        f"Октаэдрическая норма вектора невязки = {np.sum(np.abs(R))}")  # Сумма модулей элементов вектора невязки (знак "1")
    print(
        f"Сферическая норма вектора невязки = {np.sqrt(np.sum(np.square(np.abs(R))))}\n")  # Корень из суммы квадратов элементов вектора невязки (знак "1")


def norm_matrix(A):
    print(
        f"Кубическая норма матрицы A = {np.max(list(map(lambda x: np.sum(np.abs(x)), A)))}")  # Максимальная среди сумм строк
    print(
        f"Октаэдрическая норма матрицы A = {np.max(list(map(lambda x: np.sum(np.abs(x)), A.transpose())))}\n")  # Максимальная среди сумм столбцов


def detA(A):
    for i, value in enumerate(A[1:]):
        A[i + 1] = value - A[0] * (value[0] / A[0, 0])
    if len(A) > 2:
        A[1:, 1:] = detA(A[1:, 1:])
    return A


def main():
    print_variables(Var.A, Var.f)
    triangleMatrix, solution = method_Gauss(Var.A, Var.f)
    R = discrepancy_vector((Var.A, Var.f, solution, triangleMatrix))
    norm_discrepancy_vector(R)
    norm_matrix(Var.A)
    detMatrixA = detA(np.copy(Var.A))
    print(f"Определитель матрицы A = {np.product(np.diagonal(detMatrixA))}")


if __name__ == "__main__":
    main()
