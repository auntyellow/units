from uncertainties import ufloat
from math import pi, sqrt

cm = 1e-2
gram = 1e-03
dyn = gram*cm
erg = dyn*cm
c = 299792458
c_g = c/cm
h = 6.62607015e-34
h_g = h/erg
hbar = h/2/pi
hbar_g = hbar/erg
e = 1.602176634e-19
na = 6.02214076e+23
kb = 1.380649e-23
# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
# https://physics.nist.gov/cgi-bin/cuu/Value?ryd
r_inf = 10973731.568160
r_inf = ufloat(r_inf, r_inf*1.9e-12)
m0 = 2*h*a/e**2/c
e0 = e**2/2/c/h/a
z0 = 2*h*a/e**2
z0_g = 4*pi/c_g
statC = sqrt(dyn)*cm
c_statC = 1/(4*pi*e0)**.5/statC
e_g = e*c_statC
kj = 2*e/h
v_statV = 1/c_statC/erg
kj_g = kj/v_statV
rk = h/e**2
rk_g = z0_g/a/2
me = 2*h*r_inf/c/a**2
me_g = me/gram
mb = e*hbar/2/me
mb_g = e_g*hbar_g/2/me_g/c_g
f = na*e
f_g = f*c_statC
sb = 2*pi**5*kb**4/15/h**3/c**2
sb_g = 2*pi**5*kb**4/15/h_g**3/c_g**2
print(f'µ_0 = {m0:S} N/A^2')
print(f'Z_0 = {z0:S} Ω')
print(f'Z_0 = {z0_g} s/cm')
print(f'e   = {e_g:S} statC')
print(f'K_J = {kj} Hz/V')
print(f'K_J = {kj_g:S} Hz/statV')
print(f'R_K = {rk} Ω')
print(f'R_K = {rk_g:S} s/cm')
print(f'α   = {a:S}')
print(f'm_e = {me:S} kg')
print(f'm_e = {me_g:S} g')
print(f'µ_B = {mb:S} J/T')
print(f'µ_B = {mb_g:S} erg/G')
print(f'F   = {f} C/mol')
print(f'F   = {f_g:S} statC/mol')
print(f'σ   = {sb} W/m^2K^4')
print(f'σ   = {sb_g} erg/cm^2sK^4')
e_nu = (4*pi*a)**.5
r_inf_nu = r_inf*c*h/e
me_nu = 2*r_inf_nu/a**2
mb_nu = e_nu/2/me_nu
mu = 1.66053906660e-27
mu = ufloat(mu, mu*3e-10)
mu_nu = mu*c**2/e
print(f'e   = {e_nu:S}')
print(f'R_∞ = {r_inf_nu:S} eV')
print(f'm_e = {me_nu:S} eV')
print(f'µ_B = {mb_nu:S} eV^-1')
print(f'm_u = {mu_nu:S} eV')