import numpy as np

alfa0 = 0
alfa1 = 1
beta0 = 1
beta1 = 1
gamma0 = 0.5
gamma1 = 1
h = 0.1


def p(x):
    return -2 / x


def q(x):
    return 4 / (x ** 2 + 2)


def f(x):
    return 8


def r(x):
    return (-4 - 2 * (h ** 2) * q(x)) / (2 + h * p(x))


def s(x):
    return (2 - h * p(x)) / (2 + h * p(x))


def t(x):
    return (2 * (h ** 2) * f(x)) / (2 + h * p(x))


h = 0.1
x1_list = np.arange(5, 11, 1)
# начальные условия
# x = 0.5
p_list = []
q_list = []
f_list = []
r_list = []
s_list = []
t_list = []

for i in x1_list:
    x = i * h
    p_new = p(x)
    p_list.append(p_new)
    # p = p_new
    q_new = q(x)
    q_list.append(q_new)
    # q = q_new
    f_list.append(f(x))
    r_new = r(x)
    r_list.append(r_new)
    # r = r_new
    s_new = s(x)
    s_list.append(s_new)
    # s = s_new
    t_new = t(x)
    t_list.append(t_new)
    # t = t_new

print(f"\nВычисления p, q, f, r, s, t:")
for i in zip(x1_list, p_list, q_list, f_list, r_list, s_list, t_list):
    print(
        f"x_i = {i[0] * 0.1}\tp_xi = {i[1]}\tq_xi = {i[2]}\tf_xi = {i[3]}\tr_xi = {i[4]}\ts_xi = {i[5]}\tt_xi = {i[6]}")
print()

a0 = -(2 * alfa0 * h * s_list[0] + r_list[0] * beta0) / (beta0 * s_list[0] + beta0)
b0 = (2 * gamma0 * h * s_list[0] + t_list[0] * beta0) / (beta0 * s_list[0] + beta0)
an_1 = (beta1 * s_list[-1] + beta1) / (2 * h * alfa1 - r_list[-1] * beta1)
bn_1 = (2 * h * gamma1 - beta1 * t_list[-1]) / (2 * h * alfa1 - r_list[-1] * beta1)

x2_list = np.arange(5, 11, 1)
# начальные условия
x = 0.5
c = a0
d = b0
c_list = [c]
d_list = [d]
for i in x2_list[1:]:
    x = i * h
    c_new = -r(x) - (s(x)) / c
    d_new = t(x) - r(x) * d - c_new * d
    c_list.append(c_new)
    d_list.append(d_new)
    c = c_new
    d = d_new

print(f"Вычисления c, d:")
for i in zip(x2_list, c_list, d_list):
    print(f"x_i = {i[0] * 0.1}\t\tc_xi = {i[1]}\t\td_xi = {i[2]}")
print()

y_N = (an_1 * d_list[-2] - bn_1 * c_list[-2]) / (an_1 - c_list[-2])
print(f"y_N = {y_N}")

x3_list = np.arange(5, -1, -1)  # [5 4 3 2 1 0]
# print(x3_list)
# начальные условия
y = y_N
y_list = [y]
for i in x3_list[1:]:
    y_new = 1 / c_list[i] * (y - d_list[i])
    y_list.append(y_new)
    y = y_new

y_list.reverse()  # от 0.5 до 1
print(f"\nВычисления y:")
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
