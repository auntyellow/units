from uncertainties import ufloat_fromstr
from math import pi, sqrt

e0 = ufloat_fromstr('8.8541878128(13)e-12')
dyn = 1e-05
cm = 1e-02
statC = sqrt(dyn)*cm
x = 1/(4*pi*e0)**.5/statC
print('1 C =', x, 'statC')
print('1 statC =', 1/x, 'C')