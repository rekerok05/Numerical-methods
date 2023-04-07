import numpy as np


def f_y(x, y, z):
    dydt = np.power(np.e, -(y ** 2 + z ** 2)) + 2 * x
    return dydt


def f_z(x, y, z):
    dzdt = 3 * np.power(y, 2) + z
    return dzdt


print("Численное решение с помощью метода R - К, r = 1\n")
y = list
h = 0.1
x_list = np.arange(0, 0.4, h)
x = 0
y = 0.5
y_list = [y]
z = 1
z_list = [z]
for i in x_list[1:]:
    y_new = y + h * f_y(x, y, z)
    z_new = z + h * f_z(x, y, z)
    y_list.append(y_new)
    z_list.append(z_new)
    y = y_new
    z = z_new
    x = i
for i in zip(x_list, y_list, z_list):
    print(f"x_i = {i[0]}\ty_xi = {i[1]}\tz_xi = {i[2]}")
print()

print("\nЧисленное решение с помощью метода R - К, r = 4")
y = y_list[0]
z = z_list[0]
x = 0
h = 0.1
print(y, z)
k1_1 = h * f_y(x, y, z)
k1_2 = h * f_z(x, y, z)
k2_1 = h * f_y(x + h / 2, y + k1_1 / 2, z + k1_2 / 2)
k2_2 = h * f_z(x + h / 2, y + k1_1 / 2, z + k1_2 / 2)
k3_1 = h * f_y(x + h / 2, y + k2_1 / 2, z + k2_2 / 2)
k3_2 = h * f_z(x + h / 2, y + k2_1 / 2, z + k2_2 / 2)
k4_1 = h * f_y(x + h, y + k3_1, z + k3_2)
k4_2 = h * f_z(x + h, y + k3_1, z + k3_2)
y_list = [y]
z_list = [z]
for i in x_list[1:]:
    y_new = y + (1 / 6) * (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1)
    z_new = z + (1 / 6) * (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2)
    y_list.append(y_new)
    y = y_new
    z_list.append(z_new)
    z = z_new
    x = i
    k1_1 = h * f_y(x, y, z)
    k1_2 = h * f_z(x, y, z)
    k2_1 = h * f_y(x + h / 2, y + k1_1 / 2, z + k1_2 / 2)
    k2_2 = h * f_z(x + h / 2, y + k1_1 / 2, z + k1_2 / 2)
    k3_1 = h * f_y(x + h / 2, y + k2_1 / 2, z + k2_2 / 2)
    k3_2 = h * f_z(x + h / 2, y + k2_1 / 2, z + k2_2 / 2)
    k4_1 = h * f_y(x + h, y + k3_1, z + k3_2)
    k4_2 = h * f_z(x + h, y + k3_1, z + k3_2)
for i in zip(x_list, y_list, z_list):
    print(f"x_i = {i[0]}\ty_xi = {i[1]}\tz_xi = {i[2]}")
