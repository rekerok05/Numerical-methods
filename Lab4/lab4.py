import numpy as np

import Variables as var


def output_matrix(name, value):
    print(f"\n{name} = \n{value}\n")


def iteration_method(B, g, x=None):
    newX = np.dot(B, x) + g
    print(f"\nOLD X: x1={x[0]}\tx2={x[1]}\tx3={x[2]}")
    print(f"NEW X: x1={newX[0]}\tx2={newX[1]}\tx3={newX[2]}")
    coub_norm_B = np.linalg.norm(B, np.inf)
    eps = ((1 - coub_norm_B) / coub_norm_B) * var.eps
    cub_norm = np.linalg.norm(newX - x, np.inf)
    print(f"norm (x(n+1) - x(n)) = {np.linalg.norm(newX - x, np.inf)}")
    print(f"eps = {eps}")
    if cub_norm > eps:
        return iteration_method(B, g, newX)
    return newX


def make_matrixB(A, C):
    return np.eye(3) - np.dot(C, A)


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

    cub_norm = np.max(list(map(lambda x: np.sum(np.abs(x)), B)))
    print(f"cub_norm = {cub_norm}")
    g = np.dot(C, expandedMatrix[:, -1])
    output_matrix("g", g)
    x = iteration_method(B, g, g)
    vector = np.dot(var.A, x) - var.f
    print(f"\nвектора невязки = {vector}")
    print(f"кубическая норма вектора невязки = {np.max(np.abs(vector))}")


if __name__ == "__main__":
    main()
