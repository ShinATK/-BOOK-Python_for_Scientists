import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

[X,Y] = np.mgrid[-2.5:2.5:51j, -3:3:61j]
Z = X**2 - Y**2

# 1.线条绘制等高线图
# colors='k' 表示曲线以黑色展示
# curves = ax.contour(X, Y, Z, 12, colors='k')
# curves = ax.contour(X,Y,Z,12)
# ax.clabel(curves)

# 2.颜色绘制等高线图
# 用颜色填充等高线之间的空间
# im= ax.contourf(X,Y,Z,12)
# fig.colorbar(im, orientation='vertical')

# 3.隐藏等高线
im = ax.imshow(Z)
fig.colorbar(im,orientation='vertical')

fig.suptitle(r"The level contours of $Z=X^2-Y^2$", fontsize=20)

plt.show()