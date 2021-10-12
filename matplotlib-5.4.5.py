import matplotlib.pyplot as plt
import numpy as np

# 在区间(-pi, pi]上定义一个分段函数，x<0,f(x)=-1; x>=0,f(x)=1
x=np.linspace(-np.pi, np.pi, 101)
f=np.ones_like(x)
f[x<0]=-1

# 构造傅里叶级数
def Fourier(x, m):
	result = 0
	n = 2*m + 1
	for i in range(1, n, 2):
		result += (4/np.pi)*(np.sin(x*i)/i)
	return result



# 构造指定级数的傅里叶级数公式
y1 = Fourier(x, 2)
y2 = Fourier(x, 4)
y3 = Fourier(x, 6)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, f, 'b-', lw=3, label='f(x)')
ax.plot(x, y1, 'c--', lw=2, label='two terms')
ax.plot(x, y2, 'r-', lw=2, label='four terms')
ax.plot(x, y3, 'b:', lw=2, label='six terms')
ax.legend(loc='best')
ax.set_xlabel('x', style='italic')
ax.set_ylabel('partial sums', style='italic')
fig.suptitle('Partial sums for Fourier series of f(x)', size=16, weight='bold')

plt.show()