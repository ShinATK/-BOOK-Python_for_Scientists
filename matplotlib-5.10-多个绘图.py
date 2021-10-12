import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 101)
y1 = 1.0/(x+1.0)
y2 = np.exp(-x)
y3 = np.exp(-0.1*x**2)
y4 = np.exp(-5*x**2)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y1')

ax2 = fig.add_subplot(222)
ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('y2')

ax3 = fig.add_subplot(223)
ax3.plot(x, y3)
ax3.set_xlabel('x')
ax3.set_ylabel('y3')

ax4 = fig.add_subplot(224)
ax4.plot(x, y4)
ax4.set_xlabel('x')
ax4.set_ylabel('y4')

fig.suptitle('Various decay functions')
plt.show()