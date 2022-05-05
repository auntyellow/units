from uncertainties import ufloat
from math import pi, sqrt

c = 299792458
h = 6.62607015e-34
e = 1.602176634e-19
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
e0 = e**2/2/c/h/a
# e0 = ufloat_fromstr('8.8541878128(13)e-12')
print('ε_0 =', e0, 'F/m')
dyn = 1e-05
cm = 1e-02
statV = sqrt(dyn)
x = (e0/4/pi)**.5*statV/cm
print('1 statV/cm =', x, 'C/m^2')