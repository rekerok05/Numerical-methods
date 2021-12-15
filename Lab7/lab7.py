import numpy as np
import Variables as var


def printValue(name, value):
    print(f"{name} = \n{value}")


if __name__ == "__main__":
    tmpy = np.array([[1], [1], [1]])
    tmpz = tmpy / np.max(np.abs(tmpy))
    tmpy = np.dot(var.A, tmpz)
    tmpyz = tmpy / tmpz
    print(f"tmpY = {np.reshape(tmpy, (1, 3))}")
    print(f"tmpZ = {np.reshape(tmpz, (1, 3))}")
    print(f"tmpYZ = {np.reshape(tmpyz, (1, 3))}")
    d1 = tmpyz[0]
    d2 = tmpyz[1]
    d3 = tmpyz[2]
    tmpz = tmpy / np.max(np.abs(tmpy))
    tmpy = np.dot(var.A, tmpz)
    tmpyz = tmpy / tmpz
    print(f"tmpY = {np.reshape(tmpy, (1, 3))}")
    print(f"tmpZ = {np.reshape(tmpz, (1, 3))}")
    print(f"tmpYZ = {np.reshape(tmpyz, (1, 3))}")
    d1new = tmpyz[0]
    d2new = tmpyz[1]
    d3new = tmpyz[2]
    i = 1
    print("------------------------------")
    print("------------------------------")
    tmpVar = np.max(np.abs([d1new - d1, d2new - d2, d2new - d2]))
    while tmpVar > var.eps:
        print(f"STEP {i}")
        print(f"tmpZ/tmpY = {np.reshape(tmpz / tmpy, (1, 3))}")
        print(d1, d2, d3)
        print(np.max(np.abs([d1new - d1, d2new - d2, d2new - d2])))
        tmpz = tmpz = tmpy / np.max(np.abs(tmpy))
        tmpy = np.dot(var.A, tmpz)
        tmpyz = tmpy / tmpz
        d1 = d1new
        d2 = d2new
        d3 = d3new
        d1new = tmpyz[0]
        d2new = tmpyz[1]
        d3new = tmpyz[2]
        tmpVar = np.max(np.abs([d1new - d1, d2new - d2, d2new - d2]))
        i += 1
        print("------------------------------")
    x = tmpy / np.max(np.abs(tmpy))
    printValue("A", var.A)
    printValue("y", tmpy)
    printValue("x", x)
