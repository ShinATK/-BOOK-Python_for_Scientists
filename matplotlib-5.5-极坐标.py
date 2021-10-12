import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(0, 2*np.pi, 201)
r1=np.abs(np.cos(5.0*theta)-1.5*np.sin(3.0*theta))
r2=theta/np.pi
r3=2.25*np.ones_like(theta)

fig = plt.figure()
ax=fig.add_subplot(111, projection='polar')

ax.plot(theta, r1, label='trig')
ax.plot(5*theta, r2, label='spiral')
ax.plot(theta, r3, label='circle')
ax.legend(loc='best')
plt.show()
