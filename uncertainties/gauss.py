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
# magnetic B field
gs = sqrt(dyn)/cm
x = gs/(4*pi*e0)**.5/c
print('1 G =', x, 'T')
print('1 T =', 1/x, 'G')
# magnetic flux
mx = gs*cm**2
x = mx/(4*pi*e0)**.5/c
print('1 Mx =', x, 'Wb')
print('1 Wb =', 1/x, 'Mx')
# magnetic dipole moment
statC = sqrt(dyn)*cm
x = statC*cm*(4*pi*e0)**.5*c
print('1 erg/G =', x, 'J/T')
print('1 J/T =', 1/x, 'erg/G')