from uncertainties import ufloat_fromstr
from math import pi, sqrt

c = 299792458
h = 6.62607015e-34
e = 1.602176634e-19
a1 = ufloat_fromstr('137.035999084(21)')
e0 = e**2*a1/2/c/h
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