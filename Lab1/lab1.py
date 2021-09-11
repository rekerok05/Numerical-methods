import numpy as np


def main():
    D = np.array(
        [[6.22, 1.42, -1.72, 1.91], [1.44, 5.33, 1.11, -1.82], [-1.72, 1.11, 5.24, 1.42], [1.91, -1.82, 1.42, 6.55]],
        float)
    C = np.identity(4, dtype=float)
    f = np.array([[7.53], [6.06], [8.05], [8.06]])
    K = 1

    A = np.array(D + C.dot(K))

    print("Matrix A\n", A, "\n")

    matrix_with_free_elements = np.column_stack([A, f])

    print("Matrix A with free elements\n", matrix_with_free_elements, "\n")

    matrix_sum = np.array([])

    for stroka in matrix_with_free_elements:
        matrix_sum = np.append(matrix_sum, [np.sum(stroka)])

    matrix_with_sum_elements = np.column_stack([matrix_with_free_elements, matrix_sum])

    print("\n\n\n", matrix_with_sum_elements)

    def func(matrix):
        for stroka in matrix:
            stroka /= stroka[0]
        for stroka in matrix[1:]:
            stroka -= matrix[0]

    func(matrix_with_sum_elements)
    print("\n\n\n", matrix_with_sum_elements)
    func(matrix_with_sum_elements[1:, 1:])
    print("\n\n\n", matrix_with_sum_elements)
    func(matrix_with_sum_elements[2:, 2:])
    print("\n\n\n", matrix_with_sum_elements)
    func(matrix_with_sum_elements[3:, 3:])
    print("\n\n\n", matrix_with_sum_elements)


main()
