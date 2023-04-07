import numpy as np


def p(x):
    return -2 / x


def q(x):
    return 4 / (x ** 2 + 2)


def f(x):
    return 8


# для первой системы
def f_z(x, z, s):
    return s


def f_s(x, z, s):
    return -p(x) * s + q(x) * z + f(x)


# для второй системы
def f_z1(x1, z1, s1):
    return s1


def f_s1(x1, z1, s1):
    return -p(x1) * s1 + q(x1) * z1


# для третьей системы
def f_z2(x2, z2, s2):
    return s2


def f_s2(x2, z2, s2):
    return -p(x2) * s2 + q(x2) * z2


print("Численное решение с помощью метода R - К, r = 1")

# первая з-К
z = list
s = list
h = 0.1
x_list = np.arange(5, 11, 1)
# начальные условия
x = 0.5
z = 0
s = 0
z_list = [z]
s_list = [s]
for i in x_list[1:]:
    z_new = z + h * f_z(x, z, s)
    s_new = s + h * f_s(x, z, s)
    z_list.append(z_new)
    s_list.append(s_new)
    z = z_new
    s = s_new
    x = i * 0.1
print("Вычисления для первой задачи Коши")
for i in zip(x_list, z_list, s_list):
    print(f"x_i = {i[0] * 0.1}\tz_xi = {i[1]}\ts_xi = {i[2]}")
print()

# вторая з-К
z1 = list
s1 = list
h = 0.1
x1_list = np.arange(5, 12, 1)
# начальные условия
x1 = 0.5
z1 = 0
s1 = 1
z1_list = [z1]
s1_list = [s1]
for i in x1_list[1:]:
    z1_new = z1 + h * f_z1(x1, z1, s1)
    s1_new = s1 + h * f_s1(x1, z1, s1)
    z1_list.append(z1_new)
    s1_list.append(s1_new)
    z1 = z1_new
    s1 = s1_new
    x1 = i * 0.1
print("Вычисления для второй задачи Коши")
for i in zip(x1_list, z1_list, s1_list):
    print(f"x1_i = {i[0] * 0.1}\tz1_xi = {i[1]}\ts1_xi = {i[2]}")
print()

# третья з-К
z2 = list
s2 = list
h = 0.1
x2_list = np.arange(5, 11, 1)
# начальные условия
x2 = 0.5
z2 = 1
s2 = 0
z2_list = [z2]
s2_list = [s2]
for i in x1_list[1:]:
    z2_new = z2 + h * f_z2(x2, z2, s2)
    s2_new = s2 + h * f_s2(x2, z2, s2)
    z2_list.append(z2_new)
    s2_list.append(s2_new)
    z2 = z2_new
    s2 = s2_new
    x2 = i * 0.1
print("Вычисления для третьей задачи Коши")
for i in zip(x2_list, z2_list, s2_list):
    print(f"x2_i = {i[0] * 0.1}\tz2_xi = {i[1]}\ts2_xi = {i[2]}")
print()

# находим c1, c2
alfa0 = 0
alfa1 = 1
beta0 = 1
beta1 = 1
gamma0 = 0.5
gamma1 = 1

A = np.array([[alfa0 * z1_list[0] + beta0 * s1_list[0], alfa0 * z2_list[0] + beta0 * s2_list[0]],
              [alfa1 * z1_list[-1] + beta1 * s1_list[-1],
               alfa1 * z2_list[-1] + beta1 * s2_list[-1]]])  # Матрица (левая часть системы)
print(f"A = {A}")
free_koef = np.array([gamma0 - alfa0 * z_list[0] - beta0 * s_list[0],
                      gamma1 - alfa1 * z_list[-1] - beta1 * s_list[-1]])  # Вектор (правая часть системы)
print(f"B = {free_koef}")
print(f"\n{A[0][0]}*c1 + {A[0][1]}*c2 = {free_koef[0]}")
print(f"{A[1][0]}*c1 + {A[1][1]}*c2 = {free_koef[1]}\n")
c1, c2 = np.linalg.solve(A, free_koef)
print(f"c1 = {c1}")
print(f"c2 = {c2}\n")

# находим y-ки
print("Вычисление y(x)")
y = z_list[0] + c1 * z1_list[0] + c2 * z2_list[0]
y_list = [y]
for i in range(1, 6, 1):
    y_new = z_list[i] + c1 * z1_list[0] + c2 * z2_list[0]
    y_list.append(y_new)
    y = y_new
for i in zip(x_list, y_list):
    print(f"x_i = {i[0] * 0.1}\ty_xi = {i[1]}")
print()

# проверка
h = 0.1

y_dif_a = (y_list[1] - y_list[0]) / h
y_dif_b = (y_list[-1] - y_list[-2]) / h

print("Проверка:")
print(f"|{alfa0} * {y_list[0]} + {beta0} * {y_dif_a} - {gamma0}| = {abs(alfa0 * y_list[0] + beta0 * y_dif_a - gamma0)}")
print(f"|{alfa1} * {y_list[-1]} + {beta1} * {y_dif_b} - {gamma1}| = {abs(alfa1 * y_list[-1] + beta1 * y_dif_b - gamma1)}")


