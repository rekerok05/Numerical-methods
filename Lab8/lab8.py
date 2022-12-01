import numpy as np
import Lab8.Variables as var
from Lab4.lab4 import output_matrix


def main():
    output_matrix("A", var.A)
    y_0 = np.ones(3)
    z = y_0 / np.linalg.norm(y_0, np.inf)
    print(f"z = {z}")
    y = np.dot(var.A, z)
    print(f"y = {y}")
    step = 1
    while np.abs((y[0] / z[0]) - (y[1] / z[1])) > var.eps and \
            np.abs((y[2] / z[2]) - (y[1] / z[1])) > var.eps and \
            np.abs((y[0] / z[0]) - (y[2] / z[2])) > var.eps:
        print(f"\nSTEP {step}")
        print(f"[y[0] / z[0], y[1] / z[1], y[2] / z[2]] = {[y[0] / z[0], y[1] / z[1], y[2] / z[2]]}")
        z_new = y / np.linalg.norm(y, np.inf)
        y_new = np.dot(var.A, z_new)
        y = y_new
        z = z_new
        print(f"y = {y}")
        print(f"z = {z}")
        step += 1
    print(f"\nmax lambda = {y[0] / z[0]}")
    print(f"vector = {z}")


if __name__ == "__main__":
    main()