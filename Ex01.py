import sympy as sp
import numpy as np

x = sp.Symbol('x', positive=True, real=True)

print('p1(x) = ', sp.series(sp.log(x), x, 1, n=2).removeO())
print('p2(x) = ', sp.series(sp.log(x), x, 1, n=3).removeO())
print('p3(x) = ', sp.series(sp.log(x), x, 1, n=4).removeO())


def p1log(x):
    return x - 1


def p2log(x):
    return x - 1 - 0.5 * (x - 1)**2


def p3log(x):
    return x - 1 - 0.5 * (x - 1)**2 + (1/3) * (x - 1)**3

print('  x    p1(x)   p2(x)     p3(x)     log(x)')
for x in [0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5]:
    print('{0:4.1f}   {1:4.1f}   {2:6.3f}   {3:8.5f}   {4:8.5f}'.format(x, p1log(x), p2log(x), p3log(x), np.log(x)))
