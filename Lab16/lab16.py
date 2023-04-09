import numpy as np

alfa0 = 0
alfa1 = 1
beta0 = 1
beta1 = 1
gamma0 = 0.5
gamma1 = 1
t1 = 1
t2 = 2


def p(x):
    return -2 / x


def q(x):
    return 4 / (x ** 2 + 2)


def f(x):
    return 8


def f_z1(x, z1):
    return -z1 * z1 - p(x) * z1 + q(x)


def f_z2(x, z1, z2):
    return -z1 * z2 - p(x) * z2 + f(x)


def f_y(z1, z2, y):
    return z1 * y + z2


print("\nЧисленное решение с помощью метода R - К, r = 1")

h = 0.1
x1_list = np.arange(5, 11, 1)
# начальные условия
x = 0.5
z1 = -alfa0 / beta0
z1_list = [z1]
z2 = gamma0 / beta0
z2_list = [z2]
for i in x1_list[1:]:
    z1_new = z1 + h * f_z1(x, z1)
    z2_new = z2 + h * f_z2(x, z1, z2)
    z1_list.append(z1_new)
    z2_list.append(z2_new)
    z1 = z1_new
    z2 = z2_new
    x = i * 0.1

print(f"Вычисления для задачи Коши z1(x), z2(x)")
for i in zip(x1_list, z1_list, z2_list):
    print(f"x_i = {i[0] * 0.1}\t\tz1_xi = {i[1]}\t\tz2_xi = {i[2]}")
print()

x2_list = np.arange(10, 4, -1)
# начальные условия
x = 1
y = (gamma1 - beta1 * z2_list[-1]) / (alfa1 + beta1 * z1_list[-1])
y_list = [y]
for i in x2_list[1:]:
    y_new = y - h * f_y(z1_list[i - 10], z2_list[i - 10], y)
    y_list.append(y_new)
    y = y_new

y_list.reverse()  # от 0.5 до 1
print(f"Вычисления для задачи Коши y(x)")
for i in zip(range(5, 11, 1), y_list):
    print(f"x_i = {i[0] * 0.1}\t\ty_xi = {i[1]}")
print()

# проверка

y_dif_a = (y_list[1] - y_list[0]) / h
y_dif_b = (y_list[-1] - y_list[-2]) / h

print("Проверка:")
print(f"|{alfa0} * {y_list[0]} + {beta0} * {y_dif_a} - {gamma0}| = {abs(alfa0 * y_list[0] + beta0 * y_dif_a - gamma0)}")
print(
    f"|{alfa1} * {y_list[-1]} + {beta1} * {y_dif_b} - {gamma1}| = {abs(alfa1 * y_list[-1] + beta1 * y_dif_b - gamma1)}")
