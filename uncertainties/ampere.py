from uncertainties import ufloat_fromstr
from math import pi, sqrt

c = 299792458
h = 6.62607015e-34
e = 1.602176634e-19
a1 = ufloat_fromstr('137.035999084(21)')
e0 = e**2*a1/2/c/h
m0 = 1/c**2/e0
# m0 = ufloat_fromstr('1.25663706212(19)e-6')
print('µ_0 =', m0, 'N/A²')
print('µ_0/(4πx10^-7) =', m0/4/pi/1e-07, 'N/A²')
dyn = 1e-05
abA = sqrt(dyn)
x = (m0/4/pi)**.5/abA
print('1 A =', x, 'abA')
print('1 abA =', 1/x, 'A')