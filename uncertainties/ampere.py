from uncertainties import ufloat
from math import pi, sqrt

c = 299792458
h = 6.62607015e-34
e = 1.602176634e-19
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
m0 = 2*h*a/e**2/c
# m0 = ufloat_fromstr('1.25663706212(19)e-6')
print('µ_0 =', m0, 'N/A^2')
print('µ_0/(4πx10^-7) =', m0/4/pi/1e-07, 'N/A^2')
dyn = 1e-05
abA = sqrt(dyn)
x = (m0/4/pi)**.5/abA
print('1 A =', x, 'abA')
print('1 abA =', 1/x, 'A')