from uncertainties import ufloat
from math import pi

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
# e = 1.602176634e-19
# https://physics.nist.gov/cgi-bin/cuu/Value?ryd
r_inf = 10973731.568160
r_inf = ufloat(r_inf, r_inf*1.9e-12)
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
me = 4*pi*hbar*r_inf/c/a**2
a0 = hbar/a/me/c
au_v = c*a
au_t = 1/4/pi/c/r_inf
hartree = 4*pi*hbar*c*r_inf
print('m_e =', me, 'kg')
print('a_0 =', a0, 'm')
print('1   =', au_v, 'm/s')
print('1   =', au_t, 's')
print('1   =', hartree, 'J')