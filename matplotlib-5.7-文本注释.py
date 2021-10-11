import numpy as np
x=np.linspace(0, 2, 101)
y=(x-1)**3+1

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x, y)
ax.annotate('point of inflection at x=1', xy=(1,1),
	xytext=(0.8,0.5),
	arrowprops=dict(facecolor='black', width=1, shrink=0.05)
	)
plt.show()
