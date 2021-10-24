import sympy.plotting as syp
import sympy as sy


# syp.plot()
# 1.绘制正弦函数与其前3项级数展开
# x = sy.symbols('x')
# syp.plot(sy.sin(x), x, x-x**3/6, x-x**3/6+x**5/120, (x, -4, 4), title='sin(x) and its first three Taylor approximants')


# syp.plot_parametric()
# 2.绘制隐式定义的二维曲线
# u = sy.symbols('u')
# xc = sy.cos(u) + sy.cos(7*u)/2 + sy.sin(17*u)/3
# yc = sy.sin(u) + sy.sin(7*u)/2 + sy.cos(17*u)/3
# fig2 = syp.plot_parametric(xc, yc, (u, 0, 2*sy.pi))
# # fig2.save('foo.pdf')


# syp.plot_implicit()
# 3.绘制平面中隐式定义的一条或多条曲线
# x, y = sy.symbols('x y')
# syp.plot_implicit(x**2+x*y+y**2-1, (x, -1.5, 1.5), (y, -1.5, 1.5))

# 4.复平面曲线
# real=True x，y参数取实数范围
# x, y = sy.symbols('x y', real=True)
# z = x + sy.I*y
# # complex=True 表达式展开为包含实部与虚部的形式
# w = sy.cos(z**2).expand(complex=True)
# wa = sy.Abs(w).expand(complex=True)
# syp.plot_implicit(wa**2-1)

# 5.图形化二维空间范围
# x, y = sy.symbols('x y')
# syp.plot_implicit(sy.And(x**2+y**2<4, x*y>1), (x,0,2), (y,0,2), line_color='blue')


# syp.plot3d() 绘制曲面
# syp.plot3d_parametric_line() 绘制参数化3d曲线
# syp.plot3d_parametric_surface() 绘制参数化3d曲面
# 6.绘制3D曲线与曲面
# x,y,u= sy.symbols('x y u')
# syp.plot3d_parametric_line(u*sy.cos(4*u), u*sy.sin(4*u), u, (u, 0, 10))
# syp.plot3d((x**2+y**2, (x, -3, 3),(y, -3, 3)),
#            (x*y, (x, -5, 5),(y, -5, 5)))
u,v = sy.symbols('u v')
x=(3+sy.sin(u)+sy.cos(v))*sy.cos(2*u)
y=(3+sy.sin(u)+sy.cos(v))*sy.sin(2*u)
z=2*sy.cos(u)+sy.sin(v)
syp.plot3d_parametric_surface(x, y, z, (u, 0, 2*sy.pi), (v, 0, 2*sy.pi))