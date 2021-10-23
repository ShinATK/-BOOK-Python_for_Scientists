import sympy as sy
import sympy.plotting as syp

# x,y,u = sy.symbols('x y u')

# 图7-1
# syp.plot(sy.sin(x), x, x-x**3/6, x-x**3/6+x**5/120, (x, -4, 4), title='sin(x) and its first three Taylor approximants')

# 隐式函数
# 图7-2
# xc = sy.cos(u) + sy.cos(7*u)/2 + sy.sin(17*u)/3
# yc = sy.sin(u) + sy.sin(7*u)/2 + sy.cos(17*u)/3
# fig2 = syp.plot_parametric(xc, yc, (u, 0, 2*sy.pi))
# fig2.save('foo.pdf')

# 绘制平面中隐式定义的一条或多条曲线
# syp.plot_implicit
# syp.plot_implicit(x**2+x*y+y**2-1, (x, -1.5, 1.5), (y, -1.5, 1.5))

# 绘制隐式定义曲线|cos((x+iy)**2)|=1
# x,y = sy.symbols('x y', real=True)
# z = x + sy.I*y
# w = sy.cos(z**2).expand(complex=True)
# wa = sy.Abs(w).expand(complex=True)
# syp.plot_implicit(wa**2-1)

# 用图形化的方法来描述分别由x^2+y^2<4和xy>1定义的两个区域在正象限中的交点
# sy.And
# x,y = sy.symbols('x y')
# syp.plot_implicit(sy.And(x**2+y**2<4, x*y>1), (x, 0, 2),(y, 0, 2), line_color='blue')

# 三维曲线和三维曲面
# u = sy.symbols('u')
# syp.plot3d_parametric_line(u*sy.cos(4*u), u*sy.sin(4*u), u, (u, 0, 10))

# z=x**2+y**2 z=x*y
x,y = sy.symbols('x y')
# syp.plot3d((x**2+y**2, (x, -3, 3), (y, -3, 3)), (x*y, (x, -5, 5), (y, -5, 5)))

# 绘制参数化曲面
u,v = sy.symbols('u v')
syp.plot3d((3+sy.sin(u)+sy.cos(v))*sy.cos(2*u), (3+sy.sin(u)+sy.cos(v))*sy.sin(2*u), 2*sy.cos(u)+sy.sin(v), (u, 0, 2*sy.pi), (v, 0, 2*sy.pi))

