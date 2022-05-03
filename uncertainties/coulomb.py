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
statC = sqrt(dyn)*cm
x = 1/(4*pi*e0)**.5/statC
print('1 C =', x, 'statC')
print('1 statC =', 1/x, 'C')
erg = 1e-07
print('Voltage:     1 statV =', x*erg, 'V')
print('Resistance:  1 s/cm  =', x**2*erg, 'Ω')
print('Capacitance: 1 cm    =', 1/x**2/erg, 'F')
print('Inductance:  1 s²/cm =', x**2*erg, 'H')