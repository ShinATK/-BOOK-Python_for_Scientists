import numpy as np
import numpy.random as npr

x=np.linspace(0, 4, 21)
y=np.exp(-x)
xe=0.08*npr.randint(len(x))
ye=0.1*npr.randint(len(y))

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(x,y,fmt='bo', lw=2, xerr=xe, yerr=ye, ecolor='r', elinewidth=1)

plt.show()