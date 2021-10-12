import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

[X,Y] = np.mgrid[-2.5:2.5:51j, -3:3:61j]
Z = X**2 - Y**2

curves = ax.contour(X, Y, Z, 12, colors='k')
ax.clabel(curves)

fig.suptitle(r"The level contours of $Z=X^2-Y^2$", fontsize=20)

plt.show()