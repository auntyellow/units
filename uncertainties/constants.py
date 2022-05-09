from uncertainties import ufloat
from math import pi, sqrt

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
e0 = e**2/2/c/h/a
z0 = 2*h*a/e**2
cm = 1e-2
z0_g = 4*pi/c*cm
dyn = 1e-05
statC = sqrt(dyn)*cm
c_statC = 1/(4*pi*e0)**.5/statC
e_g = e*c_statC
erg = 1e-07
v_statV = 1/c_statC/erg
kj = 2*e/h
kj_g = kj/v_statV
rk = h/e**2
rk_g = z0_g/a/2
me = 4*pi*hbar*r_inf/c/a**2
print(f'µ_0 = {m0:S} N/A^2')
print(f'Z_0 = {z0:S} Ω')
print(f'Z_0 = {z0_g} s/cm')
print(f'e   = {e_g:S} statC')
print(f'K_J = {kj} Hz/V')
print(f'K_J = {kj_g:S} Hz/statV')
print(f'R_K = {rk} Ω')
print(f'R_K = {rk_g:S} s/cm')
print(f'α   = {a:S}')
print(f'me  = {me:S} kg')