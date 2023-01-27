import matplotlib.pyplot as plt
import numpy as np
def one():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()
    return
def two():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints, 'o')
    plt.show()
    return
def three():
    xpoints = np.array([1, 2, 6, 8])
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(xpoints, ypoints)
    plt.show()
    return
def four():
    ypoints = np.array([3, 8, 1, 10, 5, 7])

    plt.plot(ypoints)
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
