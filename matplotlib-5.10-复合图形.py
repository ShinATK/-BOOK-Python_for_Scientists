import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 301)
y = np.cos(x)

z = np.sin(x)

# 创建两个绘图窗口
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x, y)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(x, z)

plt.show()