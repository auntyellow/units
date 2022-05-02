from uncertainties import ufloat_fromstr
from math import pi, sqrt

e0 = ufloat_fromstr('8.8541878128(13)e-12')
dyn = 1e-05
cm = 1e-02
g = sqrt(dyn)/cm
c = 299792458
x = g/(4*pi*e0)**.5/c
print('1 G =', x, 'T')
print('1 T =', 1/x, 'G')