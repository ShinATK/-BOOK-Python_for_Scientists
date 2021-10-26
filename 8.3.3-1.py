import numpy as np
from scipy.integrate import odeint

def rhs(y, t, mu):
    return [y[1], mu*(1-y[0]**2)*y[1]-y[0]]
    
def jac(y, t, mu):
    return [[0, 1], [-2*mu*y[0]*y[1]-1, mu*(1-y[0]**2)]]

mu = 1.0
t_final = 15.0 if mu<10 else 4.0*mu
n_points = 1001 if mu<10 else 1001*mu
t = np.linspace(0, t_final, n_points)
y0 = np.array([2.0, 0.0])
y, info = odeint(rhs, y0, t, args=(mu,), Dfun=jac, full_output=True)

print('mu=%g, number of Jacobian calls is %d'%(mu, info['nje'][-1]))

import matplotlib.pyplot as plt
plt.plot(y[:,0], y[:,1])
plt.show()