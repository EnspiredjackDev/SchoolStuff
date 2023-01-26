"""
import matplotlib.pyplot as plt
import numpy as np


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.xlabel("jovi")
plt.ylabel("ben")

plt.grid()
plt.show()

"""

"""
import matplotlib.pyplot as plt
import numpy as np


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)

plt.title("name")
plt.xlabel("jovi")
plt.ylabel("ben")

plt.grid()
plt.show()
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {"family":"serif","color":"blue","size":20}
font2 = {"family":"serif","color":"darkred","size":15}

plt.plot(x,y)

plt.title("name", fontdict = font1)
plt.xlabel("jovi", fontdict = font2)
plt.ylabel("ben", fontdict = font2)

plt.plot(x,y)
plt.grid()
plt.show()


"""
import matplotlib.pyplot as plt
import numpy as np


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {"family":"serif","color":"blue","size":20}
font2 = {"family":"serif","color":"darkred","size":15}

plt.plot(x,y)

plt.title("name", loc = "left", fontdict = font1)
plt.xlabel("jovi", fontdict = font2)
plt.ylabel("ben", fontdict = font2)

plt.plot(x,y)
plt.grid()
plt.show()
"""
