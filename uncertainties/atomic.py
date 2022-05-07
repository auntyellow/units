from uncertainties import ufloat, ufloat_fromstr
from math import pi

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
e = 1.602176634e-19
me = ufloat_fromstr('9.1093837015(28)e-11')
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
a0 = hbar/a/me/c
print('a_0 =', a0, 'm')