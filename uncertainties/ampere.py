from uncertainties import ufloat_fromstr
from math import pi, sqrt

m0 = ufloat_fromstr('1.25663706212(19)e-6')
print('µ_0/(4πx10^-7) =', m0/4/pi/1e-07)
dyn = 1e-05
abA = sqrt(dyn)
x = (m0/4/pi)**.5/abA
print('1 A =', x, 'abA')
print('1 abA =', 1/x, 'A')