import numpy as np
import Variables as var


def part1():
    M3 = np.eye(4)
    M3[3] = var.A[-1, :2] / var.A[-1, -2]
    print(M3)


def main():
    part1()


if __name__ == "__main__":
    main()
