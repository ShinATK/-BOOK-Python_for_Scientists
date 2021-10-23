import sympy as sy

sy.init_printing()

# 1.书写代数表达式
x,y = sy.symbols('x, y')
D = (x+y)*sy.exp(x)*sy.cos(y)
print(D)

# 2.书写未知函数
# 向symbols中传递参数 cls=sy.Function
f, g = sy.symbols('f, g', cls=sy.Function)
print(f(x), f(x,y), g(x))