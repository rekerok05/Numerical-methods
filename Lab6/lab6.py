import numpy as np

import Variables as var
from Lab4.lab4 import output_matrix


def main():
    output_matrix("A", var.A)
    M1, M2, M3 = np.eye(4), np.eye(4), np.eye(4)

    M3[2] = [-var.A[3, 0] / var.A[3, 2], - var.A[3, 1] / var.A[3, 2], 1 / var.A[3, 2], -var.A[3, 3] / var.A[3, 2]]
    M3inv = np.linalg.inv(M3)
    output_matrix("M3", M3)
    output_matrix("M3inv", M3inv)

    A_1 = np.dot(np.dot(M3inv, var.A), M3)
    output_matrix("A_1", A_1)

    M2[1] = [-A_1[2, 0] / A_1[2, 1], 1 / A_1[2, 1], -A_1[2, 2] / A_1[2, 1], -A_1[2, 3] / A_1[2, 1]]
    M2inv = np.linalg.inv(M2)
    output_matrix("M2", M2)
    output_matrix("M2inv", M2inv)

    A_2 = np.dot(np.dot(M2inv, A_1), M2)
    output_matrix("A_2", A_2)

    M1[0] = [1 / A_2[1, 0], -A_2[1, 1] / A_2[1, 0], -A_2[1, 2] / A_2[1, 0], -A_2[1, 3] / A_2[1, 0]]
    M1inv = np.linalg.inv(M1)
    output_matrix("M1", M1)
    output_matrix("M1inv", M1inv)

    F = np.dot(np.dot(M1inv, A_2), M1)
    output_matrix("A_3 or F", F)

    print(f"p1 = {F[0, 0]}")
    print(f"sum of diagonal elements of A = {np.sum(np.diagonal(var.A))}\n")

    print(f"Charactestic equation :\n(-1)^4(λ^4 - {F[0, 0]}λ^3 - {F[0, 1]}λ^2 - {F[0, 2]}λ - {F[0, 3]}) = 0")

    lambdas = np.roots([1, -F[0, 0], -F[0, 1], -F[0, 2], -F[0, 3]])

    print(f"\nlambdas = {lambdas}")

    y_1 = [pow(np.real(lambdas[0]), 3), pow(np.real(lambdas[0]), 2), np.real(lambdas[0]), 1]
    print(f"\ny_1 = {y_1}")

    y_2 = [pow(np.real(lambdas[1]), 3), pow(np.real(lambdas[1]), 2), np.real(lambdas[1]), 1]
    print(f"\ny_2 = {y_2}")

    x_1 = np.dot(M3, np.dot(M2, np.dot(M1, y_1)))
    print(f"\n\n{np.dot(M1, y_1)}")
    print(f"\n{np.dot(M2, np.dot(M1, y_1))}")
    print(f"\nx_1 ={x_1}")

    x_2 = np.dot(M3, np.dot(M2, np.dot(M1, y_2)))
    print(f"\n\n{np.dot(M1, y_2)}")
    print(f"\n{np.dot(M2, np.dot(M1, y_2))}")
    print(f"\nx_2 ={x_2}")

    Sinv = np.dot(M1inv, np.dot(M2inv, M3inv))
    S = np.dot(M3, np.dot(M2, M1))

    print("\nS^-1 * A * S * y_1 = λ_1 * y_1")
    print(f"{np.dot(np.dot(Sinv, np.dot(var.A, S)), y_1)} = {np.dot(np.real(lambdas[0]), y_1)}")

    print("\nS^-1 * A * S * y_2 = λ_2 * y_2")
    print(f"{np.dot(np.dot(Sinv, np.dot(var.A, S)), y_2)} = {np.dot(np.real(lambdas[1]), y_2)}")

    print("\nA * x_1 = λ_1 * x_1")
    print(f"{np.dot(var.A, x_1)} = {np.dot(np.real(lambdas[0]), x_1)}")

    print("\nA * x_2 = λ_2 * x_2")
    print(f"{np.dot(var.A, x_2)} = {np.dot(np.real(lambdas[1]), x_2)}")


if __name__ == "__main__":
    main()
