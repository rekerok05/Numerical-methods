import numpy as np
import sympy as sp

t = sp.Symbol("t")
y = sp.Function("y")(t)
print(y)
diff_eq = sp.Eq(y.diff(t), 2 * y - t ** 2)
print(sp.dsolve(diff_eq, y))


def f_y(y, t, a=2):
    dydt = a * y - pow(t, 2)
    return dydt


def f_z(z, t, a=2):
    dzdt = -z + a * t
    return dzdt


# y0 = 1
# t = np.linspace(-9, 9, 30)
# y = odeint(f_s, y0, t)
# plt.plot(t, y)
# plt.grid()
# plt.show()

print("Численное решение с помощью метода R - К, r = 1\n")

y = list
h = 0.1
x_list = np.arange(0, 0.6, h)
x = 0
y = 1
y_list = [y]
for i in x_list[1:]:
    y_new = y + h * f_y(y, x)
    y_list.append(y_new)
    y = y_new
    x = i
for i in zip(x_list, y_list):
    print(f"x_i = {i[0]}\ty_xi = {i[1]}")
print()
z = y_list[len(y_list) - 1]
h = -h
z_list = [z]
for i in np.flip(x_list)[1:]:
    z_new = z + h * f_z(z, x)
    z_list.append(z_new)
    z = z_new
    x = i

for i in zip(np.flip(x_list), z_list):
    print(f"x_i = {i[0]}\tz_xi = {i[1]}")

print("\nЧисленное решение с помощью метода R - К, r = 2")
h = -h
y = y_list[0]
y_tilda = y_list[0] + h * f_y(y, x)
y_list = [y]
for i in x_list[1:]:
    y_new = y + (h / 2) * (f_y(y, x) + f_y(y_tilda, x + h))
    y_tilda = y_new + h * f_y(y_new, x + h)
    y_list.append(y_new)
    x = i
    y = y_new
for i in zip(x_list, y_list):
    print(f"x_i = {i[0]}\ty_xi = {i[1]}")
print()

z = y_list[len(y_list) - 1]
h = -h
z_tilda = z + h * f_z(z, x)
z_list = [z]
for i in np.flip(x_list)[1:]:
    z_new = z + (h / 2) * (f_z(z, x) + f_z(z_tilda, x + h))
    z_tilda = z_new + h * f_z(z_new, x + h)
    z_list.append(z_new)
    x = i
    z = z_new

for i in zip(np.flip(x_list), z_list):
    print(f"x_i = {i[0]}\tz_xi = {i[1]}")

print("\nЧисленное решение с помощью метода R - К, r = 4")
h = -h
y = y_list[0]
k1 = h * f_y(y, x)
k2 = h * f_y(y + k1 / 2, x + h / 2)
k3 = h * f_y(y + k2 / 2, x + h / 2)
k4 = h * f_y(y + k3, x + h)
y_list = [y]
for i in x_list[1:]:
    y_new = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    y_list.append(y_new)
    y = y_new
    x = i
    k1 = h * f_y(y, x)
    k2 = h * f_y(y + k1 / 2, x + h / 2)
    k3 = h * f_y(y + k2 / 2, x + h / 2)
    k4 = h * f_y(y + k3, x + h)
for i in zip(x_list, y_list):
    print(f"x_i = {i[0]}\ty_xi = {i[1]}")
print()

z = y_list[len(y_list) - 1]
z_list = [z]
h = -h
k1 = h * f_z(z, x)
k2 = h * f_z(z + k1 / 2, x + h / 2)
k3 = h * f_z(z + k2 / 2, x + h / 2)
k4 = h * f_z(z + k3, x + h)
for i in np.flip(x_list)[1:]:
    z_new = z + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    z_list.append(z_new)
    z = z_new
    x = i
    k1 = h * f_z(z, x)
    k2 = h * f_z(z + k1 / 2, x + h / 2)
    k3 = h * f_z(z + k2 / 2, x + h / 2)
    k4 = h * f_z(z + k3, x + h)

for i in zip(np.flip(x_list), z_list):
    print(f"x_i = {i[0]}\tz_xi = {i[1]}")
