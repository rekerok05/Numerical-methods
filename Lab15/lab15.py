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


# для второй системы
def f_z1(x1, z1, s1):
    return s1


def f_s1(x1, z1, s1):
    return -p(x1) * s1 + q(x1) * z1 + f(x1)


# для третьей системы
def f_z2(x2, z2, s2):
    return s2


def f_s2(x2, z2, s2):
    return -p(x2) * s2 + q(x2) * z2 + f(x2)


print("Численное решение с помощью метода R - К, r = 1")

# вторая з-К
h = 0.1
x1_list = np.arange(5, 11, 1)
# начальные условия
x1 = 0.5
z1 = t1
s1 = (gamma0 - alfa0 * t1) / beta0
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
print(f"Вычисления для задачи Коши z1(x)")
for i in zip(x1_list, z1_list, s1_list):
    print(f"x1_i = {i[0] * 0.1}\tz1_xi = {i[1]}\ts1_xi = {i[2]}")
print()

# третья з-К
x2_list = np.arange(5, 11, 1)
# начальные условия
x2 = 0.5
z2 = t2
s2 = (gamma0 - alfa0 * t2) / beta0
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
print("Вычисления для задачи Коши z2(x)")
for i in zip(x2_list, z2_list, s2_list):
    print(f"x2_i = {i[0] * 0.1}\tz2_xi = {i[1]}\ts2_xi = {i[2]}")
print()

delta = alfa1 * (z2_list[-1] - z1_list[-1]) + beta1 * (s2_list[-1] - s1_list[-1])
print(f"delta = {delta}")
c = (1 / delta) * (gamma1 - alfa1 * z1_list[-1] - beta1 * s1_list[-1])
print(f"c = {c}")

y_list = []
x_list = range(5, 11, 1)
for i in range(6):
    y_new = (1 - c) * z1_list[i] + c * z2_list[i]
    y_list.append(y_new)
print(f"\nВычисления для y(x)")
for i in zip(x_list, y_list):
    print(f"x_i = {i[0] * 0.1}\ty_xi = {i[1]}")
print()

# проверка
h = 0.1

y_dif_a = (y_list[1] - y_list[0]) / h
y_dif_b = (y_list[-1] - y_list[-2]) / h

print("Проверка:")
print(f"|{alfa0} * {y_list[0]} + {beta0} * {y_dif_a} - {gamma0}| = {abs(alfa0 * y_list[0] + beta0 * y_dif_a - gamma0)}")
print(
    f"|{alfa1} * {y_list[-1]} + {beta1} * {y_dif_b} - {gamma1}| = {abs(alfa1 * y_list[-1] + beta1 * y_dif_b - gamma1)}")

