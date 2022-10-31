from Lab4.lab4 import output_matrix, make_matrixB
import numpy as np
import Variables as var


def iteration_method(B, g, x=None):
    # newX = np.dot(B, x) + g
    newX = np.zeros(3)
    # print(newX)
    newX[0] = B[0, 0] * x[0] + B[0, 1] * x[1] + B[0, 2] * x[2] + g[0]
    newX[1] = B[1, 0] * newX[0] + B[1, 1] * x[1] + B[1, 2] * x[2] + g[1]
    newX[2] = B[2, 0] * newX[0] + B[2, 1] * newX[1] + B[2, 2] * x[2] + g[2]

    print(f"\nOLD X: x1={x[0]}\tx2={x[1]}\tx3={x[2]}")
    print(f"NEW X: x1={newX[0]}\tx2={newX[1]}\tx3={newX[2]}")
    cub_norm_B = np.linalg.norm(B, np.inf)
    eps = ((1 - cub_norm_B) / cub_norm_B) * var.eps
    cub_norm = np.linalg.norm(newX - x, np.inf)
    print(f"norm (x(n+1) - x(n)) = {np.linalg.norm(newX - x, np.inf)}")
    print(f"eps = {eps}")
    if cub_norm > eps:
        return iteration_method(B, g, newX)
    return newX


def norm_matrix_B(A):
    cub_norm = np.max(list(map(lambda x: np.sum(np.abs(x)), A)))
    oct_norm = np.max(list(map(lambda x: np.sum(np.abs(x)), A.transpose())))
    print(
        f"Кубическая норма матрицы B = {cub_norm}")  # Максимальная среди сумм строк
    print(
        f"Октаэдрическая норма матрицы B = {oct_norm}\n")  # Максимальная среди сумм столбцов
    cub_norm = np.linalg.norm(A, np.inf)
    oct = np.linalg.norm(A, 1)
    print(cub_norm)
    print(oct)
    return cub_norm, oct_norm


def main():
    output_matrix("A", var.A)
    output_matrix("f", var.f)

    expandedMatrix = np.insert(arr=var.A, obj=3, values=var.f, axis=1)
    output_matrix("expandedMatrix (without transformations)", expandedMatrix)
    expandedMatrix[2] = 2 * expandedMatrix[2] + expandedMatrix[0] - expandedMatrix[1]
    output_matrix("expandedMatrix (with transformations", expandedMatrix)

    D = np.zeros((3, 3))
    np.fill_diagonal(D, expandedMatrix.diagonal())
    output_matrix("D", D)
    C = np.linalg.inv(D)
    output_matrix("C", C)
    B = make_matrixB(expandedMatrix[:, :-1], C)
    output_matrix("B", B)
    norm_matrix_B(B)
    g = np.dot(C, expandedMatrix[:, -1])
    output_matrix("g", g)

    x = iteration_method(B, g, g)
    # vector = np.dot(var.A, x) - var.f
    # print(f"\nвектора невязки = {vector}")
    # print(f"кубическая норма вектора невязки = {np.max(np.abs(vector))}")


if __name__ == "__main__":
    main()
