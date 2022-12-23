import numpy as np
from matplotlib import pyplot as plt

import Variables as var


def f(x):
    return x ** 4 - 4 * (x ** 3) + 5.98 * (x ** 2) - 3.96 * x + 0.09801


def first_derivative_f(x):
    return 4 * (x ** 3) - 12 * (x ** 2) + 11.96 * x - 3.96


def second_derivative_f(x):
    return 12 * (x ** 2) - 24 * x + 11.96


def draw_graphic():
    x = np.arange(-10, 10, 0.01)
    plt.plot(x, x ** 3 + np.sin(x) - 12 * x + 1)
    plt.show()


def next_x(current_x):
    return current_x - (f(current_x) / first_derivative_f(current_x))


def check_theorem_conditions(x0):
    print(f"\nx0 = {x0}")
    B = np.abs(1 / first_derivative_f(x0))
    n = np.abs(f(x0) / first_derivative_f(x0))
    K = np.max(np.abs(second_derivative_f(x0)))
    h = B * n * K
    isTrue = h <= 0.5
    print("Проверка условий теоремы:")
    print(f"|f''(x)| <= K = {K}")
    print(f"|1 / (f'(x0))| <= B = {B}")
    print(f"|f(x0) / f'(x0)| <= n = {n}")
    print(f"h = K*B*n = {h}, h <= 0.5 ? {isTrue}")


def newton_method(x0):
    x_n = x0
    x_n_next = next_x(x_n)
    step = 1
    print("\nИтерации:")
    while np.abs(x_n_next - x_n) > var.eps:
        x_n = x_n_next
        x_n_next = next_x(x_n_next)
        print(f"Шаг {step}")
        print(f"x_n = {x_n}, x_n+1 = {x_n_next}")
        step += 1
    return x_n_next


def main():
    print("\nf(x) = x^4 - 4*x^3 + 5.98*x^2 - 3.96*x + 0.09801")
    print("f'(x) = 4*x^3 - 12*x^2 + 11.96*x - 3.96")
    print("f''(x) = 12*x^2 - 24*x + 11.96")
    x0_1 = 0.1
    x0_2 = 2

    x0 = x0_1
    check_theorem_conditions(x0)
    first_root = newton_method(x0)
    print(f"\nПервый корень = {first_root}, f(x) = {f(first_root)}")

    x0 = x0_2
    check_theorem_conditions(x0)
    second_root = newton_method(x0)
    print(f"\nВторой корень = {second_root}, f(x) = {f(second_root)}")

    x = np.arange(-0.5, 2.5, 0.01)
    y = np.array(x ** 4 - 4 * (x ** 3) + 5.98 * (x ** 2) - 3.96 * x + 0.09801)
    plt.plot(x, y)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.show()


if __name__ == "__main__":
    main()
