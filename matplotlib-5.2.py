import numpy as np
import matplotlib.pyplot as plt

plt.ion()

x=np.linspace(-np.pi, np.pi, 101)
y=np.sin(x)+np.sin(3*x)/3.0

plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('A simple plot')

# plt.show()