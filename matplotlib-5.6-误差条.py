import numpy as np
import numpy.random as npr

# 建立数据
x=np.linspace(0, 4, 21)
y=np.exp(-x)

# 与基数据的误差
xe=0.008*npr.randint(len(x))
ye=0.1*npr.randint(len(y))

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
# xerr=, yerr=, 参数设置误差
ax.errorbar(x,y,fmt='bo', lw=2, xerr=xe, yerr=ye, ecolor='r', elinewidth=1)

plt.show()