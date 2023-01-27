import matplotlib.pyplot as plt
import numpy as np
def one():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker = 'o')
    plt.show()
    return
def two():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker = 'o', ms = 20)
    plt.show()
    return
def three():

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
    plt.show()
    return
def four():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
    plt.show()

    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
    plt.show()
    return
def five():
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
    plt.show()
    return
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