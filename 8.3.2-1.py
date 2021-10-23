import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rhs(Y, t, omega):
    y, ydot=Y
    return ydot, -omega**2*y
   
t_arr = np.linspace(0, 2*np.pi, 101)
y_init = [1, 0]
omega = 2.0
y_arr = odeint(rhs, y_init, t_arr, args=(omega,))
y, ydot = y_arr[:, 0], y_arr[:, 1]

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(t_arr,y, t_arr,ydot)
ax1.set_xlabel('t')
ax1.set_ylabel('y and ydot')

ax2 = fig.add_subplot(122)
ax2.plot(y, ydot)
ax2.set_xlabel('y')
ax2.set_ylabel('ydot')

plt.suptitle('Solution curve when omega = %5g'%omega)
fig.tight_layout()
fig.subplots_adjust(top=0.90)

plt.show()