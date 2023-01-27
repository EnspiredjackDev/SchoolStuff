import matplotlib.pyplot as plt
import numpy as np
def one():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array(["red","green","blue","pink","orange","cyan","magenta","gray","brown","black","yellow","purple","darkred"])
    plt.scatter(x, y, color = colors)
    plt.show()
    return
def two():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    plt.scatter(x, y, c = colors, cmap='viridis')
    plt.colorbar()
    plt.show()
    return
which = input('?')
if which == '1':
    one()
elif which == '2':
    two()