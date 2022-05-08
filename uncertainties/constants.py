from uncertainties import ufloat
from math import pi

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
e = 1.602176634e-19
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
# https://physics.nist.gov/cgi-bin/cuu/Value?ryd
r_inf = 10973731.568160
r_inf = ufloat(r_inf, r_inf*1.9e-12)
m0 = 2*h*a/e**2/c
z0 = m0*c
me = 4*pi*hbar*r_inf/c/a**2
print(f'µ_0 = {m0:S} N/A^2')
print(f'Z_0 = {z0:S} Ω')
print(f'me  = {me:S} kg')