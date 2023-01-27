import matplotlib.pyplot as plt
import numpy as np
def one():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, linestyle = "dashed")

    plt.grid()

    plt.show()
    return
def two():

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, ls = ":")

    plt.grid()

    plt.show()
    return
def three():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, ls = ":", color = "r")

    plt.grid()

    plt.show()
    return
def four():
    y1 = np.array([3, 8, 1, 10])
    y2 = np.array([6, 2, 7, 11])

    plt.plot(y1)
    plt.plot(y2)

    plt.grid()

    plt.show()
    return
def five():
    x1 = np.array([0, 1, 2, 3])
    y1 = np.array([3, 8, 1, 10])
    x2 = np.array([0, 1, 2, 3])
    y2 = np.array([6, 2, 7, 11])

    plt.plot(x1, y1, x2, y2)
    plt.show()
which = input('?')
if which == '1':
    one()
elif which == '2':
    two()
elif which == '3':
    three()
elif which == '4':
    four()
elif which == '5':
    five()
