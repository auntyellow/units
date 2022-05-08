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
print(f'ε_0 = {e0:S} F/m')
dyn = 1e-05
cm = 1e-02
statC = sqrt(dyn)*cm
# M(G) = 1/sqrt(4*pi*ε_0)/c*M(SI)
# 1 erg/G cm^3 (statC/cm^2) = x/sqrt(4*pi*ε_0)*c*A/m
x = (4*pi*e0)**.5*c*statC/cm**2
print(f'1 erg/G cm^3 = {x:S} A/m')
# H(G) = sqrt(4*pi/ε_0)/c*H(SI)
# 1 Oe (statC/cm^2) = sqrt(4*pi/ε_0)/c*x*A/m
x = (e0/4/pi)**.5*c*statC/cm**2
print(f'1 Oe = {x:S} A/m')