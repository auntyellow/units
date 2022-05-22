'''
from sympy import *

x, y, d = symbols('x, y, d')
f = x**3/sqrt((x**2 + y**2)*(x**2 + (y - d)**2))**3
print(integrate(f, (y, -oo, +oo), (x, 0, +oo)))
'''

from numpy import inf, sqrt
from scipy.integrate import nquad

def f(x, y, d):
    return x**3/sqrt((x**2 + y**2)*(x**2 + (y - d)**2))**3

def integral(d):
    result, abserr = nquad(lambda x, y : f(x, y, d), [[0, +inf], [-inf, +inf]])
    print(f'Integral(f, d={d}) = {result}')

integral(.1)
integral(.2)
integral(.5)
integral(1)
integral(2)
integral(5)
integral(10)