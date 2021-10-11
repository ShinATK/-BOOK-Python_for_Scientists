import numpy as np
import matplotlib.pyplot as plt

roots=[0,1,1,2]
coeffs=np.poly(roots) # np.poly(roots) 返回以roots数值为零点的多项式系数
print("coeffs=\n",coeffs)
print("np.roots(coeffs)=\n", np.roots(coeffs)) # np.roots(poly) 返回多项式poly的零点根
x=np.linspace(0,0.5*np.pi,7)
y=np.sin(x)
c=np.polyfit(x,y,11)
print("c=\n",c)
y1=np.polyval(c,x)
print("y=\n",y,"\n y1=\n",y1,"\n y1-y=\n", y1-y)
plt.subplots()
plt.plot(y)
plt.plot(y1)
plt.show()
