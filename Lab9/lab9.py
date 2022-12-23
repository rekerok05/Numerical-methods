import numpy as np
from matplotlib import pyplot as plt

import Variables as var


def fi(x):
    return (x ** 3 + np.sin(x) + 1) / 12


def fi2(x):
    c = -1


def f(x):
    return x ** 3 + np.sin(x) - 12 * x + 1


def tmp(x_0, x1, x2):
    print(f"\nx_0 = {x_0}")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    delta = np.abs(x1 - x_0)
    print(f"\ndelta = {delta}")

    print(f"\nПервое условие теоремы:")
    print(f"|fi(x1) - fi(x2)| = {np.abs(fi(x1) - fi(x2))}")
    print(f"|x1 - x2| = {np.abs(x1 - x2)}")
    q = np.abs(fi(x1) - fi(x2)) / np.abs(x1 - x2)
    print(f"q = {q}")

    print(f"\nВторое условие теоремы:")
    print(f"|x_0 - fi(x_0)| = {np.abs(x_0 - fi(x_0))}")
    m = np.abs(x_0 - fi(x_0))
    print(f"m = {m}")

    print(f"\nТретье условие теоремы:")
    print(f"m/(1-q) = {m / (1 - q)}")
    print(f"m/(1-q) <= delta\n{m / (1 - q)} <= {delta}")

    print(f"\nИтерации:")
    step = 0
    print(f"step = {step}\tx_0 = {x_0}")
    x_1 = fi(x_0)
    step += 1
    print(f"step = {step}\tx_1 = {x_1}")
    step += 1
    print(f"|x_n+1 - x_n| = {np.abs(x_1 - x_0)}")

    while np.abs(x_1 - x_0) >= var.eps:
        x_0 = x_1
        x_1 = fi(x_0)
        print(f"\nstep = {step}\tx_{step} = {x_1}")
        step += 1
        print(f"|x_n+1 - x_n| = {np.abs(x_1 - x_0)}")

    print("\nПроверка: ")
    print(f"|f(x_n) - eps| = {np.abs(f(x_1) - var.eps)}")


def draw_graphic():
    x = np.arange(-10, 10, 0.01)
    plt.plot(x, x ** 3 + np.sin(x) - 12 * x + 1)
    plt.show()


def main():
    tmp(0.095, 0.09, 0.1)
    tmp(4, 4.005, 3.095)

    # x1 = 0.09
    # x2 = 0.1
    # x_0 = 0.095
    # print(f"\nx_0 = {x_0}")
    # print(f"x1 = {x1}")
    # print(f"x2 = {x2}")
    # delta = np.abs(x1 - x_0)
    # print(f"\ndelta = {delta}")
    #
    # print(f"\nПервое условие теоремы:")
    # print(f"|fi(x1) - fi(x2)| = {np.abs(fi(x1) - fi(x2))}")
    # print(f"|x1 - x2| = {np.abs(x1 - x2)}")
    # q = np.abs(fi(x1) - fi(x2)) / np.abs(x1 - x2)
    # print(f"q = {q}")
    #
    # print(f"\nВторое условие теоремы:")
    # print(f"|x_0 - fi(x_0)| = {np.abs(x_0 - fi(x_0))}")
    # m = np.abs(x_0 - fi(x_0))
    # print(f"m = {m}")
    #
    # print(f"\nТретье условие теоремы:")
    # print(f"m/(1-q) = {m / (1 - q)}")
    # print(f"m/(1-q) <= delta\n{m / (1 - q)} <= {delta}")
    #
    # print(f"\nИтерации:")
    # step = 0
    # print(f"step = {step}\tx_0 = {x_0}")
    # x_1 = fi(x_0)
    # step += 1
    # print(f"step = {step}\tx_1 = {x_1}")
    # step += 1
    # x = 0.0909661
    # print(f"|x_n+1 - x_n| = {np.abs(x_1 - x_0)}")
    #
    # while np.abs(x_1 - x_0) >= var.eps:
    #     x_0 = x_1
    #     x_1 = fi(x_0)
    #     print(f"\nstep = {step}\tx_{step} = {x_1}")
    #     step += 1
    #     print(f"|x_n+1 - x_n| = {np.abs(x_1 - x_0)}")
    #
    # print("\nПроверка: ")
    # print(f"|f(x_n) - eps| = {np.abs(f(x_1) - var.eps)}")

    x = np.arange(-10, 10, 0.01)
    y = np.array(x ** 3 + np.sin(x) - 12 * x + 1)
    plt.plot(x, y)
    plt.xlim((-5, 5))
    plt.ylim((-4, 4))
    plt.grid(which='major',
             color='k')
    plt.show()


if __name__ == "__main__":
    main()
