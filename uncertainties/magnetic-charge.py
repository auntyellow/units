from uncertainties import ufloat
from math import pi, sqrt

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
e = 1.602176634e-19
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
cm = 1e-02
dyn = 1e-05
erg = 1e-07
statC = sqrt(dyn)*cm
print(f'1 n.u. = {sqrt(hbar*c/4/pi)/statC} statC = {(4*pi*a)**.5*hbar/e:S} Wb')
print(f'1 C = {c} A m = {(4*pi*a)**.5/e:S} n.u.')